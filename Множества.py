""" Множества (set)"""

"""Множество - это набор неупорядоченных уник.
значений (неизм объектов)"""
# ls = [] # пустой список, множ-во так обозн. нельзя
# st = set() # пустое множество
ls = [33, 44, 22]
st = set(ls)
# print(st)
# st.clear()

# st.add(100)
# st.update({'old', 32})
# print(st)
# n = st.pop() # удалит первое значение
# st.remove('old') # удалит, если есть, если нет - ошибка
# st.discard('1001') # удалит, если знач есть, если нет - то ошибки не будет
#
# print(st)
# print(n)

"""конструкция try except нужна
для перехвата ошибок"""
# try:
#     st.remove('1001')
# except ValueError as err:
#     print(err)
# except KeyError as err:
#     print('Ошибка по ключу', err)

# try:
#     st.remove('old')
#     n = int(input('> '))
#     if n == 100:
#         raise TypeError('Ошибка типа данных')
# except ValueError:
#     print('ввод символьного значения')
# except KeyError as err:
#     print('Ошибка по ключу', err)
# except Exception as err:
#     print(err)
# else:
#     print('Ok')
# finally:
#     print('всегда')

st1 = {1, 2, 33}
st2 = {1, 2, 44}

#res = st1.union(st2) #объединение
res = st1 | st2

#res = st1.intersection(st2) #пересечение
res = st1 & st2

#res = st1.difference(st2) # вычитание
res = st1 - st2

#res = st1.symmetric_difference(st2) # симметрическая разность
res = st1 ^ st2
print(res)

st1 = {1, 2, 33} # супермножество по отношению к st3
st2 = {1, 2, 44}
st3 = {1, 2} # подмножество st1 и st2

print(st3.issubset(st1)) # T/F st3 является подмножеством st1?
print(st2.issuperset(st3)) # T/F s1 являетя супермножеством для st3?

