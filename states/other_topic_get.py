from aiogram.fsm.state import StatesGroup, State


class OtherTopicGet(StatesGroup):
	is_getting = State()
	last_page = State()