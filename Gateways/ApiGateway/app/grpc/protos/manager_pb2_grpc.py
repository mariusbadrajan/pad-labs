# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import app.grpc.protos.manager_pb2 as manager__pb2


class ManagerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetHealthStatus = channel.unary_unary(
                '/manager.ManagerService/GetHealthStatus',
                request_serializer=manager__pb2.GetHealthStatusRequest.SerializeToString,
                response_deserializer=manager__pb2.GetHealthStatusResponse.FromString,
                )
        self.RegisterService = channel.unary_unary(
                '/manager.ManagerService/RegisterService',
                request_serializer=manager__pb2.RegisterServiceRequest.SerializeToString,
                response_deserializer=manager__pb2.RegisterServiceResponse.FromString,
                )
        self.GetServiceHost = channel.unary_unary(
                '/manager.ManagerService/GetServiceHost',
                request_serializer=manager__pb2.GetServiceHostRequest.SerializeToString,
                response_deserializer=manager__pb2.GetServiceHostResponse.FromString,
                )


class ManagerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetHealthStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServiceHost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ManagerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetHealthStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHealthStatus,
                    request_deserializer=manager__pb2.GetHealthStatusRequest.FromString,
                    response_serializer=manager__pb2.GetHealthStatusResponse.SerializeToString,
            ),
            'RegisterService': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterService,
                    request_deserializer=manager__pb2.RegisterServiceRequest.FromString,
                    response_serializer=manager__pb2.RegisterServiceResponse.SerializeToString,
            ),
            'GetServiceHost': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServiceHost,
                    request_deserializer=manager__pb2.GetServiceHostRequest.FromString,
                    response_serializer=manager__pb2.GetServiceHostResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'manager.ManagerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ManagerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetHealthStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/manager.ManagerService/GetHealthStatus',
            manager__pb2.GetHealthStatusRequest.SerializeToString,
            manager__pb2.GetHealthStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/manager.ManagerService/RegisterService',
            manager__pb2.RegisterServiceRequest.SerializeToString,
            manager__pb2.RegisterServiceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServiceHost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/manager.ManagerService/GetServiceHost',
            manager__pb2.GetServiceHostRequest.SerializeToString,
            manager__pb2.GetServiceHostResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
