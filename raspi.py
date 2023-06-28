from str import Str
from util import Util
from conf import Conf
import RPi.GPIO as GPIO

class Raspi:

    def read_sensor(sensor_pin):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        #Util.log("{0}:{1}={2}".format("read_sensor", "sensor_pin", sensor_pin))
        GPIO.setup(int(sensor_pin), GPIO.IN)
        current_state = GPIO.input(int(sensor_pin))
        GPIO.cleanup()

        return current_state

    def change_engine_state(state):
        power_pin = int(Conf.read_config(Str.STR_CONF_PIN_PUMP))
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(power_pin, GPIO.OUT)
        GPIO.output(power_pin, True)  # OFF

        if state is True:
            GPIO.output(power_pin, False)
        else:
            GPIO.output(power_pin, True)

    