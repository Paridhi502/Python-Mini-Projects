from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("280x340")
root.resizable(0, 0)
root.configure(background="black")

e = Entry(root, width=16, font=('Arial', 20), borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

f_num = 0
math = ""

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
            e.insert(0, f_num + int(second_number))
    elif math == "subtraction":
            e.insert(0, f_num - int(second_number))
    elif math == "multiplication":
            e.insert(0, f_num * int(second_number))
    elif math == "division":
        if int(second_number) != 0:
            e.insert(0, f_num / int(second_number))
    else:
            e.insert(0, "Error")

btn_open_bracket = Button(text='(', height=2, width=5, fg='#000000', bg='#DCDCDC', font=('Arial', 10))
btn_open_bracket.grid(row=1, column=0, pady=5)

btn_close_bracket = Button(text=')', height=2, width=5, fg='#000000', bg='#DCDCDC', font=('Arial', 10))
btn_close_bracket.grid(row=1, column=1, pady=5)

btn_percent = Button(text='%', height=2, width=5, fg='#000000', bg='#DCDCDC', font=('Arial', 10))
btn_percent.grid(row=1, column=2, pady=5)

btn_ac = Button(text='AC', height=2, width=5, fg='#000000', bg='#DCDCDC', font=('Arial', 10), command=button_clear)
btn_ac.grid(row=1, column=3, pady=5)

btn7 = Button(text='7', height=2, width=5, fg='#000000', bg='#DCDCDC', font=('Arial', 10), command=lambda: button_click(7))
btn7.grid(row=2, column=0, pady=5)

btn8 = Button(text='8', height=2, width=5, fg='#000000', bg='#DCDCDC', font=('Arial', 10), command=lambda: button_click(8))
btn8.grid(row=2, column=1, pady=5)

btn9 = Button(text='9', height=2, width=5, fg='#000000', bg='#DCDCDC', font=('Arial', 10), command=lambda: button_click(9))
btn9.grid(row=2, column=2, pady=5)

btndiv = Button(text=chr(247), height=2, width=5, fg='#000000', bg='#DCDCDC', font=('Arial', 10), command=button_divide)
btndiv.grid(row=2, column=3, pady=5)

btn4 = Button(text='4', height=2, width=5, fg='#000000', bg='#DCDCDC', font=('Arial', 10), command=lambda: button_click(4))
btn4.grid(row=3, column=0, pady=5)

btn5 = Button(text='5', height=2, width=5, fg='#000000', bg='#DCDCDC', font=('Arial', 10), command=lambda: button_click(5))
btn5.grid(row=3, column=1, pady=5)

btn6 = Button(text='6', height=2, width=5, fg='#000000', bg='#DCDCDC', font=('Arial', 10), command=lambda: button_click(6))
btn6.grid(row=3, column=2, pady=5)

btnmul = Button(text='x', height=2, width=5, fg='#000000', bg='#DCDCDC', font=('Arial', 10), command=button_multiply)
btnmul.grid(row=3, column=3, padx=5, pady=5)

btn1 = Button(text='1', height=2, width=5, fg='#000000', bg='#DCDCDC', font=('Arial', 10), command=lambda: button_click(1))
btn1.grid(row=4, column=0, pady=5)

btn2 = Button(text='2', height=2, width=5, fg='#000000', bg='#DCDCDC', font=('Arial', 10), command=lambda: button_click(2))
btn2.grid(row=4, column=1, pady=5)

btn3 = Button(text='3', height=2, width=5, fg='#000000', bg='#DCDCDC', font=('Arial', 10), command=lambda: button_click(3))
btn3.grid(row=4, column=2, pady=5)

btnsub = Button(text='-', height=2, width=5, fg='#000000', bg='#DCDCDC', font=('Arial', 10), command=button_subtract)
btnsub.grid(row=4, column=3, pady=5)

btn0 = Button(text='0', height=2, width=5, fg='#000000', bg='#DCDCDC', font=('Arial', 10), command=lambda: button_click(0))
btn0.grid(row=5, column=0, pady=5)

btndot = Button(text='.', height=2, width=5, fg='#000000', bg='#DCDCDC', font=('Arial', 10), command=lambda: button_click('.'))
btndot.grid(row=5, column=1, pady=5)

btnequal = Button(text='=', height=2, width=5, fg='#000000', bg='#1E90FF', font=('Arial', 10), command=button_equal)
btnequal.grid(row=5, column=2, pady=5)

btnadd = Button(text='+', height=2, width=5, fg='#000000', bg='#DCDCDC', font=('Arial', 10), command=button_add)
btnadd.grid(row=5, column=3, pady=5)

root.mainloop()
