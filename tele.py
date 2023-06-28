from str import Str
from util import Util
from conf import Conf
from commands import Commands

import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton


class Tele:
    def __init__(self,main):
        self.main = main
        self.bot = telepot.Bot(Conf.read_config(Str.STR_CONF_BOT_TOKEN))
        MessageLoop(self.bot, self.handle_message).run_as_thread()
        

    def send_message(self, message):
        conf_chat_id = Conf.read_config(Str.STR_CONF_CHAT_ID)
        Util.log("{0}:{1}={2}".format("send_message", "message", message))
        if conf_chat_id and self.bot and message:
            self.bot.sendMessage(conf_chat_id, message)
        else:
            Util.log(" chat_id = {0}, bot veya message'i {1} kontrol et".format(conf_chat_id, message))

    def handle_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        Util.log("{0}:{1}={2}".format("handle_message", "chat_id", chat_id))
        # log("content type: {0} chat type: {1} chat id:{2}".format(content_type, chat_type, chat_id))
        conf_chat_id = Conf.read_config(Str.STR_CONF_CHAT_ID)
        if not conf_chat_id:
            Conf.write_config(Str.STR_CONF_CHAT_ID, str(chat_id))

        if str(conf_chat_id) == str(chat_id):
            if content_type == 'text':
                message = msg['text']
                # TODO mesaj parse edilip ilgili mesaj döndürülür
                Util.log("{0}:{1}={2}".format("handle_message", "message", message))
                self.main.handle_commands(message)

    """
    def send_buttons():
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Button 1', callback_data='button1')],
            [InlineKeyboardButton(text='Button 2', callback_data='button2')]
        ])
        bot.sendMessage(chat_id, 'Merhaba, aşağıdaki düğmelere tıklayabilirsiniz:', reply_markup=keyboard)
        pass
    def handle_callback(msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

        if query_data == 'button1':
            bot.answerCallbackQuery(query_id, text='Button 1 tıklandı!')
        elif query_data == 'button2':
            bot.answerCallbackQuery(query_id, text='Button 2 tıklandı!')
    """