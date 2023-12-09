import threading
import time
from urllib.parse import urlparse

import grpc

from app.grpc.protos import manager_pb2_grpc, manager_pb2
from app.helpers.load_balancer import loadBalancer


class HealthChecker:
    def __init__(self):
        self.health_check_interval_sec = 30
        self.is_running = False

    def check_server_health(self, host):
        parsed_url = urlparse(host)
        channel = grpc.insecure_channel(f"{parsed_url.hostname}:{parsed_url.port}")
        stub = manager_pb2_grpc.ManagerServiceStub(channel)
        return stub.GetHealthStatus(manager_pb2.GetHealthStatusRequest())

    def check_health(self, server, statuses, isRetry = False):
        service_type, host = server
        print(f"HEALTH CHECKER of `{host}`{'-RETRY' if isRetry else ''}: Checking health...")
        try:
            health_status = self.check_server_health(host)
            print(f"HEALTH CHECKER of `{host}`: Status: {manager_pb2.HealthStatus.Name(health_status.healthStatus)}")
            status = "Success"
        except grpc.RpcError as rpc_error:
            if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
                print(f"HEALTH CHECKER of `{host}: Server is down. Removing from registered services...`")
                loadBalancer.remove_service(server)
            elif rpc_error.code() == grpc.StatusCode.DEADLINE_EXCEEDED:
                if isRetry:
                    print(f"HEALTH CHECKER of `{host}`{'-RETRY' if isRetry else ''}: Taking too long to check health. Removing from registered services...")
                    loadBalancer.remove_service(server)
                else:
                    print(f"HEALTH CHECKER of `{host}: Taking too long to check health. Retrying...`")
                    self.check_health(server, True)
            status = "RpcError"
        except Exception as e:
            print(e)
            status = "Error"

        statuses.append(status)

    def start_health_checks(self):
        if self.is_running:
            return

        self.is_running = True

        while self.is_running:
            print(f"HEALTH CHECKER: Starting health check process of currently registered services...")
            threads = []
            # Needed in case API Gateway will keep track of all available services and we need to send updates when some services become unavailable
            statuses = []

            for service_type, hosts in loadBalancer.services.items():
                for host in hosts:
                    thread = threading.Thread(target=self.check_health, args=((service_type, host), statuses))
                    threads.append(thread)
                    thread.start()

            for thread in threads:
                thread.join()

            for status in statuses:
                if status == "Error":
                    pass
                elif status == "RpcError":
                    pass
                elif status == "Success":
                    pass

            print(f"HEALTH CHECKER: Finished health check process.")
            time.sleep(self.health_check_interval_sec)

    def stop_health_checks(self):
        self.is_running = False


health_checker = HealthChecker()
