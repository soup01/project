from aiogram import Router, F
from aiogram.types import Message

from lexicon.lexicon_ru import lexicon_ru

from keyboards.operator_communication import operator_communication_keyboard

router = Router()


@router.message(F.text == lexicon_ru['operator_contact'])
async def operator_contact(message: Message):
	await message.answer(text=lexicon_ru['how_to_operator_contact'],
						 reply_markup=operator_communication_keyboard)
