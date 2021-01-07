import telebot
import time

TOKEN = '1514220011:AAHxAV-8kXUO3p2wu4NxTCBYKg8CwoH2EYE'

bot = telebot.TeleBot(token=TOKEN)
def find_at(msg):
    for text in msg:
        if '@' in text:
            return text


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'hi')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'U will be connected with a helping services')

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def at_answer(message):
    texts= message.text.split()
    at_text= find_at(texts)
    if at_text =='@':
        pass
    else:

        bot.reply_to(message, 'https://instagram.com/{}'.format(at_text[1:]))
logger = telebot.logger
formatter = logging.Formatter('[%(asctime)s] %(thread)d {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
                                  '%m-%d %H:%M:%S')
ch = logging.StreamHandler(sys.stdout)
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)  # or use logging.INFO
ch.setFormatter(formatter)


while 1:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)