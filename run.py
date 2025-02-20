import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config_data.config import load_config
from handlers.user import operator_contact, other, emergency_situation, solve_problem, start

logger = logging.getLogger(__name__)


async def main() -> None:
	logging.basicConfig(level=logging.INFO)
	logger.info('Starting...')

	config = load_config()
	bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

	dp = Dispatcher()

	dp.include_routers(start.router,
					   emergency_situation.router,
					   operator_contact.router,
					   solve_problem.router,
					   other.router)

	await dp.start_polling(bot)


asyncio.run(main())

if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)
	asyncio.run(main())
