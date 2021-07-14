from lib.comm.control import ProtoControl

import time


def main():
    yellow_control = ProtoControl(team_color_yellow=True, control_ip="127.0.0.1", control_port=20012)
    blue_control = ProtoControl(team_color_yellow=False, control_ip="127.0.0.1", control_port=20013)

    current_time = time.time()

    while (time.time() - current_time < 5):
        blue_control.transmit_robot(0, -10, 10)
        yellow_control.transmit_robot(0, 10, -10)

    current_time = time.time()

    while (time.time() - current_time < 5):
        blue_control.transmit_robot(1, 10, 10)
        yellow_control.transmit_robot(1, 5, 5)

    current_time = time.time()

    while (time.time() - current_time < 5):
        blue_control.transmit_robot(2, -5, -5)
        yellow_control.transmit_robot(2, -15, -15)

    [blue_control.transmit_robot(i, 0, 0) for i in range(3)]
    [yellow_control.transmit_robot(i, 0, 0) for i in range(3)]


if __name__ == '__main__':
    main()
