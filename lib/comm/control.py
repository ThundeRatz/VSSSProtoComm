import logging

from .transmitter import Transmitter
from .protocols import packet_pb2
from .protocols import command_pb2
from ..core.command import TeamCommand

from .thread_job import Job

class ProtoControl(Transmitter):
    def __init__(self, team_color_yellow: bool, team_command: TeamCommand = None, control_ip='127.0.0.1', control_port=20011):
        super(ProtoControl, self).__init__(control_ip, control_port)

        self.team_color_yellow = team_color_yellow
        self.team_command = team_command


    def transmit(self, packet: packet_pb2.Packet):
        super().transmit(packet)


    def transmit_robot(self, robot_id, left_speed, right_speed):
        """
        Encode package and transmit.
        """

        packet = self._fill_robot_command_packet(robot_id, left_speed, right_speed)

        self.transmit(packet)


    def _fill_robot_command_packet(self, robot_id, left_speed, right_speed):
        cmd_packet = command_pb2.Commands()

        robot = cmd_packet.robot_commands.add() # pylint: disable=no-member
        robot.id          = robot_id
        robot.yellowteam  = self.team_color_yellow
        robot.wheel_left  = left_speed
        robot.wheel_right = right_speed

        packet = packet_pb2.Packet()
        packet.cmd.CopyFrom(cmd_packet) # pylint: disable=no-member

        return packet

    def transmit_team(self, team_cmd : TeamCommand):
        """
        Encode package and transmit.

        Parameters
        ----------
        team_cmd : core.commands.TeamCommand
            Commands to all robots
        """

        packet = self._fill_team_command_packet(team_cmd)

        self.transmit(packet)


    def update(self):
        """
        Update the transmitted packet with the team_command
        passed in the constructor
        """

        if self.team_command is None:
            logging.error('TeamCommand not instantiated', exc_info=True)
        else:
            self.transmit_team(self.team_command)


    def stop_team(self):
        stop_team_cmd = TeamCommand()
        self.transmit_team(stop_team_cmd)


    def _fill_team_command_packet(self, team_command : TeamCommand):
        cmd_packet = command_pb2.Commands()

        for i in range(len(team_command.commands)):
            cmd = cmd_packet.robot_commands.add() # pylint: disable=no-member
            cmd.id          = i
            cmd.yellowteam  = self.team_color_yellow
            cmd.wheel_left  = team_command.commands[i].left_speed
            cmd.wheel_right = team_command.commands[i].right_speed

        packet = packet_pb2.Packet()
        packet.cmd.CopyFrom(cmd_packet) # pylint: disable=no-member

        return packet


class ProtoControlThread(Job):
    def __init__(self, team_color_yellow: bool, team_command: TeamCommand = None, control_ip='127.0.0.1', control_port=20011):
        self.control = ProtoControl(team_color_yellow, team_command, control_ip, control_port)

        super(ProtoControlThread, self).__init__(self.control.update)


    def pause(self):
        super().pause()
        self.control.stop_team()


    def resume(self):
        super().resume()


    def stop(self):
        super().pause()
        self.control.stop_team()
