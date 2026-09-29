login = 'Student'
password = '1234'
cnt_p = 1
cnt_w = 0

for _ in range(10):
    while True:
        print('Пользователь ', cnt_p)
        login1 = input('Введите логин: ')
        password1 = input('Введите пароль: ')

        if login == login1 and password == password1:
            print('Доступ разрешен')
            print('')
            cnt_p += 1
            cnt_w = 0
            break
        else:
            print('Ошибка ввода данных', cnt_w + 1)
            cnt_w +=1
            print('')
        if cnt_w == 3:
           cnt_p += 1
           print('Учетная запись заблокирована')
           print('')
           cnt_w = 0
           break