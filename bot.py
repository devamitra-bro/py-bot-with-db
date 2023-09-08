import telebot
import db.db_service

telebot.apihelper.ENABLE_MIDDLEWARE = True
creds = ''
with open('/etc/am/am_test_bot.txt') as f:   # file contains just string like: 1234567890:Bujhb&6IytvkGCyi6YtcHJGV
	creds = f.readline().replace('\n', '')
bot = telebot.TeleBot(creds)

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.from_user.id, " Дратути")

@bot.message_handler(func=lambda message: True)
def get_text_messages(message):
	request=message.text
	# TODO
	bot.send_message(message.from_user.id, "todo")
	print("Запрос:", request, " \nОтвет :", "todo")

bot.infinity_polling(none_stop=True, interval=1)

