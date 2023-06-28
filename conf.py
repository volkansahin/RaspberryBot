from str import Str
from util import Util
import configparser

class Conf:

    @staticmethod
    def read_config(attr, section="Bot"):
        fetched_value = ""
        try:
            Util.log("{0}:{1}={2}".format("read_config", "ATTR", attr))
            config = configparser.ConfigParser()
            config.read(Str.CONFIG_FILE)
            if section in config:
                fetched_value = config[section].get(str(attr))
                Util.log("{0}:{1}={2}".format("read_config", "VALUE", fetched_value))
                # f"Value of {attr}: {fetched_value}"
            else:
                Util.log("Section bulunamadi ama eklendi")
                config.add_section(section)

        except FileNotFoundError:
            with open(Str.CONFIG_FILE, 'w') as f:
                f.write("Bu dosya oluşturuldu.")
        except Exception as e:
            Util.log("ERRRR {0}".format(str(e)))

        return fetched_value

    @staticmethod
    def write_config(attr, value, section="Bot"):
        config = configparser.ConfigParser()
        config.add_section(section)
        config.set(section, attr, str(value))

        with open(Str.CONFIG_FILE, 'w') as file:
            config.write(file)

    @staticmethod
    def update_config(attr, value, section="Bot"):
        try:
            config = configparser.ConfigParser()
            config.read(Str.CONFIG_FILE)

            if not config.has_section(section):
                config.add_section(section)

            config.set(str(section), str(attr), str(value))

            # Değişiklikleri kaydet
            with open(Str.CONFIG_FILE, 'w') as file:
                config.write(file)
        except Exception as e:
            Util.log("{0}:{1}={2}".format("update_config", "Error Message", str(e)))