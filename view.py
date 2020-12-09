from tkinter import *
from tkinter import messagebox

from sympy import SympifyError

from controller import my_solve

FONT = ("Arial Bold", 14)
window = Tk()
txt_input = Entry(window, font=FONT)
frame_solution = Frame(window)
lbl_output = Text(frame_solution, font=FONT, wrap=WORD)


def clicked():
    try:
        solution = my_solve(txt_input.get())
        print(type(solution[0]))
        lbl_output.configure(state='normal')
        lbl_output.delete(1.0, END)
        lbl_output.insert(0.0, str(solution)[1:-1].replace(', ', ',\n\n'))
        lbl_output.configure(state='disabled')
    except SympifyError:
        messagebox.showerror('Ошибка в выражении', 'Невозможно вычислить корни выражения')


def init():
    window.title("Решение многочлена")
    window.geometry('640x480')

    lbl_input = Label(window, text="Введите многочлен", font=FONT)
    lbl_input.pack(padx=20, pady=10, anchor=W)
    txt_input.pack(padx=20, pady=10, fill=BOTH)
    txt_input.focus()
    btn_solve = Button(window, text="Решить", command=clicked, font=FONT)
    btn_solve.pack(padx=20, pady=20, expand=1, fill=BOTH)
    lbl_answer = Label(frame_solution, text="Решения:", font=FONT)
    lbl_answer.pack(padx=20, pady=20, side=LEFT)
    lbl_output.pack(padx=20, pady=20, side=LEFT)
    frame_solution.pack(padx=20, pady=20, expand=1, fill=BOTH)

    window.mainloop()
