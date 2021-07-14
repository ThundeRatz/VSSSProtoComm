from lib.comm.vision import ProtoVision
from lib.core.data import FieldData

import json


def main():
    test_field_data = FieldData()
    vision = ProtoVision(team_color_yellow=False, field_data=test_field_data)

    print(test_field_data)
    vision.update()
    print(test_field_data)


if __name__ == '__main__':
    main()
