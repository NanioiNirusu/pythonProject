from tkinter import*
root = Tk()


x = ""

def update_entry(value):
    global x
    x = str(x) + str(value)
    e.delete(0, END)
    e.insert(0, x)

def clear_entry():
    global x
    x = ""
    e.delete(0, END)

def evaluate_expression():
    global x
    result = eval(x)
    e.delete(0, END)
    e.insert(0, result)
    x = result


e=Entry(width=50, font=("Arial", 15))
e.grid(row=0, column=0, columnspan=4)



myButton7 = Button(root, text="7",padx=60, pady=30, command=lambda: update_entry(7))
myButton8 = Button(root, text="8",padx=60, pady=30, command=lambda: update_entry(8))
myButton9 = Button(root, text="9",padx=60, pady=30, command=lambda: update_entry(9))
myButtonX = Button(root, text="*",padx=60, pady=30, command=lambda: update_entry("*"))
myButton4 = Button(root, text="4",padx=60, pady=30, command=lambda: update_entry(4))
myButton5 = Button(root, text="5",padx=60, pady=30, command=lambda: update_entry(5))
myButton6 = Button(root, text="6",padx=60, pady=30, command=lambda: update_entry(6))
myButtonMinus = Button(root, text="-",padx=60, pady=30, command=lambda: update_entry("-"))
myButton1 = Button(root, text="1",padx=60, pady=30, command=lambda: update_entry(1))
myButton2 = Button(root, text="2",padx=60, pady=30, command=lambda: update_entry(2))
myButton3 = Button(root, text="3",padx=60, pady=30, command=lambda: update_entry(3))
myButtonPlus = Button(root, text="+",padx=60, pady=30, command=lambda: update_entry("+"))
myButton0 = Button(root, text="0",padx=60, pady=30, command=lambda: update_entry(0))
myButtonDivide = Button(root, text="/",padx=60, pady=30, command=lambda: update_entry("/"))
myButtonClear = Button(root, text="Clear",padx=60, pady=30,width=1, height=1, command=lambda: clear_entry())
myButtonEqual = Button(root, text="=",padx=60, pady=30, command=lambda: evaluate_expression())


myButton7.grid(row=1, column=0, columnspan=1)
myButton8.grid(row=1, column=1, columnspan=1)
myButton9.grid(row=1, column=2, columnspan=1)
myButtonX.grid(row=1, column=3, columnspan=1)
myButton4.grid(row=2, column=0, columnspan=1)
myButton5.grid(row=2, column=1, columnspan=1)
myButton6.grid(row=2, column=2, columnspan=1)
myButtonMinus.grid(row=2, column=3, columnspan=1)
myButton1.grid(row=3, column=0, columnspan=1)
myButton2.grid(row=3, column=1, columnspan=1)
myButton3.grid(row=3, column=2, columnspan=1)
myButtonPlus.grid(row=3, column=3, columnspan=1)
myButton0.grid(row=4, column=0, columnspan=1)
myButtonDivide.grid(row=4, column=1, columnspan=1)
myButtonClear.grid(row=4, column=2, columnspan=1)
myButtonEqual.grid(row=4, column=3, columnspan=1)




root.mainloop()