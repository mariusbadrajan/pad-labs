import grpc
from pybreaker import CircuitBreaker

from app.grpc.clients.manager_client import ManagerClient
from app.grpc.protos import transaction_pb2_grpc, transaction_pb2


class TransactionClient:
    def __init__(self):
        self.type = 'Transaction'
        self.breaker = CircuitBreaker(fail_max=3, reset_timeout=10, exclude=[
            lambda error: isinstance(error, grpc.RpcError) and error.code() == grpc.StatusCode.NOT_FOUND])

    @property
    def get_user_transactions(self):
        @self.breaker
        def get_user_transactions_internal(user_id, url):
            channel = grpc.insecure_channel(url)
            stub = transaction_pb2_grpc.TransactionServiceStub(channel)
            request = transaction_pb2.GetUserTransactionsRequest(userId=user_id)
            return stub.GetUserTransactions(request)

        return get_user_transactions_internal

    @property
    def get_account_transactions(self):
        @self.breaker
        def get_account_transactions_internal(account_id, url):
            channel = grpc.insecure_channel(url)
            stub = transaction_pb2_grpc.TransactionServiceStub(channel)
            request = transaction_pb2.GetAccountTransactionsRequest(accountId=account_id)
            return stub.GetAccountTransactions(request)

        return get_account_transactions_internal

    @property
    def get_transaction_by_id(self):
        @self.breaker
        def get_transaction_by_id_internal(id, url):
            channel = grpc.insecure_channel(url)
            stub = transaction_pb2_grpc.TransactionServiceStub(channel)
            request = transaction_pb2.GetTransactionByIdRequest(id=id)
            return stub.GetTransactionById(request)

        return get_transaction_by_id_internal

    @property
    def create_transaction(self):
        @self.breaker
        def create_transaction_internal(transaction, url):
            channel = grpc.insecure_channel(url)
            stub = transaction_pb2_grpc.TransactionServiceStub(channel)
            request = transaction_pb2.AddTransactionRequest(userId=transaction.userId,
                                                            accountId=transaction.accountId,
                                                            amount=transaction.amount)
            return stub.CreatePaymentTransaction(request)

        return create_transaction_internal

    @property
    def update_transaction(self):
        @self.breaker
        def update_transaction_internal(transaction, url):
            channel = grpc.insecure_channel(url)
            stub = transaction_pb2_grpc.TransactionServiceStub(channel)
            request = transaction_pb2.UpdateTransactionRequest(id=transaction.id,
                                                               userId=transaction.userId,
                                                               accountId=transaction.accountId,
                                                               type=transaction.type,
                                                               amount=transaction.amount,
                                                               status=transaction.status)
            return stub.UpdateTransaction(request)

        return update_transaction_internal

    @property
    def delete_transaction(self):
        @self.breaker
        def delete_transaction_internal(id, url):
            channel = grpc.insecure_channel(url)
            stub = transaction_pb2_grpc.TransactionServiceStub(channel)
            request = transaction_pb2.DeleteTransactionRequest(id=id)
            return stub.DeleteTransaction(request)

        return delete_transaction_internal
