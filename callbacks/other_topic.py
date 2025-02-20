from aiogram.filters.callback_data import CallbackData


class OtherTopicCallback(CallbackData, prefix='other_problem'):
	page: int