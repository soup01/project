from aiogram.filters.callback_data import CallbackData


class TopicCallback(CallbackData, prefix='problem'):
	id: int