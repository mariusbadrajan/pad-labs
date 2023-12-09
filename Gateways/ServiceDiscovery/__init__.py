import threading

from app.grpc.servers.manager.manager_server import ManagerServer
from app.helpers.health_checker import health_checker

if __name__ == '__main__':
    health_check_thread = threading.Thread(target=health_checker.start_health_checks)
    health_check_thread.start()
    ManagerServer.serve()

# python -m grpc_tools.protoc -I app/grpc/protos --python_out=app/grpc/protos --grpc_python_out=app/grpc/protos app/grpc/protos/manager.proto
