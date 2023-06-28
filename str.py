import os
class Str:

    CONFIG_FILE = r'' + os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
    STR_CONF_CHAT_ID = "chat_id"
    STR_CONF_BOT_TOKEN = "bot_token"
    STR_CONF_PIN_MOISTURE = "pin_soil_moisture"
    STR_CONF_PIN_PUMP = "pin_water_pump"
    STR_MOISTURE_LAST_STATE = "last_state_moisture"
    STR_LAST_WATERED_DATE = "last_watered_date"
    STR_LAST_WATERED_ML = "last_watered_ml"
    LOG_ENABLE = False