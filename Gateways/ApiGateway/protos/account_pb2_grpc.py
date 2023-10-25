# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos import account_pb2 as account__pb2


class AccountServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUserAccounts = channel.unary_unary(
                '/account.AccountService/GetUserAccounts',
                request_serializer=account__pb2.GetUserAccountsRequest.SerializeToString,
                response_deserializer=account__pb2.AccountsResponse.FromString,
                )
        self.GetAccountById = channel.unary_unary(
                '/account.AccountService/GetAccountById',
                request_serializer=account__pb2.GetAccountByIdRequest.SerializeToString,
                response_deserializer=account__pb2.AccountResponse.FromString,
                )
        self.CreateAccount = channel.unary_unary(
                '/account.AccountService/CreateAccount',
                request_serializer=account__pb2.AddAccountRequest.SerializeToString,
                response_deserializer=account__pb2.AccountResponse.FromString,
                )
        self.UpdateAccount = channel.unary_unary(
                '/account.AccountService/UpdateAccount',
                request_serializer=account__pb2.UpdateAccountRequest.SerializeToString,
                response_deserializer=account__pb2.AccountResponse.FromString,
                )
        self.DeleteAccount = channel.unary_unary(
                '/account.AccountService/DeleteAccount',
                request_serializer=account__pb2.DeleteAccountRequest.SerializeToString,
                response_deserializer=account__pb2.AccountResponse.FromString,
                )


class AccountServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetUserAccounts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAccountById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AccountServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUserAccounts': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserAccounts,
                    request_deserializer=account__pb2.GetUserAccountsRequest.FromString,
                    response_serializer=account__pb2.AccountsResponse.SerializeToString,
            ),
            'GetAccountById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAccountById,
                    request_deserializer=account__pb2.GetAccountByIdRequest.FromString,
                    response_serializer=account__pb2.AccountResponse.SerializeToString,
            ),
            'CreateAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAccount,
                    request_deserializer=account__pb2.AddAccountRequest.FromString,
                    response_serializer=account__pb2.AccountResponse.SerializeToString,
            ),
            'UpdateAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAccount,
                    request_deserializer=account__pb2.UpdateAccountRequest.FromString,
                    response_serializer=account__pb2.AccountResponse.SerializeToString,
            ),
            'DeleteAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAccount,
                    request_deserializer=account__pb2.DeleteAccountRequest.FromString,
                    response_serializer=account__pb2.AccountResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'account.AccountService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AccountService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetUserAccounts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.AccountService/GetUserAccounts',
            account__pb2.GetUserAccountsRequest.SerializeToString,
            account__pb2.AccountsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAccountById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.AccountService/GetAccountById',
            account__pb2.GetAccountByIdRequest.SerializeToString,
            account__pb2.AccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.AccountService/CreateAccount',
            account__pb2.AddAccountRequest.SerializeToString,
            account__pb2.AccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.AccountService/UpdateAccount',
            account__pb2.UpdateAccountRequest.SerializeToString,
            account__pb2.AccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.AccountService/DeleteAccount',
            account__pb2.DeleteAccountRequest.SerializeToString,
            account__pb2.AccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
