from storage_interface import Storage

class Minio(Storage):
    def download(self):
        return "I am Minio."