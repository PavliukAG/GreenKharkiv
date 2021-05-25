from typing import Callable, List, Dict

from telebot import TeleBot
from telebot.types import Message

from queries import Queries
from users.keyboards import UserKeyboards


class UserManager:


	def __init__(self):

		self.states: Dict[int, str] = {}

	def set_material_state(self, user_id: int, material: str):

		self.states.update({user_id: material})

	def get_material_state(self, user_id: int) -> str:

		return self.states.get(user_id)

	def del_material_state(self, user_id: int):

		self.states.pop(user_id, None)


class UserHandlers:

	def __init__(self, bot: TeleBot):

		self.bot = bot

		self.manager = UserManager()

	def set_handlers(self):

		self.bot.message_handler(commands=["start"])(self.start_handler)

		for material in Queries.get_materials():

			self.register_material_handler(material)

		self.register_text_handler("Знайти місце сортування або утилізації", self.addresses_handler)

		self.register_text_handler("Обрати інший вид сировини", self.choice_material_handler)

	def register_text_handler(self, text: str, handler: Callable[[Message], None]):

		self.bot.message_handler(content_types=["text"], func=lambda msg: msg.text == text)(handler)

	def register_material_handler(self, material: str):
		"""Register handler for some type of materials. Executes after choice_material_handler."""

		@self.bot.message_handler(content_types=["text"], func=lambda msg: msg.text == material)
		def material_handler(message: Message):

			self.bot.send_message(message.chat.id, Queries.get_material_advice(material))

			self.bot.send_message(
				message.chat.id,
				"Будемо шукати де сортувати?",
				reply_markup=UserKeyboards.get_find_addresses_keyboard()
			)

			self.manager.set_material_state(message.from_user.id, material)

	def start_handler(self, message: Message):

		self.bot.send_message(
			message.chat.id,
			"Привіт! Мене звати бот Green Kharkiv. Я створений, щоб домогти тобі з сортуванням."
		)

		self.choice_material_handler(message)

		Queries.create_user(message.from_user.id, message.from_user.username)

	def choice_material_handler(self, message: Message):

		self.manager.del_material_state(message.from_user.id)

		self.bot.send_message(
			message.chat.id,
			"Обери який вид сировини потрібно відсортувати або утилізувати.",
			reply_markup=UserKeyboards.get_choice_material_keyboard()
		)

	def addresses_handler(self, message: Message):

		material: str = self.manager.get_material_state(message.from_user.id)

		addresses: List[str] = Queries.get_addresses(material)

		self.bot.send_message(
			message.chat.id,
			"\n\n".join(addresses),
			reply_markup=UserKeyboards.get_back_to_material_choice_keyboard()
		)
