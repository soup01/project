import databases.topics_db as db

from config_data.config import load_config

config = load_config()


def find_all_by_page(page: int) -> list[dict]:
	res: list[dict] = []
	width: int = config.tg_bot.topics_amount_on_page
	for el in db.find_all():
		if width * (page - 1) < el['id'] <= width * page:
			res.append(el)
	return res


def compare(problem1: str, problem2: str) -> bool:
	return problem1.lower() == problem2.lower()


def find_by_topic_problem(problem: str) -> dict:
	for topic in db.find_all():
		if compare(topic['problem'], problem):
			return topic