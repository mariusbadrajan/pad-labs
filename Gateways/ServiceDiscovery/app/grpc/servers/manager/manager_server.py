from concurrent import futures

import grpc

from app.grpc.protos import manager_pb2_grpc, manager_pb2
from app.helpers.load_balancer import loadBalancer


class ManagerServiceServicer(manager_pb2_grpc.ManagerServiceServicer):
    def RegisterService(self, request, context):
        loadBalancer.add_service(request)
        response = manager_pb2.RegisterServiceResponse(message="Registered")
        return response

    def GetServiceHost(self, request, context):
        host = loadBalancer.get_next_host(request.serviceType)
        if host is None:
            context.set_code(grpc.StatusCode.RESOURCE_EXHAUSTED)
            context.set_details("No services are available at the moment. Try again later.")
            return manager_pb2.GetServiceHostResponse()

        response = manager_pb2.GetServiceHostResponse(host=host)
        return response


class ManagerServer:
    def __init__(self):
        pass

    @staticmethod
    def serve():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        manager_pb2_grpc.add_ManagerServiceServicer_to_server(ManagerServiceServicer(), server)
        server.add_insecure_port("[::]:50051")
        server.start()
        print("Service discovery has started ...")
        server.wait_for_termination()
