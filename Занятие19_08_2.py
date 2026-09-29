from tkinter import *
from tkinter import messagebox as mb
import random

def game():
    comp_color = random.choice(list(colors))
    user_color = e.get().strip()
    print(comp_color, user_color)
    if not user_color:
        mb.showwarning(title="Ошибка!", message="Заполните поле!")
        return

    if user_color == comp_color:
        result = "Поздравляю, Вы угадали"
        result_c = f"Цвет: {comp_color}"

    else:
        result = "Не повезло!Вы не угадали"
        result_c = f"Цвет: {comp_color}"

    q = mb.askyesno(title="Вопрос", message="Показать ответ в сообщении?")
    if q:
        mb.showinfo(title="Вывод ответа", message=f"""{result}
        {result_c}""")
    else:
        l_res.config(text=result)
        l_res_c.config(text=result_c, bg=colors[comp_color])



colors = {
    'красный':"red",
    'желтый':'yellow',
    'зеленый':'green'
}

window = Tk()
window.title("Угадай цвет светофора")
window.geometry("400x300")

l = Label(window, text="Введите цвет светофора:", font="Arial 14 bold")
l.pack()

e = Entry(window, font="Arial 12")
e.pack(pady=10)

b = Button(window, text="Проверить", font="Arial 12", command=game)
b.pack()

l_res = Label(window, text="", font="Arial 12")
l_res.pack(pady=10)

l_res_c = Label(window, text="", font="Arial 12")
l_res_c.pack()

window.mainloop()



