from app.grpc.protos import manager_pb2


class LoadBalancer:
    def __init__(self):
        self.services = {}
        self.service_index = {}

    def add_service(self, server):
        key = manager_pb2.ServiceType.Name(server.serviceType)
        if key not in self.services:
            self.services[key] = [server.host]
            self.service_index[key] = 0
            print(f"LB (REGISTERED NEW SERVICE): `{key}` service type was registered and hostname `{server.host}` was added to `{key}`.")
        elif server.host not in self.services[key]:
            self.services[key].append(server.host)
            print(f"LB (ADDED NEW SERVICE): `{key}` service with hostname `{server.host}` was added to `{key}`.")
        else:
            return

        print(f"\nAvailable service: {self.services}.\n")

    def remove_service(self, server):
        service_type, host = server
        if service_type in self.services and host in self.services[service_type]:
            self.services[service_type].remove(host)
            print(f"LB (REMOVED SERVICE): `{service_type}` service with hostname `{host}` was removed from `{service_type}`.")
            if not self.services[service_type]:
                del self.services[service_type]
                del self.service_index[service_type]
                print(f"LB (REMOVED SERVICE TYPE): `{service_type}` service type was completely removed.")
        else:
            print(
                f"LB (SERVICE NOT FOUND): Service with hostname `{host}` under `{service_type}` service type not found.")

        print(f"\nAvailable services: {self.services}.\n")

    def get_next_host(self, service_type):
        parsed_service_type = manager_pb2.ServiceType.Name(service_type)
        try:
            if parsed_service_type not in self.services:
                print(f"LB (SERVICE TYPE NOT FOUND): Service type `{parsed_service_type}` not found in services.")
                return None

            hosts = self.services[parsed_service_type]

            if not hosts:
                print(f"LB (HOSTS NOT FOUND): No hosts found for service type `{parsed_service_type}`.")

            index = self.service_index.get(parsed_service_type, 0)

            if index >= len(hosts):
                index = 0  # Reset the index if it exceeds the number of hosts available

            next_host = hosts[index]
            self.service_index[parsed_service_type] = (index + 1) % len(hosts)

            return next_host
        except Exception as e:
            print(e)
            return None


loadBalancer = LoadBalancer()
