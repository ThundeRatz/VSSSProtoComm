from lib.comm.referee import RefereeComm

import json
import logging


def main():
    referee = RefereeComm()

    try:
        while True:
            referee_data = referee.receive()
            print(json.dumps(referee_data, indent=4))

            # Acess test
            # print if referee_data dict not empty
            if referee_data:
                print(f"\r\nEstado do jogo: {referee_data['foul']}\r\n")
                print(f"\r\nTempo do jogo: {referee_data['gameHalf']}\r\n")
                print(f"\r\nTime: {referee_data['teamcolor']}\r\n")
            else:
                print("\r\nNo data received\r\n")
    except KeyboardInterrupt:
        logging.info("Ending")


if __name__ == '__main__':
    main()
