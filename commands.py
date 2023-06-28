from str import Str
from util import Util
from conf import Conf
from raspi import Raspi
import subprocess
import time

class Commands:

    @staticmethod
    def to_water(sec):
        MAX_WATERED_TIME = 60
        result = ""
        if sec < MAX_WATERED_TIME:
            Raspi.change_engine_state(True)
            time.sleep(sec)
            Raspi.change_engine_state(False)
            result = "Watered for {0} seconds.(~{1}ml)".format(sec, (12*sec))
            Conf.update_config(Str.STR_LAST_WATERED_DATE, Util.get_today())
            Conf.update_config(Str.STR_LAST_WATERED_ML, (12*sec))
        return  result

    @staticmethod
    def execute( command):
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                universal_newlines=True)
        return result.stdout

    @staticmethod
    def update(self):
        return ""
    
    @staticmethod
    def status():
        current_state = Raspi.read_sensor(Conf.read_config(Str.STR_CONF_PIN_MOISTURE))
        last_watered_date = Conf.read_config(Str.STR_LAST_WATERED_DATE)
        last_watered_ml = Conf.read_config(Str.STR_LAST_WATERED_ML)
        return "En son {0} tarihinde {1} ml sulama yapıldı.\n🍋: Toprağım {2}".format(last_watered_date, last_watered_ml, "Nemli" if current_state == 0 else "Kuru")

    @staticmethod
    def check_lemon():
        result = ""
        lemon_pin = Conf.read_config(Str.STR_CONF_PIN_MOISTURE)

        current_state = Raspi.read_sensor(lemon_pin)
        last_state = Conf.read_config(Str.STR_MOISTURE_LAST_STATE)

        Util.log("{0}:{1}={2}".format("check_lemon", "last_state", last_state))
        Util.log("{0}:{1}={2}".format("check_lemon", "current_state", current_state))
        if str(last_state) != str(current_state):
            Conf.update_config(Str.STR_MOISTURE_LAST_STATE, str(current_state))
            result = "🍋: Artık toprağım {0}".format("Nemli" if current_state == 0 else "Kuru")

        return result
