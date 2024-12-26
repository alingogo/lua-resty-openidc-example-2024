import abc

class Storage(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def download(self, data):
        """Stream data into a specified place"""
        raise NotImplementedError