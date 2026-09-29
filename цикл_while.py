"""while"""
import math
# i = 0
# while i < 10:
#     i += 1
#     if i == 7:
#         break  ## прерывает цикл
#         #continue  ## прерывает итерацию, 7 выпадает
#     print(i, end=' ')
# else:
#     print('\nDone')
# print('\nEND')
#
# symbols = input('> ').upper()
# while symbols != 'END':
#     print(symbols, end=' ')
#     symbols = input('> ').upper()

# n = int(input('> '))
# sm = 0 ## сумма
# cnt = 0 ## счетик значений
# while n != 0:
#     sm += n
#     cnt += 1
#     n = int(input('>> '))
# print('Средняя температура за период: ', round(sm / cnt, 2))
# print(f'Средняя температура за период: "{sm / cnt:.2f}"')
################################# 2 знака после запятой, флоат
"""
35 100
71 cm

print(n1, n2, '\n' + str(n3), 'cm')
print(f'{n1} {n2}\n{n3} cm')
"""

"""
123 % 10 = 3
    //10 = 12 % 10 = 2
             //10 = 1 % 10 = 1
                     // 10 = 0
sm = 3 + 2 + 1
признак окончания цикла приведение числа к 0
сумма цифр и количество цифр
"""
# n = int(input('> '))
# nn = n
# sm = 0
# cnt = 0
# while n > 0:
#     rem = n % 10 # получ последнюю цифру числа
#     sm += rem # прибавляем получ цифру в sm
#     cnt += 1 # увелич счетяик на единицу
#     n //= 10 # получ целую часть числа
# print(f'В числе "{nn}" {cnt} цифр суммой {sm}')

# n = int(input('> '))
# res = 0
# while n > 0: # 123
#     rem = n % 10 # 3 -> 2 -> 1
#     res = res * 10 + rem # 3 -> 30 + 2 = 32 -> 320 + 1 = 321
#     n //= 10 # 12 -> 1 -> 0
# print(res)

"""
Наибольший общий делитель
36   24 -> 36 - 24 = 12
12   24 -> 12 - 24 = 12
12   12 -> 12 = 12 -> НОД
"""
# n1 = int(input('> '))
# n2 = int(input('>> '))
# print(f'НОД = {math.gcd(n1, n2)}')
# while n1 != n2:
#     if n1 > n2:
#         n1 -= n2
#     else:
#         n2 -= n1
# print(f'НОД = {n1}')

# for n in range(100, 200):
#     for i in range(2, n): ## простое ли число
#         if n % i == 0:
#             break
#     else:
#         print(n, end=' ')

# while True:
#     n = input('> ')
#     n1 = input('>> ')
#     if n.isnumeric() and n1.isnumeric():
#         n = int(n)
#         n1 = int(n1)
#     res = n + n1
#     print(f'{'Слово получилось: ' if isinstance(res, str) else "Сумма равна: "} {res}')
#     ##                если строка, то True
#     ## тернарный оператор if ... else ...
#     if res == 'stop':
#         break

while True:
    time = ('Может быть временем суток '
            if 0 <= (n := int(input('> '))) <= 24
            else 'Не может быть временем суток ')
    print(time)
    if n < 0:
        break

