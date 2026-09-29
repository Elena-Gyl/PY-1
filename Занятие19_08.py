from tkinter import *
from tkinter import messagebox


def show_info():
    name = e_name.get().strip()
    surname = e_surname.get().strip()
    group = e_group.get().strip()
    age = e_age.get().strip()
    gender_ = gender.get()
    about = t_about.get(1.0, END)

    l_info.config(text=f""" Студент: {name} {surname} 
    Группа: {group} 
    Возраст: {age}
    Пол: {gender_}
    О себе: {about}""")

    if not name or not surname or not group or not age or not gender_:
        messagebox.showwarning(title="Ошибка",
                               message="Заполните все поля!")
        return

    if  not age.isdigit():
        messagebox.showwarning(title="Ошибка",
                               message="Возраст должен быть числом!")
        return


def clear():
    global gender
    e_name.delete(0, END)
    e_surname.delete(0, END)
    e_group.delete(0, END)
    e_age.delete(0, END)
    gender = StringVar(value=" ")

    l_info.config(text="")
    t_about.delete(1.0, END)


window = Tk()
window.title("Анкета студента")
window.geometry('600x500')

header_frame = Frame(window)
header_frame.grid(column=0, row=0)

form_frame = Frame(window)
form_frame.grid(column=0, row=1)

button_frame = Frame(window)
button_frame.grid(column=0, row=3)

about_frame = Frame(window)
about_frame.grid(column=0, row=2)

l = Label(header_frame, text="Анкета студента", font="Verdana 14 bold")
l.grid(column=0, row=0)

b1 = Button(button_frame, text='Показать данные', font="Verdana 12",
            command=show_info)
b1.grid(column=0, row=0)

b2 = Button(button_frame, text='Выход', font="Verdana 12",
            command=lambda: window.destroy())
b2.grid(column=2, row=0)

b3 = Button(button_frame, text='Очистить', font="Verdana 12",
            command=clear)
b3.grid(column=1, row=0)

l_name = Label(form_frame, text='Имя:', font="Verdana 12")
l_name.grid(column=0, row=0)
e_name = Entry(form_frame, font="Verdana 12")
e_name.grid(column=1, row=0)

l_surname = Label(form_frame, text='Фамилия:', font="Verdana 12")
l_surname.grid(column=0, row=1)
e_surname = Entry(form_frame, font="Verdana 12")
e_surname.grid(column=1, row=1)

l_group = Label(form_frame, text='Группа:', font="Verdana 12")
l_group.grid(column=0, row=2)
e_group = Entry(form_frame, font="Verdana 12")
e_group.grid(column=1, row=2)

l_age = Label(form_frame, text='Возраст:', font="Verdana 12")
l_age.grid(column=0, row=3)
e_age = Entry(form_frame, font="Verdana 12")
e_age.grid(column=1, row=3)

gender = StringVar(value=" ")

l_gender = Label(form_frame, text='Пол:', font="Verdana 12")
l_gender.grid(column=0, row=4)

rb1 = Radiobutton(form_frame, text='Мужской', font="Verdana 12",
                  variable=gender, value='Мужской')
rb1.grid(column=1, row=5)

rb2 = Radiobutton(form_frame, text='Женский', font="Verdana 12",
                  variable=gender, value='Женский')
rb2.grid(column=1, row=6)

l_about = Label(about_frame, text='О себе:', font="Verdana 12")
l_about.grid(column=0, row=7)

t_about = Text(about_frame, font="Verdana 12", width=30, height=3)
t_about.grid(column=1, row=8)

scr = Scrollbar(about_frame, command=t_about.yview)
scr.grid(column=2, row=8)
t_about.config(yscrollcommand=scr.set)

l_info = Label(window, text='', font="Verdana 12")
l_info.grid(column=0, row=4)


window.mainloop()