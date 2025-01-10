import requests
import telebot
from telebot import types

API_URL = "http://127.0.0.1:8000/schedule/"

bot = telebot.TeleBot('7884812562:AAENmaKhdxDN3RoQrtsYykZnfdNtLL9kDlc')


#@bot.message_handler(commands=['schedule'])
#def get_schedule(message):
#    try:
#        response = requests.get(API_URL)
#        if response.status_code == 200:
#            schedules = response.json()
#            reply_message = "Розклад:\n"
#            for item in schedules:
#                reply_message += (f"{item['day_of_week']} "
#                                  f"{item['time']} - {item['subject']} {item['room_s']}\n"
#                                  f"{item['full_name']}")
#            bot.reply_to(message, reply_message)
#        else:
#            bot.reply_to(message, "Не вдалося отримати розклад.")
#    except Exception as e:
#        bot.reply_to(message, f"Помилка: {e}")

@bot.message_handler(commands=['start'])
def get_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('Перейти на сайт')
    btn2 = types.KeyboardButton('Показати розклад')
    btn3 = types.KeyboardButton('Редагувати розклад')
    markup.add(btn1)
    markup.add(btn2, btn3)

    bot.send_message(message.chat.id, "Оберіть дію:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Перейти на сайт')
def send_inline_button(message):
    inline_markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton('Перейти на сайт', url="http://127.0.0.1:8000/")
    inline_markup.add(btn)
    bot.send_message(message.chat.id, "Натисніть кнопку нижче, щоб перейти на сайт:", reply_markup=inline_markup)



@bot.message_handler(func=lambda message: message.text == 'Показати розклад')
def get_schedule(message):
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            schedules = response.json()
            reply_message = "Розклад:\n\n"
            for item in schedules:
                reply_message += (f"{item['day_of_week']} "
                                  f"{item['time']} - {item['subject']} {item['room_s']}\n"
                                  f"{item['full_name']}\n\n")
            bot.reply_to(message, reply_message)
        else:
            bot.reply_to(message, "Не вдалося отримати розклад.")
    except Exception as e:
        bot.reply_to(message, f"Помилка: {e}")


@bot.message_handler(func=lambda message: message.text == 'Редагувати розклад')
def edit_schedule(message):
    bot.send_message(message.chat.id, "Функція редагування розкладу ще не реалізована.")

if __name__ == "__main__":
    print("Бот запущений...")
    bot.polling(none_stop=True)

