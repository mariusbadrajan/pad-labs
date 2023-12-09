import grpc
from pybreaker import CircuitBreaker

from app.grpc.clients.manager_client import ManagerClient
from app.grpc.protos import account_pb2_grpc, account_pb2


class AccountClient:
    def __init__(self):
        self.type = 'Account'
        self.breaker = CircuitBreaker(fail_max=3, reset_timeout=10, exclude=[
            lambda error: isinstance(error, grpc.RpcError) and error.code() == grpc.StatusCode.NOT_FOUND])

    def get_user_accounts(self, user_id):
        url = ManagerClient.get_host(self.type)
        channel = grpc.insecure_channel(url)
        stub = account_pb2_grpc.AccountServiceStub(channel)
        request = account_pb2.GetUserAccountsRequest(userId=user_id)
        return stub.GetUserAccounts(request)

    def get_account_by_id(self, id):
        url = ManagerClient.get_host(self.type)
        channel = grpc.insecure_channel(url)
        stub = account_pb2_grpc.AccountServiceStub(channel)
        request = account_pb2.GetAccountByIdRequest(id=id)
        return stub.GetAccountById(request)

    def create_account(self, account):
        url = ManagerClient.get_host(self.type)
        channel = grpc.insecure_channel(url)
        stub = account_pb2_grpc.AccountServiceStub(channel)
        request = account_pb2.AddAccountRequest(account=account)
        return stub.CreateAccount(request)

    def update_account(self, account):
        url = ManagerClient.get_host(self.type)
        channel = grpc.insecure_channel(url)
        stub = account_pb2_grpc.AccountServiceStub(channel)
        request = account_pb2.UpdateAccountRequest(account=account)
        return stub.UpdateAccount(request)

    @property
    def delete_account(self):
        @self.breaker
        def delete_account_internal(id, url):
            channel = grpc.insecure_channel(url)
            stub = account_pb2_grpc.AccountServiceStub(channel)
            request = account_pb2.DeleteAccountRequest(id=id)
            return stub.DeleteAccount(request)

        return delete_account_internal
