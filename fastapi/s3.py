from storage_interface import Storage

class S3(Storage):
    def download(self):
        return "I am S3."