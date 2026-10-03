from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import shutil
import os
from datetime import datetime

# shutil.copytree(r"C:\Users\dfzmj\OneDrive\Рабочий стол\Пример папки",
#                 r"C:\Users\dfzmj\OneDrive\Рабочий стол\Пример папки_copy")

# shutil.move(r"C:\Users\dfzmj\OneDrive\Рабочий стол\Пример папки_copy\Задание1_move",
#             r"C:\Users\dfzmj\OneDrive\Рабочий стол\Пример папки")


root = Tk()
root.withdraw() #

dir_ = fd.askdirectory(title='Выбор папки')
if dir_:
    for file in os.listdir(dir_):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            file_path = os.path.join(dir_, file) # формирую маршрут
            last_time = os.path.getmtime(file_path) # время изм файла
            dt = datetime.fromtimestamp(last_time)
            dt = dt.strftime('%d.%m.%Y %X')
            print(f'{file} изменен {dt}')
else:
    root.destroy()






root.mainloop()