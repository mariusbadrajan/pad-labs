from flask import request, jsonify
from google.protobuf.json_format import MessageToJson
import app
from app.transactions import bp
from app.grpc.clients.account_client import AccountClient
from app.grpc.clients.transaction_client import TransactionClient

transaction_client = TransactionClient()
account_client = AccountClient()


@bp.route('/user/<int:user_id>', methods=['GET'])
def get_user_transactions(user_id):
    response = MessageToJson(transaction_client.get_user_transactions(user_id))
    app.cache.add_item(request, response)
    return response


@bp.route('/account/<int:account_id>', methods=['GET'])
def get_account_transactions(account_id):
    get_account_response = account_client.get_account_by_id(account_id)

    if get_account_response.message == 'Not found':
        return jsonify({'message': 'Account does not exist'})
    elif get_account_response.message == 'Ok':
        response = MessageToJson(transaction_client.get_account_transactions(account_id))
        app.cache.add_item(request, response)
        return response


@bp.route('/<int:id>', methods=['GET'])
def get_transaction_by_id(id):
    response = MessageToJson(transaction_client.get_transaction_by_id(id))
    app.cache.add_item(request, response)
    return response


@bp.route('/', methods=['POST'])
def create_transaction():
    request_data = request.get_json()
    account_id = request_data.get('accountId')
    amount = request_data.get('amount')
    user_id = request_data.get('userId')

    get_account_response = account_client.get_account_by_id(account_id)

    if get_account_response.message == 'Not found':
        return jsonify({'message': 'Account does not exist'})
    elif get_account_response.message == 'Ok':
        if get_account_response.balance - amount < 0:
            return jsonify({'message': 'Insufficient balance'})
        else:
            update_account_response = account_client.update_account(
                {'balance': get_account_response.balance - amount, 'id': account_id, 'userId': user_id})

            if update_account_response.message == 'Ok':
                return MessageToJson(transaction_client.create_transaction(request_data))
            else:
                return MessageToJson(update_account_response)
    else:
        return MessageToJson(get_account_response)


@bp.route('/', methods=['PUT'])
def update_transaction():
    request_data = request.get_json()
    transaction_id = request_data.get('id')
    account_id = request_data.get('accountId')
    amount = request_data.get('amount')
    user_id = request_data.get('userId')

    get_account_response = account_client.get_account_by_id(account_id)

    if get_account_response.message == 'Not found':
        return jsonify({'message': 'Account does not exist'})
    elif get_account_response.message == 'Ok':
        get_transaction_response = transaction_client.get_transaction_by_id(transaction_id)

        if get_transaction_response.message == 'Not found':
            return jsonify({'message': 'Transaction does not exist'})
        elif get_transaction_response.message == 'Ok':
            if get_account_response.balance + get_transaction_response.amount - amount < 0:
                return jsonify({'message': 'Insufficient balance'})
            else:
                update_account_response = account_client.update_account(
                    {'balance': get_account_response.balance + get_transaction_response.amount - amount,
                     'id': account_id, 'userId': user_id})
                if update_account_response.message == 'Ok':
                    return MessageToJson(transaction_client.update_transaction(request_data))
                else:
                    return MessageToJson(update_account_response)
        else:
            return MessageToJson(get_transaction_response)
    else:
        return MessageToJson(get_account_response)


@bp.route('/<int:id>', methods=['DELETE'])
def delete_transaction(id):
    return MessageToJson(transaction_client.delete_transaction(id))
