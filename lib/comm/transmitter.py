import socket
from abc import ABC, abstractmethod

from .protocols import packet_pb2

class Transmitter(ABC):
    def __init__(self, transmitter_ip='224.0.0.1', transmitter_port=10002):
        """
        Init Client object.
        Extended description of function.
        Parameters
        ----------
        ip : str
            Multicast IP in format '255.255.255.255'.
        port : int
            Port up to 1024.
        """

        self.transmitter_ip = transmitter_ip
        self.transmitter_port = transmitter_port

        # Create socket
        self.transmitter_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    @abstractmethod
    def transmit(self, packet):
        """
        Transmit packet.
        """

        data = packet.SerializeToString()

        self.transmitter_socket.sendto(data, (self.transmitter_ip, self.transmitter_port))
