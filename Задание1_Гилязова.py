## 1 ##
n = 3
while n != 53:
    print(n)
    n += 10

## 2 ##
while True:
    password = input('Введите пароль: ')
    print('Длина пароля должна быть не менее 8 символов'
          if len(password) < 8 else 'Пароль сохранён')

    if password == '':
        break

## 3 ##
print('Введите параметры автомобиля по шаблону',
      'LADA 2010г 205000км 45000руб', sep = '\n')
auto = input('>')
auto_list = auto.split()
print(f"Продается автомобиль", f"Марка: {auto_list[0]}",
      f"Год выпуска: {auto_list[1]}", f"Пробег: {auto_list[2]}",
      f"Цена: {auto_list[3]}", sep = '\n')