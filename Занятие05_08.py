#1#
# s = 'Python - современный язык программирования! Многие начинают изучать Python! Мы уже пишем код на Python!!!'
# new_s = s.replace('Python', 'Java')
# new_s = new_s.replace('!', '.')
# new_s = new_s.upper()
# print(new_s)
# cnt = len(s)
# cnt2 = cnt - s.count(' ')
#
# print(cnt, cnt2)
# print(len(s.split()) - s.count('-'))

#2#
while True:
    password = input('Введите пароль: ')
    if len(password) >= 8 and password.isalnum() == True and password.islower() == False:
        print('Пароль принят!')
        break