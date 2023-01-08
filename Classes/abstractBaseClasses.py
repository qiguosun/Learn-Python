# issue 1: we shouldn't be directly create a instance of stream class
# issue 2: need a common interface across different kind of streams
# the name of module is all lower case (abc) while the name of the classes are all upper case (ABC)
from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("reading data from a network")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream")


# stream = Stream()  #abstract class cannot be instanciate
filestream = MemoryStream()
filestream.open()
