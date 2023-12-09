import grpc
from pybreaker import CircuitBreaker

from app.grpc.protos import account_pb2_grpc, account_pb2


class AccountClient:
    def __init__(self):
        self.type = 'Account'
        self.breaker = CircuitBreaker(fail_max=3, reset_timeout=10, exclude=[
            lambda error: isinstance(error, grpc.RpcError) and error.code() == grpc.StatusCode.NOT_FOUND])

    @property
    def get_user_accounts(self):
        def get_user_accounts_internal(user_id, url):
            channel = grpc.insecure_channel(url)
            stub = account_pb2_grpc.AccountServiceStub(channel)
            request = account_pb2.GetUserAccountsRequest(userId=user_id)
            return stub.GetUserAccounts(request)

        return get_user_accounts_internal()

    @property
    def get_account_by_id(self):
        @self.breaker
        def get_account_by_id_internal(id, url):
            channel = grpc.insecure_channel(url)
            stub = account_pb2_grpc.AccountServiceStub(channel)
            request = account_pb2.GetAccountByIdRequest(id=id)
            return stub.GetAccountById(request)

        return get_account_by_id_internal

    @property
    def create_account(self):
        @self.breaker
        def create_account_internal(user_id, url):
            channel = grpc.insecure_channel(url)
            stub = account_pb2_grpc.AccountServiceStub(channel)
            request = account_pb2.AddAccountRequest(userId=user_id)
            return stub.CreateAccount(request)

        return create_account_internal

    @property
    def update_account(self):
        @self.breaker
        def update_account_internal(account, url):
            channel = grpc.insecure_channel(url)
            stub = account_pb2_grpc.AccountServiceStub(channel)
            request = account_pb2.UpdateAccountRequest(id=account.id,
                                                       userId=account.userId,
                                                       balance=account.balance)
            return stub.UpdateAccount(request)

        return update_account_internal

    @property
    def delete_account(self):
        @self.breaker
        def delete_account_internal(id, url):
            channel = grpc.insecure_channel(url)
            stub = account_pb2_grpc.AccountServiceStub(channel)
            request = account_pb2.DeleteAccountRequest(id=id)
            return stub.DeleteAccount(request)

        return delete_account_internal
