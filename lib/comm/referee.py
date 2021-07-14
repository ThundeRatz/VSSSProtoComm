from .receiver import Receiver
from .protocols import vssref_command_pb2

import json
from google.protobuf.json_format import MessageToJson

class RefereeComm(Receiver):
    def __init__(self, referee_ip='224.5.23.2', referee_port=10003):
        super(RefereeComm, self).__init__(referee_ip, referee_port)
        self.receiver_socket.setblocking(False)
        self.last_rcv_data = {}

    def receive(self):
        """
        Receive packet and decode.
        """

        try:
            data = super().receive()
            decoded_data = vssref_command_pb2.VSSRef_Command().FromString(data) # pylint: disable=no-member

            referee_data = json.loads(MessageToJson(decoded_data))
            self.last_rcv_data = referee_data
        except BlockingIOError:
            referee_data = self.last_rcv_data

        return referee_data
