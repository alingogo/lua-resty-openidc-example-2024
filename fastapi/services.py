"""Services module."""

from storage_interface import Storage


class MyService:
    def __init__(self, storage_client: Storage):
        self.storage_client = storage_client

    async def name(self):
        return self.storage_client.download()