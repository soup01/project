from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from math import ceil

from lexicon.lexicon_ru import lexicon_ru

from callbacks.topic import TopicCallback
from callbacks.other_topic import OtherTopicCallback
from callbacks.navigation import NavigationCallback
from callbacks.back_to_topic_list import BackCallback

from config_data.config import load_config
import databases.topics_db as db

config = load_config()


def create_topic_choose_keyboard(page: int, topics: list[dict]) -> InlineKeyboardMarkup:
	topic_choose_keyboard = InlineKeyboardBuilder()
	buttons: list[InlineKeyboardButton] = []

	for topic in topics:
		id: int = topic["id"]
		buttons.append(InlineKeyboardButton(text=str(id),
											callback_data=TopicCallback(
												id=id
											).pack()))

	topic_choose_keyboard.row(*buttons, width=config.tg_bot.topics_amount_on_page)

	page_amount: int = ceil(len(db.find_all()) / config.tg_bot.topics_amount_on_page)

	topic_choose_keyboard.row(
		InlineKeyboardButton(text=lexicon_ru['backward'],
							 callback_data=NavigationCallback(
								 page=page,
								 direction='backward'
							 ).pack()),
		InlineKeyboardButton(
			text=lexicon_ru['page_indicator'](page, page_amount),
			callback_data='inactive'),
		InlineKeyboardButton(text=lexicon_ru['forward'],
							 callback_data=NavigationCallback(
								 page=page,
								 direction='forward'
							 ).pack()),
		width=3
	)

	topic_choose_keyboard.row(
		InlineKeyboardButton(text=lexicon_ru['describe'],
							 callback_data=OtherTopicCallback(
								 page=page
							 ).pack()))

	return topic_choose_keyboard.as_markup()


def create_back_button(page: int) -> InlineKeyboardMarkup:
	back_keyboard = InlineKeyboardMarkup(
		inline_keyboard=[
			[InlineKeyboardButton(text=lexicon_ru['back'], callback_data=BackCallback(
				page=page
			).pack())]
		]
	)
	return back_keyboard
