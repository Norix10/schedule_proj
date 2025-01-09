# import telebot

# bot = telebot.TeleBot('7884812562:AAENmaKhdxDN3RoQrtsYykZnfdNtLL9kDlc')


# @bot.message_handler(commands=['start', 'main', 'new'])
# def main(message):
#     bot.send_message(message.chat.id, 'Привет')

# @bot.message_handler(commands=['help'])
# def information(message):
#     bot.send_message(message.chat.id, 'Helping')


# bot.polling(none_stop = True)

import requests
import telebot

API_URL = "http://127.0.0.1:8000/schedule/"

bot = telebot.TeleBot('7884812562:AAENmaKhdxDN3RoQrtsYykZnfdNtLL9kDlc')


@bot.message_handler(commands=['schedule'])
def get_schedule(message):
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            schedules = response.json()
            reply_message = "Розклад:\n"
            for item in schedules:
                reply_message += f"{item['day_of_week']} {item['time']} - {item['subject']} (teacher: {item['teacher']}) {item['room']}\n"
            bot.reply_to(message, reply_message)
        else:
            bot.reply_to(message, "Не вдалося отримати розклад.")
    except Exception as e:
        bot.reply_to(message, f"Помилка: {e}")

# Запуск бота
if __name__ == "__main__":
    print("Бот запущений...")
    bot.polling(none_stop=True)

