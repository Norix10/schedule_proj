import requests
import telebot
from telebot import types

API_URL = "http://127.0.0.1:8000/groups/"
SCHEDULE_API_URL = "http://127.0.0.1:8000/json/"
bot = telebot.TeleBot('7884812562:AAENmaKhdxDN3RoQrtsYykZnfdNtLL9kDlc')


@bot.message_handler(commands=['start'])
def get_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('Перейти на сайт')
    btn2 = types.KeyboardButton('Показати розклад')
    btn3 = types.KeyboardButton('Редагувати розклад')
    markup.add(btn1)
    markup.add(btn2, btn3)

    bot.send_message(message.chat.id, "Оберіть дію:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Показати розклад')
def choose_group(message):
    inline_markup = types.InlineKeyboardMarkup(row_width=2)

    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            groups = response.json()
            if groups:
                for group in groups:
                    inline_markup.add(
                        types.InlineKeyboardButton(group['group_name'], callback_data=f"group_{group['group_name']}"))
                bot.send_message(message.chat.id, "Оберіть групу для перегляду розкладу:", reply_markup=inline_markup)
            else:
                bot.send_message(message.chat.id, "Немає доступних груп.")
        else:
            bot.send_message(message.chat.id, "Не вдалося отримати список груп.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Помилка: {e}")


@bot.callback_query_handler(func=lambda call: call.data.startswith('group_'))
def choose_day(call):
    group_name = call.data.split('_')[1]
    inline_markup = types.InlineKeyboardMarkup(row_width=2)

    days = [
        ("Понеділок", "Monday"),
        ("Вівторок", "Tuesday"),
        ("Середа", "Wednesday"),
        ("Четвер", "Thursday"),
        ("П’ятниця", "Friday"),
        ("Субота", "Saturday"),
    ]

    for day_name, day_code in days:
        inline_markup.add(types.InlineKeyboardButton(day_name, callback_data=f"{group_name}_{day_code}"))

    bot.send_message(call.message.chat.id, f"Оберіть день тижня для групи {group_name}:", reply_markup=inline_markup)


@bot.callback_query_handler(func=lambda call: True)
def show_schedule_for_day(call):
    group_name, day_code = call.data.split('_')

    try:
        response = requests.get(f"{SCHEDULE_API_URL}?group_name={group_name}&day={day_code}")
        if response.status_code == 200:
            schedules = response.json()
            if schedules:
                reply_message = f"Розклад для групи {group_name} на {day_code}:\n\n"
                for item in schedules:
                    reply_message += (
                        f"{item['time']} - {item['subject']} {item['room_s']}\n"
                        f"{item['full_name']}\n\n"
                    )
            else:
                reply_message = f"На {day_code} для групи {group_name} немає розкладу."
            bot.send_message(call.message.chat.id, reply_message)
        else:
            bot.send_message(call.message.chat.id, "Не вдалося отримати розклад.")
    except Exception as e:
        bot.send_message(call.message.chat.id, f"Помилка: {e}")


# Редагування розкладу (поки що без реалізації)
@bot.message_handler(func=lambda message: message.text == 'Редагувати розклад')
def edit_schedule(message):
    bot.send_message(message.chat.id, "Функція редагування розкладу ще не реалізована.")


if __name__ == "__main__":
    print("Бот запущений...")
    bot.polling(none_stop=True)
