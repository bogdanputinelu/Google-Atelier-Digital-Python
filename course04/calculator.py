from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry('500x354')
window.resizable(False, False)


def click(item):
    global expression
    expression += str(item)
    input_text.set(expression)


def delete():
    global expression
    expression = ''
    input_text.set("")


def equality():
    try:
        global expression
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except ZeroDivisionError:
        expression = ""
        input_text.set("Error! Please press C.")


expression = ""
input_text = StringVar()
input_frame = Frame(window, width=312, height=50)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack()

button_frame = Frame(window, width=500, height=304, bg="grey")
button_frame.pack()

Button(button_frame, text='C', width=48, height=3, bg='#eee', cursor='hand2', command=lambda: delete()).grid(row=0, column=0, columnspan=3)
Button(button_frame, text='/', width=20, height=3, bg='#FFA500', cursor='hand2', command=lambda: click('/')).grid(row=0, column=3)
Button(button_frame, text='7', width=15, height=3, bg='#eee', cursor='hand2', command=lambda: click('7')).grid(row=1, column=0)
Button(button_frame, text='8', width=15, height=3, bg='#eee', cursor='hand2', command=lambda: click('8')).grid(row=1, column=1)
Button(button_frame, text='9', width=15, height=3, bg='#eee', cursor='hand2', command=lambda: click('9')).grid(row=1, column=2)
Button(button_frame, text='*', width=20, height=3, bg='#FFA500', cursor='hand2', command=lambda: click('*')).grid(row=1, column=3)
Button(button_frame, text='4', width=15, height=3, bg='#eee', cursor='hand2', command=lambda: click('4')).grid(row=2, column=0)
Button(button_frame, text='5', width=15, height=3, bg='#eee', cursor='hand2', command=lambda: click('5')).grid(row=2, column=1)
Button(button_frame, text='6', width=15, height=3, bg='#eee', cursor='hand2', command=lambda: click('6')).grid(row=2, column=2)
Button(button_frame, text='-', width=20, height=3, bg='#FFA500', cursor='hand2', command=lambda: click('-')).grid(row=2, column=3)
Button(button_frame, text='1', width=15, height=3, bg='#eee', cursor='hand2', command=lambda: click('1')).grid(row=3, column=0)
Button(button_frame, text='2', width=15, height=3, bg='#eee', cursor='hand2', command=lambda: click('2')).grid(row=3, column=1)
Button(button_frame, text='3', width=15, height=3, bg='#eee', cursor='hand2', command=lambda: click('3')).grid(row=3, column=2)
Button(button_frame, text='+', width=20, height=3, bg='#FFA500', cursor='hand2', command=lambda: click('+')).grid(row=3, column=3)
Button(button_frame, text='0', width=31, height=3, bg='#eee', cursor='hand2', command=lambda: click('0')).grid(row=4, column=0, columnspan=2)
Button(button_frame, text='.', width=15, height=3, bg='#eee', cursor='hand2', command=lambda: click('.')).grid(row=4, column=2)
Button(button_frame, text='=', width=20, height=3, bg='#FFA500', cursor='hand2', command=lambda: equality()).grid(row=4, column=3)

window.mainloop()
