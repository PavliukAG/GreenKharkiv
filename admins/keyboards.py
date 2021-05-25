
from telebot.types import ReplyKeyboardMarkup

from queries import Queries


class AdminKeyboards:

	@staticmethod
	def get_keyboard(*args) -> ReplyKeyboardMarkup:

		keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)

		for arg in args:

			keyboard.add(arg)

		return keyboard

	@staticmethod
	def get_confirm_keyboard() -> ReplyKeyboardMarkup:

		return AdminKeyboards.get_keyboard("Так, все вірно!", "Ні, спробую ще раз.")

	@staticmethod
	def get_choice_materials_keyboard() -> ReplyKeyboardMarkup:

		return AdminKeyboards.get_keyboard(*Queries.get_materials())

	@staticmethod
	def get_materials_confirm_keyboard() -> ReplyKeyboardMarkup:

		return AdminKeyboards.get_keyboard("Так", "Ні")

