
from telebot import TeleBot
from config import BOT_TOKEN
from users.handlers import UserHandlers
from admins.handlers import AdminHandlers

if __name__ == '__main__':

	bot: TeleBot = TeleBot(BOT_TOKEN, parse_mode="HTML")

	# ignore messages from chats.
	bot.message_handler(content_types=["text"], func=lambda msg: msg.chat.id != msg.from_user.id)(lambda msg: 0)

	UserHandlers(bot).set_handlers()

	AdminHandlers(bot).set_handlers()

	bot.message_handler(content_types=["text"])(
		lambda msg: bot.send_message(msg.chat.id, "Я створений лише для допомоги з сортуванням")
	)

	while True:
		try:
			bot.polling(none_stop=False, interval=1, timeout=400000)
		except Exception as exc:
			pass
