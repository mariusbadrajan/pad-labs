import grpc

from protos import transaction_pb2, transaction_pb2_grpc


class TransactionClient:
    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:5177')
        self.stub = transaction_pb2_grpc.TransactionServiceStub(self.channel)

    def get_user_transactions(self, user_id):
        request = transaction_pb2.GetUserTransactionsRequest(userId=user_id)
        return self.stub.GetUserTransactions(request)

    def get_account_transactions(self, account_id):
        request = transaction_pb2.GetAccountTransactionsRequest(accountId=account_id)
        return self.stub.GetAccountTransactions(request)

    def get_transaction_by_id(self, id):
        request = transaction_pb2.GetTransactionByIdRequest(id=id)
        return self.stub.GetTransactionById(request)

    def create_transaction(self, transaction):
        request = transaction_pb2.AddTransactionRequest(transaction=transaction)
        return self.stub.CreatePaymentTransaction(request)

    def update_transaction(self, transaction):
        request = transaction_pb2.UpdateTransactionRequest(transaction=transaction)
        return self.stub.UpdateTransaction(request)

    def delete_transaction(self, id):
        request = transaction_pb2.DeleteTransactionRequest(id=id)
        return self.stub.DeleteTransaction(request)