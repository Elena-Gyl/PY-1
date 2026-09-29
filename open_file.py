#file = open('text.txt','r', encoding= 'utf-8') # метод r - открывает для чтения
# # s = file.read() # прочитает (n) символов
# # print(s)
# # s = file.readline() # прочитает все, что осталось
# # print(s)
# s = file.readlines()
# print(s)
# file.close()
# #должны прочитать один раз и обязательно закрыть файл

# for i in open('text.txt', encoding='utf-8'):
#     print(i.rstrip())
#
with open('text.txt', encoding='utf-8') as file:
    ls = file.read().title().split()
#ls.sort()
print(ls)

with open('text1.txt', 'w', encoding='utf-8') as file:
    for k, i in enumerate(ls, 1):
        file.write(f'{k}. {i}\n')

# w - перезаписывает (заново, с нуля)
# a - добавляет
# r - читает