from lib.comm.vision import ProtoVision

import json
import logging

def main():
    vision = ProtoVision(team_color_yellow=False)

    try:
        counter = 0

        while True:
            vision_data = vision.receive_dict()

            vision_dict = json.dumps(vision_data, indent=4)

            if vision_dict:
                counter += 1

            print(vision_dict)
    except KeyboardInterrupt:
        logging.info("Ending")


if __name__ == '__main__':
    main()
