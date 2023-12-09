import time

import grpc
from flask import request, jsonify
from google.protobuf.json_format import MessageToJson
import app
from app.accounts import bp
from app.grpc.clients.account_client import AccountClient
from app.grpc.clients.manager_client import ManagerClient

client = AccountClient()
type = 'Account'

@bp.route('/user/<int:user_id>', methods=['GET'])
def get_user_accounts(user_id):
    client = AccountClient()
    breaker = client.breaker
    try:
        url = ManagerClient.get_host(type)
        get_user_accounts_function = client.get_user_accounts
        response = get_user_accounts_function(user_id, url)
        app.cache.add_item(request, response)
        return MessageToJson(response)
    except grpc.RpcError as rpc_error:
        if isinstance(rpc_error, grpc.RpcError) and rpc_error.code() == grpc.StatusCode.NOT_FOUND:
            raise rpc_error
    except ConnectionRefusedError as connection_error:
        raise connection_error
    except Exception as error:
        while breaker.state.name == 'closed':
            time.sleep(3)
            try:
                response = get_user_accounts_function(user_id, url)
                app.cache.add_item(request, response)
                return MessageToJson(response)
            except grpc.RpcError as rpc_error:
                if isinstance(rpc_error, grpc.RpcError) and rpc_error.code() == grpc.StatusCode.NOT_FOUND:
                    raise rpc_error
            except Exception as innerError:
                pass

    if breaker.state.name == 'open':
        return get_user_accounts(user_id)


@bp.route('/<int:id>', methods=['GET'])
def get_account_by_id(id):
    client = AccountClient()
    breaker = client.breaker
    try:
        url = ManagerClient.get_host(type)
        get_account_by_id_function = client.get_account_by_id
        response = get_account_by_id_function(id, url)
        app.cache.add_item(request, response)
        return MessageToJson(response)
    except grpc.RpcError as rpc_error:
        if isinstance(rpc_error, grpc.RpcError) and rpc_error.code() == grpc.StatusCode.NOT_FOUND:
            raise rpc_error
    except ConnectionRefusedError as connection_error:
        raise connection_error
    except Exception as error:
        while breaker.state.name == 'closed':
            time.sleep(3)
            try:
                response = get_account_by_id_function(id, url)
                app.cache.add_item(request, response)
                return MessageToJson(response)
            except grpc.RpcError as rpc_error:
                if isinstance(rpc_error, grpc.RpcError) and rpc_error.code() == grpc.StatusCode.NOT_FOUND:
                    raise rpc_error
            except Exception as innerError:
                pass

    if breaker.state.name == 'open':
        return get_account_by_id(id)


@bp.route('/', methods=['POST'])
def create_account():
    client = AccountClient()
    breaker = client.breaker
    try:
        url = ManagerClient.get_host(type)
        request_data = request.get_json()
        create_account_function = client.create_account
        response = create_account_function(request_data, url)
        return MessageToJson(response)
    except grpc.RpcError as rpc_error:
        if isinstance(rpc_error, grpc.RpcError) and rpc_error.code() == grpc.StatusCode.NOT_FOUND:
            raise rpc_error
    except ConnectionRefusedError as connection_error:
        raise connection_error
    except Exception as error:
        while breaker.state.name == 'closed':
            time.sleep(3)
            try:
                response = create_account_function(request_data, url)
                return MessageToJson(response)
            except grpc.RpcError as rpc_error:
                if isinstance(rpc_error, grpc.RpcError) and rpc_error.code() == grpc.StatusCode.NOT_FOUND:
                    raise rpc_error
            except Exception as innerError:
                pass

    if breaker.state.name == 'open':
        return create_account()


@bp.route('/', methods=['PUT'])
def update_account():
    client = AccountClient()
    breaker = client.breaker
    try:
        url = ManagerClient.get_host(type)
        request_data = request.get_json()
        update_account_function = client.update_account
        response = update_account_function(request_data, url)
        return MessageToJson(response)
    except grpc.RpcError as rpc_error:
        if isinstance(rpc_error, grpc.RpcError) and rpc_error.code() == grpc.StatusCode.NOT_FOUND:
            raise rpc_error
    except ConnectionRefusedError as connection_error:
        raise connection_error
    except Exception as error:
        while breaker.state.name == 'closed':
            time.sleep(3)
            try:
                response = update_account_function(id, url)
                return MessageToJson(response)
            except grpc.RpcError as rpc_error:
                if isinstance(rpc_error, grpc.RpcError) and rpc_error.code() == grpc.StatusCode.NOT_FOUND:
                    raise rpc_error
            except Exception as innerError:
                pass

    if breaker.state.name == 'open':
        return update_account()

@bp.route('/<int:id>', methods=['DELETE'])
def delete_account(id):
    client = AccountClient()
    breaker = client.breaker
    try:
        url = ManagerClient.get_host(type)
        delete_account_function = client.delete_account
        response = delete_account_function(id, url)
        return MessageToJson(response)
    except grpc.RpcError as rpc_error:
        if isinstance(rpc_error, grpc.RpcError) and rpc_error.code() == grpc.StatusCode.NOT_FOUND:
            raise rpc_error
    except ConnectionRefusedError as connection_error:
        raise connection_error
    except Exception as error:
        while breaker.state.name == 'closed':
            time.sleep(3)
            try:
                response = delete_account_function(id, url)
                return MessageToJson(response)
            except grpc.RpcError as rpc_error:
                if isinstance(rpc_error, grpc.RpcError) and rpc_error.code() == grpc.StatusCode.NOT_FOUND:
                    raise rpc_error
            except Exception as innerError:
                pass

    if breaker.state.name == 'open':
        return delete_account(id)
