from time import sleep
from urllib.parse import urlparse

import grpc

from app.grpc.protos import manager_pb2_grpc, manager_pb2

MAX_REGISTER_RETRIES = 3
REGISTER_RETRY_DELAY_MS = 3


class ManagerClient:
    def __init__(self):
        pass

    @staticmethod
    def get_host(service_type):
        retries = 0
        connected = False
        host = None

        while not connected and retries < MAX_REGISTER_RETRIES:
            try:
                parsed_service_type = manager_pb2.ServiceType.Value(service_type)
                channel = grpc.insecure_channel("localhost:50051")
                stub = manager_pb2_grpc.ManagerServiceStub(channel)
                response = stub.GetServiceHost(manager_pb2.GetServiceHostRequest(serviceType=parsed_service_type))
                parsed_url = urlparse(response.host)
                host = f"{parsed_url.hostname}:{parsed_url.port}"
                connected = True
            except grpc.RpcError as rpc_error:
                if (rpc_error.code() == grpc.StatusCode.RESOURCE_EXHAUSTED):
                    raise rpc_error
                print(f"Failed to get host for {parsed_service_type}: {rpc_error.code()}. Retry: {retries + 1}")
                retries += 1
                sleep(REGISTER_RETRY_DELAY_MS)  # Sleep in seconds

        if not connected:
            print("Failed to get host after all retries.")
            raise ConnectionRefusedError('Service discovery unavailable.')

        return host

