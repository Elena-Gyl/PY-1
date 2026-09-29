# from datetime import datetime, date
#
# count_info = 0
# count_error = 0
# count_warning = 0
#
# dates = []
#
# with open(r"C:\Users\dfzmj\OneDrive\Рабочий стол\logs.txt", 'r', encoding = 'utf-8') as f:
#     for line in f:
#         if line.split()[1] == 'INFO':
#             count_info += 1
#         elif line.split()[1] == 'ERROR':
#             count_error += 1
#         elif line.split()[1] == 'WARNING':
#             count_warning += 1
#
#         dates.append(line.split()[0])
#
# early_date = datetime.strptime(min(dates), '%Y-%m-%d')
# latest_date = datetime.strptime(max(dates), '%Y-%m-%d')
#
# variance = latest_date - early_date
#
#
# print(f'''Количество INFO: {count_info}
# Количество ERROR: {count_error}
# Количество WARNING: {count_warning}
# Самая ранняя дата: {early_date.date()}
# Самая поздняя дата: {latest_date.date()}
# Разница: {variance.days}''')

def procces_list(lst):
    if not isinstance(lst, list):
        return ("Ошибка: аргумент не является списком")
    #Списковое включение
    new_lst = [i**2 if i%2==0 else i**3 for i in lst]

    #new_lst = []
    # for i in lst:
    #     if i%2==0:
    #         new_lst.append(i**2)
    #     else:
    #         new_lst.append(i**3)

    return new_lst

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#lst = 'hhh'
print(procces_list(lst))

#Лямба-функция
new_lst = list(map(lambda i: i**2 if i%2==0 else i**3, lst))
print(new_lst)