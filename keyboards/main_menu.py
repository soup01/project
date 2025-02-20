from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon.lexicon_ru import lexicon_ru

main_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
	[KeyboardButton(text=lexicon_ru['how_to_problem_solve'])],
	[KeyboardButton(text=lexicon_ru['emergency_situation']), KeyboardButton(text=lexicon_ru['operator_contact'])]
],
	resize_keyboard=True,
	input_field_placeholder=lexicon_ru['choose_option'])
