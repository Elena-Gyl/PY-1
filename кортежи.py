"""Кортежи (tuple)
Упорядоченный габор неизменяемых объектов"""

# from string import ascii_lowercase, ascii_uppercase, digits, ascii_letters
#
# print(ascii_lowercase)
# print(ascii_uppercase)
# print(digits)
# print(ascii_letters)
#
# t  = 22
# tp = (22, 33, 44)
# print(id(tp[0]), id(t))
# # tp[0] = 220  не работает
# print(tp[1])  # получение значения по индексу
# print(tp[:-1])  # срез с кортежа
# print(tp[::-1])
# print(type(tp))  # тип объекта
# print(list(tp))
# string = 'qwerty'
# lst = list(string)
# print(lst)
# print(''.join(lst))
# tps = tuple(string)
# print(tps)
# print(''.join(tps))
#
# print(ord('A'))  # lat
# print(ord('А'))  # рус
# print(ord('\n'))
# print(ord('\t'))
# print(ord('\r'))
# print(ord('2'))
# print(chr(1049))
#
# # n = 7, 5, 8 # будет формироваться кортеж
# n, m, z = (7, 5, 8)
# print(type(n))
# print(n)
#
# PI = 3.1415926,
# print(PI[0])
# print(type(PI))
#
# name, *marks, predlast, last = 'Ivan', 4, 5, 3, 5, 7 # * оператор - упаковщик
# print(name) # Иван
# print(marks) # список [4, 5, 3]
# #print(*marks) # 4, 5, 3 распаковка списка
# print(predlast) # 5
# print(last) # 7
#
# tp = ('login', 'password') # кортеж неизм
# print(tp)
# print(id(tp)) # один айди
# buff = list(tp)
# print(buff)
# buff[-1] = 'qwerty'
# print(buff)
# tp = tuple(buff)
# print(id(tp)) # другой айди
# print(tp) # другой кортеж стем же именем

tp = (22, 33, 44, 22)
print(tp)
print(len(tp))
print(tp.count(22))
print(tp.index(22))
print(tp[0] == tp[-1]) # сравнение первого объекта с последним, True
print(tp[0] is tp[-1]) # является ли этот объект тем же самым? True
print(id(tp[0]), id(tp[-1]))





