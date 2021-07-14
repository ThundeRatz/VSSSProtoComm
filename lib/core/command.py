class RobotCommand(object):
    def __init__(self, left_speed=0, right_speed=0):
        self.left_speed = left_speed
        self.right_speed = right_speed

    def __add__(self, other):
        sum_of_left = self.left_speed + other.left_speed
        sum_of_right = self.right_speed + other.right_speed
        return RobotCommand(sum_of_left, sum_of_right)

    def __sub__(self, other):
        sum_of_left = self.left_speed - other.left_speed
        sum_of_right = self.right_speed - other.right_speed
        return RobotCommand(sum_of_left, sum_of_right)

    def __mul__(self, multiplier):
        return RobotCommand(self.left_speed * multiplier, self.right_speed * multiplier)

    def __str__(self):
        msg = (
            f'LEFT SPEED: {self.left_speed}\n'
            f'RIGHT SPEED: {self.right_speed}\n'
        )
        return msg

    def __repr__(self):
        return f'RobotCommand({self})'


class TeamCommand(object):
    def __init__(self):
        self.commands = [RobotCommand() for i in range(3)]

    def reset(self):
        for cmd in self.commands:
            cmd.left_speed = 0
            cmd.right_speed = 0

    def __str__(self):
        msg = f'\nTEAM COMMAND:\n'
        for i in range(3):
            msg += f'ROBOT_{i}\n{self.commands[i]}'
        return msg

    def __repr__(self):
        return f'TeamCommand({self})'
