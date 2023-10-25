class InMemoryCache:
    def __init__(self):
        self.cache_items = {}

    def add_item(self, request, response):
        if 'Request timeout' in response or 'Not found' in response or 'Collection is empty' in response:
            return

        key = request.endpoint
        if key in self.cache_items:
            self.cache_items[key].append(response)
        else:
            self.cache_items[key] = [response]