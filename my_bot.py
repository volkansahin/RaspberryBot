from str import Str
from util import Util
from tele import Tele
from conf import Conf
from commands import Commands

import time, select, sys

"""
@vinzo_pi_bot
"""
SEC_SLEEP = 5
DEFAULT_WATERED_TIME = 5
MAX_WATERED_TIME = 60

class Main:

    def __init__(self):
        self.flag_exit = False
        self.tele = Tele(self)
        self.send_my_ip()

    def send_my_ip(self):
        while True:
            wlan0_ip = Util.get_ip_address('wlan0')
            if wlan0_ip:
                self.tele.send_message(str(wlan0_ip))
                break
            else:
                time.sleep(SEC_SLEEP)
                # log("wlan0 IP adresi:", wlan0_ip)

    def handle_commands(self, message):
        result = ""
        if message == "/exit":
            self.flag_exit = True
        elif message == "/status":
            result = Commands.status()
        elif message.startswith("/exe"):
            result = Commands.execute(message[len("/exe"):])
        elif message.startswith("/update"):
            pass
        elif message.startswith("/water"):
            watered_sec = DEFAULT_WATERED_TIME
            if message[len("/water "):] and 0 < int(message[len("/water "):]) < MAX_WATERED_TIME:
                watered_sec = int(message[len("/water "):])
            result = Commands.to_water(watered_sec)
        else:
            print(message)

        if result:
            self.tele.send_message(result)


main = Main()


# Programı sonsuz döngüde tutma
while main.flag_exit is False:
    # konsol girislerini gelen mesaj olarak algılar
    ready, _, _ = select.select([sys.stdin], [], [], 0)
    if ready:
        user_input = sys.stdin.readline().rstrip('\n')
        if user_input == 'q':
            break
        else:
            Commands.handle_commands(user_input)

    main.tele.send_message(Commands.check_lemon())
    time.sleep(SEC_SLEEP)
    Util.log("-------------------")

