from aiogram.types import CopyTextButton, InlineKeyboardMarkup, InlineKeyboardButton

from lexicon.lexicon_ru import lexicon_ru


operator_communication_keyboard = InlineKeyboardMarkup(inline_keyboard=[
	[InlineKeyboardButton(text=lexicon_ru['telegram'], url='https://t.me/u7l34b8')], # это временно
	[InlineKeyboardButton(text=lexicon_ru['mobile_communication'],
						  copy_text=CopyTextButton(text='+79297004240'))] # это временно
])
