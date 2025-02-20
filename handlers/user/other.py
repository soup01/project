from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data == 'inactive')
async def inactive(callback: CallbackQuery):
	await callback.answer()
