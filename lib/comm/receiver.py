import socket
import struct
from abc import ABC, abstractmethod

class Receiver(ABC):
    def __init__(self, receiver_ip='224.0.0.1', receiver_port=10002):
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

        self.receiver_ip = receiver_ip
        self.receiver_port = receiver_port

        # Create socket
        self.receiver_socket = self._create_socket()

    @abstractmethod
    def receive(self):
        """
        Receive packet.
        """

        data, _ = self.receiver_socket.recvfrom(1024)

        return data


    def _create_socket(self):
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM,
            socket.IPPROTO_UDP
        )

        sock.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_REUSEADDR, 1
        )

        sock.bind((self.receiver_ip, self.receiver_port))

        mreq = struct.pack(
            "4sl",
            socket.inet_aton(self.receiver_ip),
            socket.INADDR_ANY
        )

        sock.setsockopt(
            socket.IPPROTO_IP,
            socket.IP_ADD_MEMBERSHIP,
            mreq
        )

        return sock
