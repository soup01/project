from aiogram.filters.callback_data import CallbackData


class NavigationCallback(CallbackData, prefix='navigation'):
	page: int
	direction: str