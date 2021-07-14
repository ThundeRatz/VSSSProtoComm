FIELD_WIDTH = 1.3
FIELD_LENGTH = 1.5

GOAL_WIDTH = 0.4
GOAL_DEPTH = 0.1

GOAL_AREA_WIDTH = 0.7
GOAL_AREA_DEPTH = 0.15

ROBOT_SIZE = 0.075
WHEEL_RADIUS = 0.025
BALL_RADIUS = 0.02135


class Pose2D:
    def __init__(self, x: float = 0, y: float = 0, theta: float = 0):
        self.x = x
        self.y = y
        self.theta = theta

    def __str__(self):
        return f'x: {self.x:.02f}  y: {self.y:.02f}  th: {self.theta:.02f}'

    def __repr__(self):
        return f'Pose2D({self})'


class EntityData:
    def __init__(self):
        self.position = Pose2D()
        self.velocity = Pose2D()

    def __str__(self):
        msg = (
            f'Position: {self.position}\n'
            f'Velocity: {self.velocity}\n'
        )
        return msg

    def __repr__(self):
        return f'EntityData({self})'


class FieldData:
    def __init__(self):
        self.robots = [EntityData() for i in range(3)]
        self.foes = [EntityData() for i in range(3)]
        self.ball = EntityData()

    def __str__(self):
        msg = f'BALL\n{self.ball}'
        for i in range(3):
            msg += f'\nROBOT_{i}\n{self.robots[i]}'
        for i in range(3):
            msg += f'\nFOE_{i}\n{self.foes[i]}'
        return msg

    def __repr__(self):
        return f'FieldData({self})'
