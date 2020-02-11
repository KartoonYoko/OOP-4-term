import datetime

class Bot:
	""" Класс чат-бот.
		Умеет овечать на
			реплики-шаблолны:
				- Привет, бот!
				-
				-
				-
				-
			простые команды:
				- Который час?
				-
				-
			команды с параметрами:
				- умножь 12 на 157
				- 
				-
		Умеет хранить историю сообщений, записывая историю в файл по завершению программы.
		И загружать из файла при запуске.

		Получение актуальной информации из интернета.
	"""


	def __init__(self, userName = "user"):
		self._userName = userName


	def reply(self, s):
		if isinstance(s, str):
			s = s.lower()
			if "привет, бот" in s:
				return str("Привет, " + self._userName)
			elif "который час?" in s:
				now = datetime.datetime.now()			# 
				return now.strftime("%d-%m-%Y %H:%M")	# Вернет текущую дату и время
			elif "умножь" in s:
				buf = s.find("на", s.find("умножь"))
				if buf != -1:
					s1 = s[s.find("умножь") + 1: buf - 1]
					s2 = s[buf + 1: s.find(" ", buf + 1) - 1]
					try:
						answer = s1 * s2
					except ValueError as e:
						return "Неверный формат"
					return str(answer)
			else:
				return "Я Вас не понял, не могли бы повторить?"