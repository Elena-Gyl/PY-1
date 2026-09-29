"""Занятие 08.08"""
import random
from turtle import *

# 1 #
# s = 'Иванов Иван Иванович, email: ivanov_ii@examle.com, тел: +7(912)345-67-89, адрес: ул. Ленина, дом 15, кв. 200'
# ss = s.split(',')
# fio = ss[0]
# fio_s = fio.split()
# fio_f = fio_s[0]
# fio_n = (fio_s[1])[0]
# fio_o = (fio_s[2])[0]
# print(ss)
# print(f'Пользователь: {fio_f} {fio_n}.{fio_o}.')
# mail = (ss[1].split())[1]
# mail_ss = mail.split('@')
# mail_dom = mail_ss[1]
# mail_name = mail_ss[0]
# print(f'Email: домен: @{mail_dom}, имя: {mail_name}')
# tel_ss = ss[2].split()
# tel = tel_ss[1]
# print(f'Тел.: {tel}')
# adr_ss = ss[3].split(':')
# adr_yl = adr_ss[1]
# adr = adr_yl + ss[4] + ss[5]
# print(f'Адрес проживания:{adr}')

#2 и 3#
# numbers = [12, 7, 18, 5, 9, 14, 21, 8, 30, 11, 4, 15]
# print(numbers[::2])
# print(numbers[::-1])
# for num in numbers:
#     if num % 3 == 0:
#         numbers.remove(num)
# print(numbers)
# или
# new_num = [i for i in numbers if i % 3 != 0]
# print(new_num)

# chet_num = [i for i in numbers if i % 2 == 0]
# nechet_num = [i for i in numbers if i % 2 != 0]
#
# print(f"""Исходный список: {numbers}
# Количество элементов: {len(numbers)}
# Четные числа: {chet_num}
# Нечетные числа:{nechet_num}
# Максимальное значение: {max(numbers)}
# Минимальное значение: {min(numbers)}
# Среднее значение: {round(sum(numbers)/len(numbers), 2)}
# Отсортированный список: {sorted(numbers)}
# Список наоборот: {numbers[::-1]}
# """)

# 4 #
# fruits = ('яблоко', 'банан', 'груша', 'апельсин', 'банан', 'киви', 'банан', 'слива')
# banan_i = fruits.index('банан')
# banan_cnt = fruits.count('банан')
# print(banan_i)
# print(banan_cnt)
# new_fruit = ()
# for f in fruits:
#     new_fruit += (f,f)
# print(new_fruit)

# 5 #
# set1 = {2, 4, 6, 8, 10, 12}
# set2 = {6, 8, 10, 14, 16, 18}
# # inter = set1.intersection(set2)
# # un = set1.union(set2)
# print(set1&set2) # пересечение
# print(set1|set2) # объединение
# print(set1 - set2) # удалили эл-ты set2 из set1
# print(set1.issubset(set2)) # является ли set1 подмножеством set2
#                            # T/F
# 6 #
# dict = {'Иван': [5, 4, 5], 'Петр': [3, 4, 4], 'Мария': [5, 5, 4], 'Ольга': [4, 5, 5]}
# dict['Анна'] = [5, 5, 5]
# dict_1 = {'Елена': [5, 4, 5], 'Сергей': [4, 4, 5]}
# print(dict)
# del dict['Петр']
# print(dict)
# for k, v in dict.items():
#     avar = sum(v) / len(v)
#     print(k, round(avar, 2))

# 7 #
# num = random.randint(1, 100)
# p = 0
# while True:
#     num_p = int(input('Какое число загадал компьютер? '))
#     if num_p < num:
#         print('Больше!')
#         p += 1
#     elif num_p > num:
#         print('Меньше!')
#         p += 1
#     else:
#         print(f"Поздравляю! Вы угадали число {num} с {p} попытки(ок).")
#         break

# 8 #
# s = input('> ')
# s = s.lower()
# vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
# nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# cnt_vowels = 0
# cnt_consonants = 0
# cnt_nums = 0
# print(len(s))
# ss = []
# for i in range(len(s)):
#     if s[i].isspace() == False:
#         ss.append(s[i])
#
# #print(ss)
# for i in range(len(ss)):
#     if ss[i].isalpha() == True:
#         if ss[i] in vowels:
#             cnt_vowels += 1
#         else:
#             cnt_consonants += 1
#     if ss[i] in nums:
#         cnt_nums += 1
# cnt = []
# for i in range(len(ss)):
#     cnt.append(ss.count(ss[i]))
# m = max(cnt)
# symb = ss[cnt.index(m)]
#
# print(f"""Количество гласных: {cnt_vowels}
# Количество согласных: {cnt_consonants}
# Количество цифр: {cnt_nums}
# Самый частый символ: {symb}
# """)

# Черепашка #
def draw_landscape():
    penup()
    goto(-200,-200)
    pendown()
    color("lightgreen")
    begin_fill()
    for i in range(2):
        forward(400)
        left(90)
        forward(150)
        left(90)
    end_fill()

def draw_sky():
    penup()
    goto(-200, -50)
    pendown()
    color("lightblue")
    begin_fill()
    for i in range(2):
        forward(400)
        left(90)
        forward(300)
        left(90)
    end_fill()

def draw_sun():
    penup()
    goto(-150, 150)
    pendown()
    color("yellow")
    begin_fill()
    circle(50)
    end_fill()

def draw_home():
    penup()
    goto(10, -100)
    pendown()
    color("gray")
    begin_fill()
    for i in range(2):
        forward(150)
        left(90)
        forward(300)
        left(90)
    end_fill()

def draw_window():
    penup()
    x = 30
    y = 0
    goto(x, y)
    pendown()
    color("black")
    for w in range(3):
        for i in range(4):
            forward(40)
            left(90)
        penup()
        y += 60
        goto(x, y)
        pendown()

    x += 70
    for w in range(3):
        penup()
        y -= 60
        goto(x, y)
        pendown()
        for i in range(4):
            forward(40)
            left(90)

def draw_farmacy():
    penup()
    goto(-170, -100)
    pendown()
    color("gray")
    begin_fill()
    for i in range(2):
        forward(150)
        left(90)
        forward(150)
        left(90)
    end_fill()
    penup()
    goto(-105, 0)
    pendown()
    color("red")
    begin_fill()
    for i in range(2):
        forward(20)
        left(90)
        forward(10)
        left(90)
    end_fill()
    penup()
    goto(-100, -5)
    pendown()
    begin_fill()
    for i in range(2):
        forward(10)
        left(90)
        forward(20)
        left(90)

    end_fill()



draw_landscape()
draw_sky()
draw_sun()
draw_home()
draw_window()
draw_farmacy()
exitonclick()

