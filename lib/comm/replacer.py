import logging
from typing import List

from .transmitter import Transmitter
from .protocols import vssref_placement_pb2
from ..core.data import EntityData


class ReplacerComm(Transmitter):
    def __init__(self, team_color_yellow: bool, replacer_ip='224.5.23.2', replacer_port=10004):
        super(ReplacerComm, self).__init__(replacer_ip, replacer_port)

        self.team_color_yellow = team_color_yellow


    def transmit(self, packet):
        super().transmit(packet)


    def place_team(self, replacement_list):
        """
        Encode package and transmit.

        Args:
            replacement_list (list): List of tuples with the entity data and it`s id
        """
        packet = self._fill_robot_command_packet(replacement_list)

        self.transmit(packet)


    def _fill_robot_command_packet(self, replacement_list):
        placement_packet = vssref_placement_pb2.VSSRef_Placement()
        placement_packet.world.teamColor = int(self.team_color_yellow)

        for desired_placement in replacement_list:
            entity_data, robot_id = desired_placement

            robot = placement_packet.world.robots.add()
            robot.robot_id = int(robot_id)
            robot.x = entity_data.position.x
            robot.y = entity_data.position.y
            robot.orientation = entity_data.position.theta

        return placement_packet
