import telebot
import time
from telebot import types
import random
import numpy as np
#we get this token from @botFather and it connects to our tg bot thru it
TOKEN = '1514220011:AAHxAV-8kXUO3p2wu4NxTCBYKg8CwoH2EYE'

bot = telebot.TeleBot(token=TOKEN)
randnums = np.random.randint(1, 11, 10)


def find_at(msg):
    for text in msg:
        if '@' in text:
            return text

#method, which triggers the script after writing '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # creating users' keyboard
    markup_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Узнай см Сережи")
    item2 = types.KeyboardButton("Как он с этим живет?")
    markup_keyboard.add(item1, item2)
    # opening sticker
    sti = open('C:/RandomShit/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.reply_to(message, 'Добро пожаловать, {0.first_name}!\nЯ - {1.first_name}, подконтрольный тебе бот'
                 .format(message.from_user, bot.get_me()), parse_mode='markdown', reply_markup=markup_keyboard)

#creating random num
def random_number():
    rand_num = str(random.randint(0, 10))
    return rand_num


# rand_penis=str(random.randint(0,10))
#in this method we are filtering all incoming messages, and answering them
@bot.message_handler(content_types=['text'])
def replying_to_markup(message):
    rand_ = random_number()

    if message.chat.type == 'private':
        if message.text == 'Узнай см Сережи':

            bot.send_message(message.chat.id, randnums)
        elif message.text == 'Как он с этим живет?':
            #creating inline keyboard(bots' keyboard)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Пусть отвыкает', callback_data='good')
            item2 = types.InlineKeyboardButton('{} мало'.format(randnums[0]), callback_data='bad')
            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Он привык', reply_markup=markup)
        elif message.text != 'Узнай см Сережи' and message.text != 'Как он с этим живет' and '@' in message.text:
            @bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
            def at_answer(message):
                texts = message.text.split()
                at_text = find_at(texts)
                if at_text == '@':
                    pass
                else:
                    bot.reply_to(message.chat.id, 'https://instagram.com/{}'.format(at_text[1:]))
        #if we type smth wrong, triggers this part
        else:
            bot.send_message(message.chat.id, 'Не знаю что ответить')

#just a help section
@bot.message_handler(commands=['help'])
def send_welcome1(message):
    bot.reply_to(message, 'U will be connected with a helping services')

#so here we are analyzing the response from the inline button by callback_data
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, "Его надо сначала увидеть, чтобы отвыкнуть, не наш случай")
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=
                'Бля ну ты конечно и умный отвыкай говорит а какой')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, "Может быть {} и мало, но что поделаешь".format(randnums[0]))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=
                'Слушай, Сережа, не загоняйся, {} сантиметра не так уж и мало, главное ширина.... наверное'.format(
                    randnums[0]))
            # removes inline buttons after pressing
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Как он с этим живет?',
                                  reply_markup=None)


    except Exception as e:
        print(repr(e))

#just infinite loop
while 1:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
