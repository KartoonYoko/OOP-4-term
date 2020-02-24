from bot import Bot


# user = input("Консоль для работы с чат-ботом. Ввведите ваше имя.")
user = "asdasd"
alex = Bot(user)
# x = input("Теперь можете написать ему что-нибудь.")
# print(alex.get_history_of_chatting())
# while x != "q":
# 	print(alex.reply(x))
# 	x = input("Для завершения введите \"q\".")
print(alex.find_out_weather())
