from config_data.config import load_config

config = load_config()

lexicon_ru: dict[str: str] = {
	'hello': lambda name: 'Здравствуйте, ' + name + '!',
	'page_indicator': lambda current_page, page_amount: str(current_page) + "/" + str(page_amount),
	'problem_list': lambda problems: problem_list(problems),

	'in_development': 'В разработке...',
	'describe_problem': 'Опишите свою проблему.',
	'unknown_problem': 'К сожалению, мы пока не знаем, как решить эту проблему.',
	'how_to_operator_contact': 'Как вы хотите связаться?',
	'operator_contact': 'Связаться с оператором',
	'emergency_situation': 'Экстренная ситуация',
	'choose_option': 'Выберите пункт меню...',
	'how_to_problem_solve': 'Что делать с неисправностью?',
	'back': '« Назад',
	'describe': 'Описать вручную',
	'backward': '«',
	'forward': '»',
	'telegram': 'Telegram',
	'mobile_communication': 'Мобильная связь'
}


def problem_list(problems):
	text = '<b>Найдите вашу проблему в списке и нажмите ниже на соответствующий ей номер.</b>\n\n'
	for problem in problems:
		text += f"<b>{str(problem['id'])}:</b> {problem['problem']} \n\n"
	return text
