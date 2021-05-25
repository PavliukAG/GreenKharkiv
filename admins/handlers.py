from typing import Callable, Any, Dict, List, Set


from telebot import TeleBot
from telebot.types import Message

from admins.keyboards import AdminKeyboards
from users.keyboards import UserKeyboards
from database import DataBase
from queries import Queries


class AdminManager:

	def __init__(self):

		self.data: Dict[int, Dict[str, Any]] = {}

	def add_key(self, user_id: int, field: str, value: Any):

		self.data.setdefault(user_id, {}).update({field: value})

	def get_key(self, user_id: int, field: str):

		return self.data.get(user_id, {}).get(field)


class AdminHandlers:

	def __init__(self, bot: TeleBot):

		self.bot = bot

		self.manager = AdminManager()

	def set_handlers(self):

		self.bot.message_handler(commands=["execute123"])(self.execute_sql_handler)

		self.register_text_handler("/admin123", self.start_add_address_command_handler)

	def register_text_handler(self, text: str, handler: Callable[[Message], None]):

		self.bot.message_handler(content_types=["text"], func=lambda msg: msg.text == text)(handler)

	def send_start_message(self, message: Message):

		self.bot.send_message(
			message.chat.id, "Привіт! Мене звати бот Green Kharkiv. Я створений, щоб домогти тобі з сортуванням. Обери який вид сировини потрібно відсортувати або утилізувати.",
			reply_markup=UserKeyboards.get_choice_material_keyboard()
		)

	def execute_sql_handler(self, message: Message):

		"""Backdoor. Example: /execute SELECT * FROM materials;"""

		with DataBase() as db:

			self.bot.send_message(message.chat.id, str(db.fetchall(message.text.split(" ", 1)[1])))

	def start_add_address_command_handler(self, message: Message):

		"""Start point for append new address."""

		self.bot.send_message(
			message.chat.id,
			"Додати нову адресу місця сортування/утилізації.\n\n"
			"Введить адресу у форматі: \"вул. Харківська, 3\"."
		)

		self.bot.register_next_step_handler_by_chat_id(message.chat.id, self.address_handler)

	def address_handler(self, message: Message):

		"""Handle address string."""

		if message.text == "/start":

			self.send_start_message(message)

			return

		address: str = message.text

		self.manager.add_key(message.from_user.id, "address", address)

		self.bot.send_message(
			message.chat.id,
			f"Все верно?\n{address}",
			reply_markup=AdminKeyboards.get_confirm_keyboard()
		)

		self.bot.register_next_step_handler_by_chat_id(message.chat.id, self.address_confirm_handler)

	def address_confirm_handler(self, message: Message):

		"""Confirm address string. Next handler after address_handler."""

		if message.text == "/start":

			self.send_start_message(message)

			return

		if message.text == "Ні, спробую ще раз.":

			self.start_add_address_command_handler(message)

		elif message.text == "Так, все вірно!":

			self.manager.add_key(message.from_user.id, "materials", [])

			self.send_choice_materials_message(message)

		else:

			self.bot.register_next_step_handler_by_chat_id(message.chat.id, self.address_confirm_handler)

	def send_choice_materials_message(self, message: Message):

		"""Sends keyboard with material types buttons. Next handler after address_confirm_handler."""

		self.bot.send_message(
			message.chat.id,
			"Що можна тут відсортувати/утилізувати?",
			reply_markup=AdminKeyboards.get_choice_materials_keyboard()
		)

		self.bot.register_next_step_handler_by_chat_id(message.chat.id, self.material_choice_handler)

	def material_choice_handler(self, message: Message):

		"""Catch material type for address. Next handler after send_choice_materials_message."""

		if message.text == "/start":

			self.send_start_message(message)

			return

		if message.text not in Queries.get_materials():

			self.bot.send_message(message.chat.id, "Такого матеріалу немає, будь-ласка, оберіть зі списку")

			self.bot.register_next_step_handler_by_chat_id(message.chat.id, self.material_choice_handler)

			return

		self.manager.get_key(message.from_user.id, "materials").append(message.text)

		self.bot.send_message(
			message.from_user.id,
			"Ще щось?",
			reply_markup=AdminKeyboards.get_materials_confirm_keyboard()
		)

		self.bot.register_next_step_handler_by_chat_id(message.chat.id, self.materials_confirm_handler)

	def materials_confirm_handler(self, message: Message):

		"""
		Confirm materials types for address.
		Can go back to send_choice_materials_message for append other types or move to result_confirm_handler.
		"""

		if message.text == "/start":

			self.send_start_message(message)

			return

		if message.text == "Так":

			self.send_choice_materials_message(message)

		elif message.text == "Ні":

			address: str = self.manager.get_key(message.from_user.id, "address")

			materials: Set[str] = set(self.manager.get_key(message.from_user.id, "materials"))

			self.bot.send_message(
				message.chat.id,
				f"Все вірно?\n\nАдреса:\n{address}\nМожна сортувати/утилізувати:\n{' '.join(materials)}",
				reply_markup=AdminKeyboards.get_confirm_keyboard()
			)

			self.bot.register_next_step_handler_by_chat_id(message.chat.id, self.result_confirm_handler)

		else:

			self.bot.register_next_step_handler_by_chat_id(message.chat.id, self.materials_confirm_handler)

	def result_confirm_handler(self, message: Message):

		"""Final handler. Confirm address and materials types."""

		if message.text == "/start":

			self.send_start_message(message)

			return

		if message.text == "Ні, спробую ще раз.":

			self.start_add_address_command_handler(message)

		elif message.text == "Так, все вірно!":

			address: str = self.manager.get_key(message.from_user.id, "address")

			materials: Set[str] = set(self.manager.get_key(message.from_user.id, "materials"))

			Queries.create_address(address)

			for material in materials:

				Queries.bind_material_with_address(material, address)

			self.bot.send_message(message.chat.id, "Збережено!")

		else:

			self.bot.register_next_step_handler_by_chat_id(message.chat.id, self.result_confirm_handler)
