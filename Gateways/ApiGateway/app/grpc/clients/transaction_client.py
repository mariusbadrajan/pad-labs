import grpc

from app.grpc.clients.manager_client import ManagerClient
from app.grpc.protos import transaction_pb2_grpc, transaction_pb2


class TransactionClient:
    def __init__(self):
        self.type = 'Transaction'

    def get_user_transactions(self, user_id):
        url = ManagerClient.get_host(self.type)
        channel = grpc.insecure_channel(url)
        stub = transaction_pb2_grpc.TransactionServiceStub(channel)
        request = transaction_pb2.GetUserTransactionsRequest(userId=user_id)
        return stub.GetUserTransactions(request)

    def get_account_transactions(self, account_id):
        url = ManagerClient.get_host(self.type)
        channel = grpc.insecure_channel(url)
        stub = transaction_pb2_grpc.TransactionServiceStub(channel)
        request = transaction_pb2.GetAccountTransactionsRequest(accountId=account_id)
        return stub.GetAccountTransactions(request)

    def get_transaction_by_id(self, id):
        url = ManagerClient.get_host(self.type)
        channel = grpc.insecure_channel(url)
        stub = transaction_pb2_grpc.TransactionServiceStub(channel)
        request = transaction_pb2.GetTransactionByIdRequest(id=id)
        return stub.GetTransactionById(request)

    def create_transaction(self, transaction):
        url = ManagerClient.get_host(self.type)
        channel = grpc.insecure_channel(url)
        stub = transaction_pb2_grpc.TransactionServiceStub(channel)
        request = transaction_pb2.AddTransactionRequest(transaction=transaction)
        return stub.CreatePaymentTransaction(request)

    def update_transaction(self, transaction):
        url = ManagerClient.get_host(self.type)
        channel = grpc.insecure_channel(url)
        stub = transaction_pb2_grpc.TransactionServiceStub(channel)
        request = transaction_pb2.UpdateTransactionRequest(transaction=transaction)
        return stub.UpdateTransaction(request)

    def delete_transaction(self, id):
        url = ManagerClient.get_host(self.type)
        channel = grpc.insecure_channel(url)
        stub = transaction_pb2_grpc.TransactionServiceStub(channel)
        request = transaction_pb2.DeleteTransactionRequest(id=id)
        return stub.DeleteTransaction(request)