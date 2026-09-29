import tkinter as tk
import random

choice = ""
def stone_choice():
    choice = button_stone["text"]

def cutter_choice():
    choice = button_cutter["text"]

def paper_choice():
    choice = button_paper["text"]

options = ["камень", "ножницы", "бумага"]
comp_choice = random.choice(options)

if choice == comp_choice:
    game_label2 = tk.Label(fr_1, text="Ничья")
    game_label2.pack()

win = {"камень": "ножницы", "ножницы": "бумага", "бумага": "камень"}

if win[choice] == comp_choice:
    game_label3 = tk.Label(fr_1, text="Ура! Вы победили!")
    game_label3.pack()

else:
    game_label3 = tk.Label(fr_1, text="Вы проиграли")
    game_label3.pack()

win = tk.Tk()
win.geometry("300x300")
win.title('Игра "Камень. Ножницы. Бумага"')

fr_center = tk.Frame(win)
fr_center.pack()

fr_1 = tk.Frame(fr_center)
fr_1.pack(side = tk.TOP)

fr_2 = tk.Frame(fr_center)
fr_2.pack(side = tk.BOTTOM)


button_stone = tk.Button(fr_2, text = "Камень", font = ("Arial", 16), command = stone_choice)
button_stone.pack()

button_cutter = tk.Button(fr_2, text = "Ножницы", font = ("Arial", 16), command = cutter_choice)
button_cutter.pack()

button_paper = tk.Button(fr_2, text = "Бумага", font = ("Arial", 16), command = paper_choice)
button_paper.pack()

game_label = tk.Label(fr_1, text=f"Вы выбрали {choice}")
game_label.pack()

game_label1 = tk.Label(fr_1, text=f"Компьютер выбрал {comp_choice}")
game_label1.pack()





tk.mainloop()