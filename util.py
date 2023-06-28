from str import Str
import os, certifi, sys
import netifaces
from datetime import datetime
import locale



class Util:

    os.environ['SSL_CERT_FILE'] = certifi.where()
    
    @staticmethod
    def log(log_message):
        if Str.LOG_ENABLE:
            print(log_message)

    @staticmethod
    def get_ip_address(interface):
        try:
            addresses = netifaces.ifaddresses(interface)
            ip_info = addresses[netifaces.AF_INET][0]
            ip_address = ip_info['addr']
            return ip_address
        except KeyError:
            return None

    @staticmethod
    def get_today():
        locale.setlocale(locale.LC_TIME, 'tr_TR.utf8')

        today = datetime.today()
        formatted_date = today.strftime("%d %B %Y")
        day_of_week = today.strftime("%A")

        return "{0} {1}".format(formatted_date, day_of_week)
