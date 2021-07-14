import logging

from lib.comm.control import ProtoControlThread
from lib.core.command import TeamCommand

import time
import logging

TEST_ROBOT = 0
WAIT_TIME = 0.5

def main():
    team_command = TeamCommand()

    blue_control = ProtoControlThread(team_color_yellow=False, team_command=team_command, control_port=20013)

    team_command.commands[TEST_ROBOT].left_speed = -10
    team_command.commands[TEST_ROBOT].right_speed = 10

    logging.info("--- Starting ---\r\n")
    blue_control.start()

    time.sleep(WAIT_TIME)

    logging.info("--- Pause ---\r\n")
    blue_control.pause()

    time.sleep(WAIT_TIME)

    logging.info("--- Resume ---\r\n")
    blue_control.resume()

    time.sleep(WAIT_TIME)

    logging.info("--- Stoping ---\r\n")
    blue_control.stop()


if __name__ == '__main__':
    main()
