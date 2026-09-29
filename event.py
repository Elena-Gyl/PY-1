import tkinter as tk

def show_event_info(event):
    info = f"""
    Виджет: {event.widget}
    Координаты: ({event.x},{event.y})
    Координаты экраны: ({event.x_root},  {event.y_root})
    """

    if hasattr(event, 'char'): # для клавиши клавиатуры
        info += f'Символ: {event.char}; '
        info += f'Имя клавиши: {event.keysym}; '
        info += f'Код клавиши: {event.keycode}; '

    if hasattr(event, 'num'):
        info += f'Номер кнопки: {event.num} '

    print(info)


root = tk.Tk()
root.geometry('300x150+200+200')
frame = tk.Frame(root, width = 200, height = 100, bg = 'light gray')
frame.pack(pady = 20, padx = 20)

frame.bind('<Button>', show_event_info)
frame.bind('<Key>', show_event_info)
frame.focus_set()


root.mainloop()

