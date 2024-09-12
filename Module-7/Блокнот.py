import tkinter
from tkinter import messagebox


def show_info():
    messagebox.showinfo('Info', 'Этот блокнот позволяет открывать и редактировать текстовые файлы.')


def show_about():
    messagebox.showinfo('About', 'Блокнот. Версия 1.0. Автор: Волик Василиса')


window = tkinter.Tk()
window.title('Блокнот')
window.geometry('400x400')

menu_bar = tkinter.Menu(window)

info_menu = tkinter.Menu(menu_bar, tearoff=0)
info_menu.add_command(label='Info', command=show_info)
menu_bar.add_cascade(label='Info', menu=info_menu)

about_menu = tkinter.Menu(menu_bar, tearoff=0)
about_menu.add_command(label='About', command=show_about)
menu_bar.add_cascade(label='About', menu=about_menu)

window.config(menu=menu_bar)

window.mainloop()
