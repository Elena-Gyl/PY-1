import tkinter as tk

# warehouse = {
# "laptop": {"price": 80000, "quantity": 5},
# "mouse": {"price": 1500, "quantity": 20},
# "keyboard": {"price": 4000, "quantity": 10}
# }
#
# while True:
#     print(f"\n")
#     print(f"1 — Показать товары.")
#     print(f"2 — Добавить товар.")
#     print(f"3 — Продать товар")
#     print(f"4 — Пополнить остаток")
#     print(f"5 — Изменить цену")
#     print(f"6 — Общая стоимость склада")
#     print(f"7 — Самый дорогой товар")
#     print(f"8 — Товары с остатком меньше 3")
#     print(f"0 — Выход")
#
#     choice = input("Выберите действие: ")
#     if choice == "1": #1 — Показать товары
#         for name, product in warehouse.items():
#             print(f" Товар:{name} Цена: {product['price']} руб Остаток: {product['quantity']}")
#
#     elif choice == "2": # 2 — Добавить товар
#         name = input("Введите товар :")
#         if name in warehouse:
#             print("Товар есть в списке!")
#         else:
#             price = int(input("Введите цену :"))
#             quantity = int(input("Введите количество :"))
#             warehouse[name]= {"price": price, "quantity": quantity}
#             print("Товар добавлен!")
#
#     elif choice == "3": # 3 — Продать товар
#         name = input("Введите товар :")
#         if name not in warehouse:
#             print("Товара нет в списке!")
#         else:
#             quantity = int(input("Введите количество :"))
#         if warehouse[name]['quantity'] > quantity:
#             warehouse[name]['quantity'] -= quantity
#             print("Товар продан")
#         else:
#             print("Недостаточное количество товара.")
#
#     elif choice == "4": # 4 — Пополнить остаток
#         name = input("Введите товар :")
#         if name not in warehouse:
#             print("Товара нет в списке!")
#         else:
#             quantity = int(input("Введите количество :"))
#             warehouse[name]['quantity'] += quantity
#             print("Остаток пополнен.")
#
#     elif choice == "5": # 5 — Изменить цену
#         name = input("Введите товар :")
#         if name not in warehouse:
#             print("Товара нет в списке!")
#         else:
#             new_price = int(input("Введите новую цену :"))
#             warehouse[name]['price'] = new_price
#             print("Цена изменена.")
#
#     elif choice == "6":# 6 — Общая стоимость склада
#         total = 0
#         for product in warehouse.values():
#             total += product['price'] + product['quantity']
#         print(f"Общая стоимость склада {total} рублей")
#
#     elif choice == "7":  # 7 — Самый дорогой товар
#         max_price = 0
#         max_product = ""
#         for name, product in warehouse.items():
#             if product['price'] > max_price:
#                 max_product = name
#                 max_price = product['price']
#         print(f"Самый дорогой товар {max_product} стоит {max_price} рублей")
#
#     elif choice == "8": #8 — Товары с остатком меньше 3
#         flag = False
#         for name, product in warehouse.items():
#             if product['quantity'] < 3:
#                 print(f"Товары в количестве меньше 3: {name}, количество = {product['quantity']}")
#                 flag = True
#         if flag == False:
#             print(f"На складе достаточное количество товара!")

    # elif choice == "0":
    #     print("Выход.")
    #     break

#бронирвоание места в кинотеатре#
# hall = [[0 for place in range(3)] for row in range(2)]
# for row in range(2):
#     #print(f"Ряд: {row + 1}")
#     for place in range(3):
#         #print(f"Место: {place + 1}")
#         if hall[row][place] == 0:
#             answer = input(f"Ряд: {row + 1} Место: {place + 1} свободно. Хотите забронировать?(Да/Нет): ")
#             if answer == "Да":
#                 hall[row][place] = 1
#                 print(f"Ряд: {row + 1} Место: {place + 1} забронировано!")
#
#         answer_2 = input("Хотите забронировать еще? (Да/Нет): ")
#         if answer_2 == "Да":
#             continue
#         else:
#             break
#
# cnt = 0
# for row in range(2):
#     for place in range(3):
#         if hall[row][place] == 0:
#             cnt += 1
# print(f"Свободных мест осталось {cnt}")
# for row in hall:
#     print(row)

#tkinter#
def add_value():
    number.set(number.get() + 1)

def reduce_value():
    number.set(number.get() - 1)

def print_value():
    text_name = entry_name.get()
    text_age = entry_age.get()
    word = ""
    if int(text_age) not in range(10, 20):
        if int(text_age) % 10 == 1:
            word = "год"
        elif int(text_age) % 10 == 2 or int(text_age) % 10 == 3 or int(text_age) % 10 == 4:
            word = "года"
        else:
            word = "лет"
    else:
        word = "лет"
    # print(f"Привет, {text_name}! Тебе {text_age} {word}.")

    text_label.config(text=f"Привет, {text_name}! Тебе {text_age} {word}.", bg="white")



win = tk.Tk()
win.geometry("250x200") # создаем окно с заданными размерами
win.title("Анкета") # заголовок окна

# fr_center = tk.Frame(win)
# fr_center.pack()
#
# fr2 = tk.Frame(fr_center)
# fr2.pack(side = "left")
#
# fr3 = tk.Frame(fr_center)
# fr3.pack(side = "right")
#
# number = tk.IntVar(value = 0)
# label = tk.Label(fr3, textvariable = number, fg = "darkblue", bg = "lightblue",font = ("Arial", 16), height = 2, width = 20) # создаем лэйбл
# label.pack(pady = 10) # проявляем лeйбл
#
# button = tk.Button(fr2, text = "+ 1", command = add_value, height = 1, width = 5) # создаем кнопку
# button.pack()
#
# button1 = tk.Button(fr2, text = "- 1", command = reduce_value, height = 1, width = 5) # создаем кнопку
# button1.pack(pady = 10)
#
# entry = tk.Entry(fr3, width = 20)
# entry.pack(pady = 15)
#
# button2 = tk.Button(fr2, text = "Вывести в консоль", command = print_value)
# button2.pack()

name = tk.Label(win, text= "Имя:")
name.pack()

entry_name = tk.Entry(win)
entry_name.pack()

age = tk.Label(win, text= "Возраст:")
age.pack()

entry_age = tk.Entry(win)
entry_age.pack()

button = tk.Button(win, text= "Вывести", command=print_value)
button.pack(pady = 10)

text_label = tk.Label(win)
text_label.pack()



tk.mainloop()

