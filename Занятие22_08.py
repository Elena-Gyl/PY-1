from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import random


# Светофор с радиокнопками

# def game():
#     comp_color = random.choice(list(colors))
#     user_color = col.get().strip()
#     print(comp_color, user_color)
#     if not user_color:
#         mb.showwarning(title="Ошибка!", message="Заполните поле!")
#         return
#
#     if user_color == comp_color:
#         result = "Поздравляю, Вы угадали"
#         result_c = f"Цвет: {comp_color}"
#
#     else:
#         result = "Не повезло!Вы не угадали"
#         result_c = f"Цвет: {comp_color}"
#
#     q = mb.askyesno(title="Вопрос", message="Показать ответ в сообщении?")
#     if q:
#         mb.showinfo(title="Вывод ответа", message=f"""{result}
#         {result_c}""")
#     else:
#         l_res.config(text=result)
#         l_res_c.config(text=result_c, bg=colors[comp_color])
#
#
#
# colors = {
#     'красный':"red",
#     'желтый':'yellow',
#     'зеленый':'green'
# }
#
# window = Tk()
# window.title("Угадай цвет светофора")
# window.geometry("400x300")
#
# l = Label(window, text="Выберите цвет светофора:", font="Arial 14 bold")
# l.pack(pady=10)
#
# col = StringVar(value=" ")
#
# red = Radiobutton(window, text="Красный", font="Arial 12",
#                   variable=col, value="красный")
# red.pack()
#
# yellow = Radiobutton(window, text="Желтый", font="Arial 12",
#                   variable=col, value="желтый")
# yellow.pack()
#
# green = Radiobutton(window, text="Зеленый", font="Arial 12",
#                   variable=col, value="зеленый")
# green.pack()
#
# b = Button(window, text="Проверить", font="Arial 12", command=game)
# b.pack(pady=10)
#
# l_res = Label(window, text="", font="Arial 12")
# l_res.pack(pady=10)
#
# l_res_c = Label(window, text="", font="Arial 12")
# l_res_c.pack()
#
# window.mainloop()

#Менеджер заметок


def about():
    mb.showinfo("О программе", 'Приложение "Менеджер заметок"')

def clear():
    q = mb.askyesno("Очистка", "Очистить все заметки?")
    if q:
        t.delete(1.0, END)


def add():
    try:
        file = fd.askopenfilename(
            filetypes = [("Text", "*.txt"), ("All", "*.*")]
        )

        if not file:
            mb.showerror("Ошибка!", "Файл не выбран!")
            return
        with open(file, "r", encoding="utf-8") as file:
            note = file.read()
            t.insert(END, note)
    except Exception as e:
        mb.showerror("Ошибка!", f"Выбран файл неверного формата!\n{e}")


def save():
    try:
        file = fd.asksaveasfilename(
            filetypes = [("Text", "*.txt")]
        )
        if not file:
            mb.showerror("Ошибка!", "Файл не выбран!")
            return

        with open(file, "w", encoding="utf-8") as file:
            note = t.get(1.0, END)
            file.write(note)
            mb.showinfo("Info", "Файл успешно сохранён")

    except Exception as e:
        mb.showerror("Ошибка!", e)


window = Tk()
WIDTH = window.winfo_screenwidth()
HEIGHT = window.winfo_screenheight()
X_x = 600
Y_y = 400
window.geometry(f"{X_x}x{Y_y}+{WIDTH // 2 - X_x // 2}"
              f"+{HEIGHT // 2 - Y_y // 2}")

window.title("Менеджер заметок")
mainmenu = Menu(window)
window.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Добавить заметку", command=add)
filemenu.add_command(label="Очистить", command=clear)
filemenu.add_command(label="Сохранить", command=save)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=lambda: window.destroy())

aboutmenu = Menu(mainmenu, tearoff=0)
aboutmenu.add_command(label="О программе", command=about)

mainmenu.add_cascade(label="Meню", menu=filemenu)
mainmenu.add_cascade(label="Инфо", menu=aboutmenu)

text_frame = Frame(window)
text_frame.pack(side=LEFT)

# menu_frame = Frame(window)
# menu_frame.pack(side=LEFT)

t = Text(text_frame, width=70, height=10, bg="#FFFFE0", wrap=WORD)
t.pack(side=LEFT)

scr = Scrollbar(text_frame, orient=VERTICAL, command=t.yview)
scr.pack(fill=Y, side=RIGHT)
t.config(yscrollcommand=scr.set)

# b1 = Button(menu_frame, text = "Добавить заметку", command=add)
# b1.pack()
#
# b2 = Button(menu_frame, text = "Очистить", command=clear)
# b2.pack()
#
# b3 = Button(menu_frame, text = "Сохранить", command=save)
# b3.pack()

window.mainloop()

