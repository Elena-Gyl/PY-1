#Просмотр сайта google.com.
from tkinter import *
import tkinterweb
import time
import datetime as dt

# window=Tk()
# frame = tkinterweb.HtmlFrame(window)
# frame.load_website("https://www.google.com")
# frame.pack(fill="both", expand=1)
# window.mainloop()

# Просмотр любого сайта
# Добавляем поле ввода и кнопку для ввода
# произвольного адреса сайта

# def read(event=None):
#     Site = e.get()
#     frame.load_website(Site)
#
#
# window=Tk()
# m = Label(text="введите адрес сайта:")
# m.pack()
# e = Entry(width=20, justify='left')
# e.pack()
# b = Button(text="Ввод", command=read)
# b.pack()
# e.bind('<Return>', read) # привязываем событие к entry
# frame = tkinterweb.HtmlFrame(window)
# frame.pack(fill="both", expand=1)
# window.mainloop()

#Задание
# Добавьте в проект еще один фрейм, и поместите в него метку,
# поле ввода и кнопку, чтобы они располагались слева направо

# def read(event=None):
#     Site = e.get()
#     frame.load_website(Site)
#
#
# window=Tk()
# f = Frame(window)
# f.pack()
# m = Label(f, text="Введите адрес сайта:")
# m.pack(side=LEFT)
# e = Entry(f, width=20, justify='left')
# e.pack(side=LEFT)
# b = Button(f, text="Ввод", command=read)
# b.pack(side=LEFT)
# e.bind('<Return>', read)
# frame = tkinterweb.HtmlFrame(window)
# frame.pack(fill="both", expand=1)
# window.mainloop()

#Выводим дату и время

# window=Tk()
# window.title('Календарь')
# window.geometry('600x200')
# time = time.strftime('%c')
# m = Label(font="Verdana 24 bold")
# m.pack()
# m.config(text=time)
# window.mainloop()

#Выводим только дату

# window=Tk()
# window.title('Календарь')
# window.geometry('600x200')
# time = time.strftime('%d %B %Y')
# m = Label(font="Verdana 24 bold")
# m.pack()
# m.config(text=time)
# window.mainloop()

#Переводим название месяца

# window=Tk()
# window.title('Календарь')
# window.geometry('600x200')
# Month = time.strftime('%B')
# Year = time.strftime('%Y')
# match Month:
#     case "January":
#         Month = "Январь"
#     case "February":
#         Month = "Февраль"
#     case "March":
#         Month = "Март"
#     case "August":
#         Month = "Август"
#     case "September":
#         Month = "Сентябрь"
#
# m = Label(font="Verdana 24 bold")
# m.pack()
# m.config(text=Month + " " + Year)
# window.mainloop()

#Часы

# def tick():
#     t = time.strftime("%H:%M:%S")
#     m.config(text=t)
#     m.after(1000, tick) # вызовы идут каждую секунду
#
#
# window=Tk()
# window.title('Часы')
# m = Label(font="Verdana 24 bold")
# m.pack()
# tick()
# window.mainloop()

#Задание
# Запрограммируй чтобы программа выводила день недели на русском языке в виде фразы “Сегодня понедельник”

# window = Tk()
# window.title("Календарь")
# Day = time.strftime('%A')
# match Day:
#     case "Monday":
#         Day = "понедельник"
#     case "Tuesday":
#         Day = "вторник"
#     case "Wednesday":
#         Day = "среда"
#     case "Thursday":
#         Day = "четверг"
#     case "Friday":
#         Day = "пятница"
#     case "Saturday":
#         Day = "суббота"
#     case "Sunday":
#         Day = "воскресенье"
# metka = Label(window, font=("Verdana 24 bold"))
# metka.pack()
# metka.config(text = "Сегодня " + Day)
# window.mainloop()

# Радиокнопки

# window=Tk()
# window.title("Радиокнопки")
# window.geometry("600x400")
#
# kvas = "Квас"
# tea = "Чай"
# coffee = "Кофе"
# drink = StringVar(value=coffee)
#
# m = Label(text="Выбери любимый напиток:")
# m.pack()
#
# m2 = Label(textvariable=drink)
# m2.pack()
#
# minecraft_b = Radiobutton(text=kvas, value=kvas, variable=drink)
# minecraft_b.pack()
#
# roblox_b = Radiobutton(text=tea, value=tea, variable=drink)
# roblox_b.pack()
#
# brawl_b = Radiobutton(text=coffee, value=coffee, variable=drink)
# brawl_b.pack()
#
# window.mainloop()

#Часы с радиокнопками

# def datetime():
#     m.config(text = f"{Date} {Time}")
#
#
# def date():
#     m.config(text = Date)
#
#
# def time():
#     m.config(text = Time)
#
#
# def night():
#     m.config(bg="black", fg="white")
#     R1.config(bg="black", fg="white")
#     R2.config(bg="black", fg="white")
#     R3.config(bg="black", fg="white")
#     R4.config(bg="black", fg="white")
#
#
# window=Tk()
# window.title("Часы с радиокнопками")
#
# d = dt.datetime.now()
# Date = d.strftime('%d %B %Y')
# print(Date)
# Time = d.strftime('%X')
# print(Time)
#
# var = IntVar()
# var.set(0)
#
# R1 = Radiobutton(text="Дата и время", command=datetime,
#                  variable=var, value=0)
# R1.pack(side = LEFT)
#
# R2 = Radiobutton(text="Дата", command=date,
#                  variable=var, value=1)
# R2.pack(side = LEFT)
#
# R3 = Radiobutton(text="Время", command=time,
#                  variable=var, value=2)
# R3.pack(side = LEFT)
#
# R4 = Radiobutton(text="Ночная тема", command=night,
#                  variable=var, value=3)
# R4.pack(side = LEFT)
#
# m = Label(font="Verdana 24 bold")
# m.pack(side = LEFT)
# m.config(text = f"{Date} {Time}")
#
# window.mainloop()

# Часы с флажками

def tick():
    t = time.strftime("%H:%M:%S")
    m.config(text=t)
    m.after(1000, tick)


def bg_color():
    m['bg'] = v1.get()


def fg_color():
    m['fg'] = v2.get()


def font():
    m['font'] = v3.get()


def size():
    m['height'] = v4.get()


window = Tk()
window.title("Часы с флажками")
window.geometry('400x300')

m = Label(font='Verdana 16', bg='lightblue', fg='black')
m.pack()

v1 = StringVar()
v1.set('lightblue')

c1 = Checkbutton(text='Переключатель цвета фона', variable=v1, onvalue='salmon',
                 offvalue='lightblue', command=bg_color)
c1.pack()

v2 = StringVar()
v2.set('black')

c2 = Checkbutton(text='Переключатель цвета текста', variable=v2, onvalue='white',
                 offvalue='black', command=fg_color)
c2.pack()

v3 = StringVar()
v3.set('Verdana 16')

c3 = Checkbutton(text='Переключатель шрифта', variable=v3, onvalue='Courier 16 bold',
                 offvalue='Verdana 16', command=font)
c3.pack()

v4 = IntVar()
v4.set(1)
c4 = Checkbutton(text='Переключатель высоты', variable=v4, onvalue=3,
                 offvalue=1, command=size)
c4.pack()

tick()
window.mainloop()