import grpc

from protos import account_pb2_grpc, account_pb2


class AccountClient:
    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:5165')
        self.stub = account_pb2_grpc.AccountServiceStub(self.channel)

    def get_user_accounts(self, user_id):
        request = account_pb2.GetUserAccountsRequest(userId=user_id)
        return self.stub.GetUserAccounts(request)

    def get_account_by_id(self, id):
        request = account_pb2.GetAccountByIdRequest(id=id)
        return self.stub.GetAccountById(request)

    def create_account(self, account):
        request = account_pb2.AddAccountRequest(account=account)
        return self.stub.CreateAccount(request)

    def update_account(self, account):
        request = account_pb2.UpdateAccountRequest(account=account)
        return self.stub.UpdateAccount(request)

    def delete_account(self, id):
        request = account_pb2.DeleteAccountRequest(id=id)
        return self.stub.DeleteAccount(request)
