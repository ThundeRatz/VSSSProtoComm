from lib.comm.vision import ProtoVisionThread
from lib.core.data import FieldData

import time
import logging

def main():
    test_field_data = FieldData()
    vision = ProtoVisionThread(team_color_yellow=False, field_data=test_field_data)

    vision.start()

    try:
        while True:
            print(test_field_data)
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Ending")


if __name__ == '__main__':
    main()
