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
