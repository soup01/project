from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from math import ceil

from lexicon.lexicon_ru import lexicon_ru

from keyboards.topic_choose import create_topic_choose_keyboard, create_back_button

from callbacks.topic import TopicCallback
from callbacks.navigation import NavigationCallback
from callbacks.back_to_topic_list import BackCallback
from callbacks.other_topic import OtherTopicCallback

from databases import topics_db as db, db_tools

from states.other_topic_get import OtherTopicGet

from config_data.config import load_config

router = Router()
config = load_config()


@router.message(F.text == lexicon_ru['how_to_problem_solve'])
async def solve_problem(message: Message):
	page: int = 1
	problems: list[dict] = db_tools.find_all_by_page(page)
	await message.answer(text=lexicon_ru['problem_list'](problems),
						 reply_markup=create_topic_choose_keyboard(page, problems))


@router.callback_query(TopicCallback.filter())
async def get_solution(callback: CallbackQuery,
					   callback_data: TopicCallback):
	id: int = callback_data.id
	await callback.message.edit_text(text=db.find_by_id(id)['solution'],
									 reply_markup=create_back_button(
										 (id - 1) // config.tg_bot.topics_amount_on_page + 1
									 ))
	await callback.answer()


@router.callback_query(NavigationCallback.filter())
async def navigation(callback: CallbackQuery,
					 callback_data: NavigationCallback):
	page: int = callback_data.page
	direction: str = callback_data.direction

	if direction == 'backward' and page > 1 or direction == 'forward' and \
			page < ceil(len(db.find_all()) / config.tg_bot.topics_amount_on_page):
		if direction == 'backward':
			page -= 1
		if direction == 'forward':
			page += 1
		problems: list[dict] = db_tools.find_all_by_page(page)
		await callback.message.edit_text(text=lexicon_ru['problem_list'](problems),
										 reply_markup=create_topic_choose_keyboard(page, problems))

	await callback.answer()


@router.callback_query(BackCallback.filter())
async def back_to_topic_list(callback: CallbackQuery,
							   callback_data: TopicCallback,
							   state: FSMContext):
	page: int = callback_data.page
	problems: list[dict] = db_tools.find_all_by_page(page)
	await callback.message.edit_text(text=lexicon_ru['problem_list'](problems),
									 reply_markup=create_topic_choose_keyboard(page, problems))

	await state.clear()
	await callback.answer()


@router.callback_query(OtherTopicCallback.filter())
async def other_topic_getting(callback: CallbackQuery,
								callback_data: OtherTopicCallback,
								state: FSMContext):
	page: int = callback_data.page
	await state.set_state(OtherTopicGet.is_getting)
	await state.update_data(last_page=page)
	await callback.message.edit_text(text=lexicon_ru['describe_problem'],
									 reply_markup=create_back_button(page))
	await callback.answer()


@router.message(OtherTopicGet.is_getting)
async def other_topic_got(message: Message,
							state: FSMContext):
	data = await state.get_data()
	found_problem: dict | None = db_tools.find_by_topic_problem(message.text)

	if found_problem is not None:
		await message.answer(text=found_problem['solution'],
							 reply_markup=create_back_button(data['last_page']))
	else:
		await message.answer(text=lexicon_ru['unknown_problem'],
							 reply_markup=create_back_button(data['last_page']))
	await state.clear()
