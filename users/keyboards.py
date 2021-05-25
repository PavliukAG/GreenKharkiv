from telebot.types import ReplyKeyboardMarkup

from queries import Queries


class UserKeyboards:

	@staticmethod
	def get_choice_material_keyboard() -> ReplyKeyboardMarkup:

		keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

		for material in Queries.get_materials():

			keyboard.add(material)

		return keyboard

	@staticmethod
	def get_find_addresses_keyboard() -> ReplyKeyboardMarkup:

		keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

		keyboard.row("Знайти місце сортування або утилізації")
		keyboard.row("Обрати інший вид сировини")

		return keyboard

	@staticmethod
	def get_back_to_material_choice_keyboard() -> ReplyKeyboardMarkup:

		keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

		keyboard.row("Обрати інший вид сировини")

		return keyboard
