import json

import grpc
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from app.accounts import bp as accounts_bp
from app.helpers.in_memory_cache import InMemoryCache as Cache
from app.transactions import bp as transactions_bp

cache = Cache()


def create_app():
    app = Flask(__name__)
    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=["5/second"],
    )

    # Register blueprints here
    app.register_blueprint(accounts_bp, url_prefix='/accounts')
    app.register_blueprint(transactions_bp, url_prefix='/transactions')

    @app.before_request
    def before_hook():
        cached_items = cache.cache_items
        if request.method == 'GET' and request.endpoint in cached_items:
            if 'by_id' in request.endpoint:
                values = cached_items[request.endpoint]
                for obj_str in values:
                    obj = json.loads(obj_str)
                    id = int(request.path.split('/')[-1])
                    if obj.get('id') == id:
                        return obj
            else:
                return json.loads(cached_items.get(request.endpoint)[0])
        elif request.method == 'POST':
            view = request.path.split('/')[1]
            if view == 'accounts':
                for key in list(cached_items.keys()):
                    if 'get_user_accounts' in key:
                        del cached_items[key]
            elif view == 'transactions':
                for key in list(cached_items.keys()):
                    if 'get_user_transactions' in key or 'get_account_transactions' in key:
                        del cached_items[key]
        elif request.method == 'PUT':
            view = request.path.split('/')[1]
            if view == 'accounts':
                for key in list(cached_items.keys()):
                    if 'get_account_by_id' in key:
                        values = cached_items[key]
                        for obj in values:
                            if json.loads(obj).get('id') == request.get_json().get('id'):
                                values.remove(obj)
                    elif 'get_user_accounts' in key:
                        del cached_items[key]
            elif view == 'transactions':
                for key in list(cached_items.keys()):
                    if 'get_transaction_by_id' in key:
                        values = cached_items[key]
                        for obj in values:
                            if json.loads(obj).get('id') == request.get_json().get('id'):
                                values.remove(obj)
                    elif 'get_user_transactions' in key or 'get_account_transactions' in key:
                        del cached_items[key]
        elif request.method == 'DELETE':
            view = request.path.split('/')[1]
            if view == 'accounts':
                for key in list(cached_items.keys()):
                    if 'get_account_by_id' in key:
                        values = cached_items[key]
                        for obj in values:
                            if json.loads(obj).get('id') == int(request.path.split('/')[-1]):
                                values.remove(obj)
                    elif 'get_user_accounts' in key:
                        del cached_items[key]
            elif view == 'transactions':
                for key in list(cached_items.keys()):
                    if 'get_transaction_by_id' in key:
                        values = cached_items[key]
                        for obj in values:
                            if json.loads(obj).get('id') == int(request.path.split('/')[-1]):
                                values.remove(obj)
                    elif 'get_user_transactions' in key or 'get_account_transactions' in key:
                        del cached_items[key]

    @app.errorhandler(Exception)
    def all_exception_handler(error):
        if isinstance(error, grpc.RpcError):
            message = error.details()
            return jsonify({"error": "gRPC error", "message": message}), 500

        return jsonify({"error": "Unhandled exception", "message": str(error)}), 500

    return app


app = create_app()

if __name__ == '__main__':
    app.run()

# python -m grpc_tools.protoc -I app/grpc/protos --python_out=app/grpc/protos --grpc_python_out=app/grpc/protos app/grpc/protos/manager.proto
