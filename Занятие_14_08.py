#9#
import datetime
#import random
# def process_list(lst):
#     if isinstance(lst, list):
#
#         new_lst = []
#
#         for i in lst:
#             if i % 2 == 0:
#                 new_lst.append(i**2)
#             else:
#                 new_lst.append(i**3)
#         return new_lst
#     else:
#         print("Ошибка: аргумент не является списком")
#
# process_list("ghghg")
#
# #10#
# options = ["камень", "ножницы", "бумага"]
#
# while True:
#     choice = input("Выберите: камень/ножницы/бумага/выход: ")
#     comp_choice = random.choice(options)
#     if choice == "выход":
#         print("Игра завершена")
#         break
#
#     elif choice not in options:
#         print("Ошибка. Некорректный ввод данных")
#         continue
#
#     print("Компьютер выбрал", comp_choice)
#     if choice == comp_choice:
#         print("Ничья")
#     win = {"камень":"ножницы", "ножницы":"бумага", "бумага":"камень"}
#     print(win[choice])
#     if win[choice] == comp_choice:
#         print("Ура! Вы победили!")
#     else:
#         print("Вы проиграли")
#     # if choice == "камень":
#     #     if comp_choice == "ножницы":
#     #         print("Ура, Вы победили")
#     #     elif comp_choice == "бумага":
#     #         print("Вы проиграли")
#     # if choice == "ножницы":
#     #     if comp_choice == "бумага":
#     #         print("Ура, Вы победили")
#     #     elif comp_choice == "камень":
#     #         print("Вы проиграли")
#     # if choice == "бумага":
#     #     if comp_choice == "камень":
#     #         print("Ура, Вы победили")
#     #     elif comp_choice == "ножницы":
#     #         print("Вы проиграли")
#12#
# try:
#     birthday = input("Введите дату рождения в формате DD.MM.YYYY: ")
#     # year = int(birthday.split(".")[2])
#     # month = int(birthday.split(".")[1])
#     # day = int(birthday.split(".")[0])
#     today = datetime.date.today()
#     birthday = datetime.datetime.strptime(birthday, "%d.%m.%Y")
#     age = today.year - birthday.year
#     if today.month < birthday.month:
#         age -= 1
#     remains = age % 10
#     if remains == 1:
#         print(f"Вам {age} год")
#     elif remains == 2 or remains == 3 or remains == 4:
#         print(f"Вам {age} года")
#     else:
#         print(f"Вам {age} лет")
#
# except ValueError:
#     print("Ошибка ввода даты")
#13#
# user = {
#     "name": "Anna",
#     "age": 20,
#     "city": "Moscow",
#     "email": "fsebf@mail.ru"
# }
# print(f"Имя: {user["name"]}, возраст: {user["age"]}")
# user.update({"city": "New York"})
# user.update({"job": "teacher"})
# user.pop("age")
# if "email" in user:
#     print(f"email: {user["email"]}")
# else:
#     print("Ключ отсутствует")
#
# for k, v in user.items():
#     print(f"{k}: {v}")
#14#
text = "Осень в Москве, Зима в Москве, Весна в Москве, Лето в Москве. Времена года!"
counts = {}
text_lst = text.replace("!", "").replace(",", "").replace(".", "").split()

for word in text_lst:
    if word in counts:
        counts[word] += 1
        #print(counts)
    else:
        counts[word] = 1
        #print(counts)
for k, v in counts.items():
    print(f"{k}: {v}")


