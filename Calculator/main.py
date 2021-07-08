from tkinter import *

calc = Tk()
calc.title("Calculator")

calc.grid_columnconfigure(0, weight=1)
calc.grid_columnconfigure(1, weight=1)
calc.grid_columnconfigure(2, weight=1)
calc.grid_columnconfigure(3, weight=1)
calc.grid_rowconfigure(0, weight=1)
calc.grid_rowconfigure(1, weight=1)
calc.grid_rowconfigure(2, weight=1)
calc.grid_rowconfigure(3, weight=1)
calc.grid_rowconfigure(4, weight=1)
calc.grid_rowconfigure(5, weight=1)

entry_line = Entry(calc, width=64)
entry_line.grid(row=0, column=0, columnspan=4)
answer = False


def add_input(inp):
    global answer
    current = entry_line.get()
    entry_line.delete(0, END)
    if inp == "bc":
        entry_line.insert(0, str(current)[:-1])
    else:
        if answer:
            entry_line.delete(0, END)
            if inp.isdigit():
                entry_line.insert(0, str(inp))
            else:
                entry_line.insert(0, "0" + str(inp))
            answer = False
        else:
            entry_line.insert(0, str(current) + str(inp))


def calculate(event=None):
    current = entry_line.get()
    entry_line.delete(0, END)
    entry_line.insert(0, eval(current))
    global answer
    answer = True


def clear():
    entry_line.delete(0, END)


entry_line.bind("<Return>", calculate)

plus_button = Button(calc, text="+", padx=39, pady=20, command=lambda: add_input("+"))
plus_button.grid(row=1, column=0)
divide_button = Button(calc, text="/", padx=40, pady=20, command=lambda: add_input("/"))
divide_button.grid(row=1, column=1)
multiply_button = Button(calc, text="*", padx=40, pady=20, command=lambda: add_input("*"))
multiply_button.grid(row=1, column=2)
minus_button = Button(calc, text="-", padx=40, pady=20, command=lambda: add_input("-"))
minus_button.grid(row=1, column=3)

button_7 = Button(calc, text="7", padx=40, pady=20, command=lambda: add_input("7"))
button_7.grid(row=2, column=0)
button_8 = Button(calc, text="8", padx=40, pady=20, command=lambda: add_input("8"))
button_8.grid(row=2, column=1)
button_9 = Button(calc, text="9", padx=40, pady=20, command=lambda: add_input("9"))
button_9.grid(row=2, column=2)
left_brackets_button = Button(calc, text="(", padx=40, pady=20, command=lambda: add_input("("))
left_brackets_button.grid(row=2, column=3)

button_4 = Button(calc, text="4", padx=40, pady=20, command=lambda: add_input("4"))
button_4.grid(row=3, column=0)
button_5 = Button(calc, text="5", padx=40, pady=20, command=lambda: add_input("5"))
button_5.grid(row=3, column=1)
button_6 = Button(calc, text="6", padx=40, pady=20, command=lambda: add_input("6"))
button_6.grid(row=3, column=2)
right_brackets_button = Button(calc, text=")", padx=40, pady=20, command=lambda: add_input(")"))
right_brackets_button.grid(row=3, column=3)

button_1 = Button(calc, text="1", padx=40, pady=20, command=lambda: add_input("1"))
button_1.grid(row=4, column=0)
button_2 = Button(calc, text="2", padx=40, pady=20, command=lambda: add_input("2"))
button_2.grid(row=4, column=1)
button_3 = Button(calc, text="3", padx=40, pady=20, command=lambda: add_input("3"))
button_3.grid(row=4, column=2)
backspace_button = Button(calc, text="<-", padx=36, pady=20, command=lambda: add_input("bc"))
backspace_button.grid(row=4, column=3)

button_0 = Button(calc, text="0", padx=40, pady=20, command=lambda: add_input("0"))
button_0.grid(row=5, column=0)
dot_button = Button(calc, text=".", padx=41, pady=20, command=lambda: add_input("."))
dot_button.grid(row=5, column=1)
equal_button = Button(calc, text="=", padx=39, pady=20, command=calculate)
equal_button.grid(row=5, column=2)
clear_button = Button(calc, text="C", padx=39, pady=20, command=clear)
clear_button.grid(row=5, column=3)

calc.mainloop()
