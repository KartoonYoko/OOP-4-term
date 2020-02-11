from bot import Bot

user = input("Консоль для работы с чат-ботом. Ввведите ваше имя.")
alex = Bot(user)
x = input("Теперь можете написать ему что-нибудь.")
while x != "Yes":
	print(alex.reply(x))
	x = input("Для завершения введите Yes.")