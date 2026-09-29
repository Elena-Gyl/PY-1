"""
СПИСКИ (list)
тип данных - списки, структура д. - массив """
from copy import deepcopy
import random

"""Список - упорядоченный набор объектов"""
"""     0    1   2   3   4 """
# nums = [55, 33, 44, 99, 77]
"""     -5  -4  -3  -2  -1 """
# print(nums[2])
# print(nums[-3])
# print(nums[2::-1])
# print(nums[2:])
# print(nums[::-1])  # реверсивный вывод
#nums = [20, 30, [40, 50]]
#s = nums
#s = nums.copy() # поверхностное копирование
# так как копирует НЕизм объекты, а изм. изменятся
# s = deepcopy(nums) # глубокое копирование
# nums[0] = 200
# nums[-1][0] = 400
# print(nums) #[200, 30, [400, 50]]
# print(id(nums))
# print(id(s))
# print(s) # [20, 30, [400, 50]]
# nums[:3] = 10, 20, 30
# print(nums)

# nums.append(100) # временная сложность 0(1) - констанстная
# nums.insert(3, 200) # временная сложность 0(1) - линейная
# nums.extend([1, 2]) # объедин списки, как конкатенация
# #nums += [1,2] # один айди
# #nums = nums + [1, 2] # айди новый
# nums.pop() # удаляет последний эл-т списка, врем сл - конст
# n = nums.pop() # сохр удаленный эл-т
# nn = nums.pop(3)
# nums.remove(100) # удалит конкретный эл-т (только первый)
# while 55 in nums:
#     nums.remove(55) # удалит все конкретные эл-ты

# print(id(nums))
# print(nums)
# print('n =', n, 'nn =', nn)
# print(len(nums))
# print(nums.index(55))
# print(nums.count(55))
# print(sum(nums))
# print(max(nums))
# print(min(nums))
# nums.reverse()
# nums.sort()
# nums.sort(reverse = True)

# nums = []
# n = 0
# while n != -273:
#     n = float(input('> '))
#     nums.append(n)
# nums.remove(-273)
#
# print(f"""min = {min(nums)}
# max = {max(nums)}
# mean = {sum(nums)/len(nums):.2f}""")

nums = [22, 33, 44, 55, 99]
ls = [2, 3, 4, 5, 9, 10]
# print(nums)
# # итерация по индексу
# for i in range(len(nums)): # 0, 1, 2, 3, 4
#     print(i, nums[i], ls[i], end = '  ')
# print()
# # по значению
# cnt = 0
# for i in nums:
#     print(cnt, i, end = '  ')
#     cnt += 1
# print()
# for i in enumerate(nums): # будут кортежи из индекса и эл-та
#     print(i[0], i[1],  end = '  ')  # если print(i, end = ' ')
# print()
# for i, j in enumerate(nums):
#     print(i, j, end = '  ')
# print()
names = ['Fedor', 'Alisa', 'Sasha', 'Glasha', 'Masha']
# names.sort()
# for n, name in enumerate(names, 1):
#     print(f'{n}.{name}')
#
# for i, j in zip(nums, ls): # получаем кортежи, обрезает лишние значения, если списки не одинаковые
#     print(i - j)

# # генерация случайных вещественных чисел
# print(random.random())
# print(random.uniform(0.9,1))
# print(random.uniform(-100,-99))
#
# # генерация целых чисел
# print(random.randint(2,10))
# print(random.randrange(2, 100, 2))
# print(random.randrange(1, 20, 2))
#
# #генерация случайного выбора из коллекции
# print(random.choice(nums))
# print(random.choice(range(1, 10, 3)))
# print(random.choice(names))
#
# # генерация коллекции случ объектов
# print(random.choices('аивгдеёжз', k = 4))
# print(random.choices(names, k = 7)) # вытащит рандомные имена n раз
# print(random.sample(names, k = len(names))) # вытащит имена, не повторяя, как бы пересортирует список

a = 'I like python, it is very useful for data analysis'
b = 'python is the best tool for dealing with big data'
a_split = (a.replace(',', '')).split()
b_split = b.split()
c = []
for word in b_split:
    if word not in a_split:
        c.append(word)
# res = [word for word in b if word not in a]

# print(' '.join(c))
# print(' '.join([word for word in b_split if word not in a_split]))

# res = random.sample(range(1000000), 1000000)
# res.insert(0, 0)
# for n, i in enumerate(res, 1):
#     print(n, i)
#     if i == 0:
#         break

# n = int(input('Введите количество студентов: '))
# data = {}
# for i in range(n):
#     name, *marks = input('формат: имя 5 4 3 2 :> ').split()
#     marks = [int(mark) for mark in marks]
#     mean = sum(marks) / len(marks)
#     data[name] = round(mean, 2)
# print(data)


s = 'rewerewferwetfdsrewerewferwetfdsrewerewferwetfds'
print({symb:s.count(symb) for symb in set(s)})


