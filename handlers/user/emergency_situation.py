from aiogram import Router, F
from aiogram.types import Message

from lexicon.lexicon_ru import lexicon_ru

router = Router()


@router.message(F.text == lexicon_ru['emergency_situation'])
async def emergency_situation(message: Message):
	await message.answer(text=lexicon_ru['in_development'])
