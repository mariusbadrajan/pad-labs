from flask import request
from google.protobuf.json_format import MessageToJson
import app
from app.accounts import bp
from app.grpc.account_client import AccountClient

client = AccountClient()


@bp.route('/user/<int:user_id>', methods=['GET'])
def get_user_accounts(user_id):
    response = MessageToJson(client.get_user_accounts(user_id))
    app.cache.add_item(request, response)
    return response


@bp.route('/<int:id>', methods=['GET'])
def get_account_by_id(id):
    response = MessageToJson(client.get_account_by_id(id))
    app.cache.add_item(request, response)
    return response


@bp.route('/', methods=['POST'])
def create_account():
    request_data = request.get_json()
    return MessageToJson(client.create_account(request_data))


@bp.route('/', methods=['PUT'])
def update_account():
    request_data = request.get_json()
    return MessageToJson(client.update_account(request_data))


@bp.route('/<int:id>', methods=['DELETE'])
def delete_account(id):
    return MessageToJson(client.delete_account(id))
