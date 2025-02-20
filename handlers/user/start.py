from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from lexicon.lexicon_ru import lexicon_ru

from keyboards.main_menu import main_menu_keyboard

router = Router()


@router.message(CommandStart())
async def start(message: Message):
	await message.answer(text=lexicon_ru['hello'](message.from_user.first_name),
						 reply_markup=main_menu_keyboard)