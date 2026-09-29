"""Графический редактор"""
import tkinter
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from PIL import Image, ImageTk, ImageGrab


# Функция для рисования на холсте
def draw(event):
    pen_size = change_pen_size()
    x, y = event.x, event.y
    canvas.create_oval(x, y, x + 5, y + 5, fill=pen_color, outline=pen_color, width=pen_size)

#Изменение тощины пера
def change_pen_size():
    global pen_size
    size = entry_size.get()
    if size == "":
        pen_size = 1
    else:
        try:
            pen_size = int(size)
        except ValueError:
            print("Введите целое число")
    return pen_size


# Загрузка изображения
def load_image():
    file_path = fd.askopenfilename(filetypes=[('Image files',
'*.png;*.jpg;*.jpeg;*.bmp;*.gif')])
    if file_path:
        image = Image.open(file_path)
        image = image.resize((600, 400))
        image_tk = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor=NW, image=image_tk)
        canvas.image = image_tk

#Обработка исключений для загрузки
def load_image():
    try:
        file_path = fd.askopenfilename(filetypes=[('Image files',
'*.png;*.jpg;*.jpeg;*.bmp;*.gif')])
        if file_path: # Проверяем, был ли выбран файл
            image = Image.open(file_path)
            image = image.resize((600, 400))
            image_tk = ImageTk.PhotoImage(image)
            canvas.create_image(0, 0, anchor=NW, image=image_tk)
            canvas.image = image_tk # Сохраняем ссылку на изображение
    except Exception as e:
        mb.showerror("Ошибка", f"Не удалось загрузить: {e}")


# Сохранение изображения
def save_canvas():
    file_path = fd.asksaveasfilename(defaultextension='.png', filetypes=[('PNG files', '*.png')])
    if file_path: # Проверяем, был ли указан путь для сохранения
        x = window.winfo_rootx() + canvas.winfo_x()
        y = window.winfo_rooty() + canvas.winfo_y()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)
        mb.showinfo("Сохранено!", "Изображение успешно сохранено.")

#Обработка исключений для сохранения
def save_canvas():
    try:
        file_path = fd.asksaveasfilename(defaultextension='.png', filetypes=[('PNG files', '*.png')])
        if file_path: # Проверяем, был ли указан путь для сохранения
            x = window.winfo_rootx()
            y = window.winfo_rooty()
            x1 = x + 600
            y1 = y + 400
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)
            mb.showinfo("Сохранено!", "Изображение успешно сохранено в PNG файл!")
    except Exception as e:
        mb.showerror("Ошибка", f"Не удалось сохранить: {e}")

#Выход
def quit():
    window.destroy()


window = Tk()
window.title("Графический редактор")

canvas = Canvas(window, width=600, height=400)
canvas.pack()
canvas.bind("<B1-Motion>", draw)

colors = ["red", "green", "blue", "black"]
for color in colors:
    lbl = Label(window, text="", bg=color, width=8, height=2)
    lbl.pack(side=LEFT)
    lbl.bind("<Button-1>", lambda e, c=color: globals().update(pen_color=c))

menu_bar = Menu(window)

window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить изображение", command=load_image)
file_menu.add_command(label="Сохранить холст", command=save_canvas)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=quit)

"""РЕШЕНИЕ ЗАДАНИЯ"""
Label(window, text="Толщина линии: ").pack(side = LEFT)
entry_size = tkinter.Entry(window, width= 10)
entry_size.pack(side = LEFT, padx = 10)
Button(window, text="Установить толщину", command=change_pen_size).pack(side = LEFT)


window.mainloop()