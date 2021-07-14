import numpy as np

from lib.comm.replacer import ReplacerComm
from lib.comm.referee import RefereeComm
from lib.core import data

import time

def vectors_angle(vector1, vector2=np.array((1,0))):
    """Use numpy to calculate the angle of vector1 using vector2 as reference"""
    v1 = np.array((vector1))
    v2 = np.array((vector2))

    return np.arctan2(np.linalg.det([v2,v1]),np.dot(v1,v2))


def main():
    blue_replacer = ReplacerComm(team_color_yellow=False)
    referee = RefereeComm()

    robot_zero = data.EntityData()
    robot_zero.position.x = data.FIELD_LENGTH/4 - data.ROBOT_SIZE * 1.2
    robot_zero.position.y = - data.ROBOT_SIZE * 0.3

    ball_entrypoint = np.array([data.FIELD_LENGTH/2, data.GOAL_WIDTH/2 - data.BALL_RADIUS * 2.6])
    kick_angle = vectors_angle(ball_entrypoint - np.array([robot_zero.position.x, robot_zero.position.y])) * 180 / np.pi
    robot_zero.position.theta = kick_angle

    try:
        while True:
            game_state = referee.receive().get('foul', 'STOP')

            if game_state == 'PENALTY_KICK':
                blue_replacer.place_team([(robot_zero, 1)])
                break

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
