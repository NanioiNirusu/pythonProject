from tkinter import*
root = Tk()


x = ""
outerResult=""

class MyButton:
    def __init__(self, root, text, command,padx=60, pady=30, width=1, height=1,):
        self.button = Button(root, text=text, padx=padx, pady=pady,width=width, height=height, command=command)
    def grid(self, row, column):
        self.button.grid(row=row, column=column)

def update_entry(value):
    global x
    print(x)
    global outerResult
    print(outerResult)
    print()
    if  x==outerResult and value=="*" or value== "/" or value =="+" or value== "-":
        x = str(x) + str(value)
        e.delete(0, END)
        e.insert(0, x)
    elif x==outerResult and 0<=value>=9:
        x = str(value)
        e.delete(0, END)
        e.insert(0, x)

    else :
        x = str(x) + str(value)
        e.delete(0, END)
        e.insert(0, x)

def clear_entry():
    global x
    x = ""
    e.delete(0, END)

def evaluate_expression():
    global x
    global outerResult
    result = eval(x)
    e.delete(0, END)
    e.insert(0, result)
    x = result
    outerResult=result


e=Entry(width=50, font=("Arial", 15))
e.grid(row=0, column=0, columnspan=4)



myButton7 = MyButton(root, "7", lambda: update_entry(7))
myButton8 = MyButton(root, "8", lambda: update_entry(8))
myButton9 = MyButton(root, "9", lambda: update_entry(9))
myButtonX = MyButton(root, "*", lambda: update_entry("*"))
myButton4 = MyButton(root, "4", lambda: update_entry(4))
myButton5 = MyButton(root, "5", lambda: update_entry(5))
myButton6 = MyButton(root, "6", lambda: update_entry(6))
myButtonMinus = MyButton(root, "-", lambda: update_entry("-"))
myButton1 = MyButton(root, "1", lambda: update_entry(1))
myButton2 = MyButton(root, "2", lambda: update_entry(2))
myButton3 = MyButton(root, "3", lambda: update_entry(3))
myButtonPlus = MyButton(root, "+", lambda: update_entry("+"))
myButton0 = MyButton(root, "0", lambda: update_entry(0))
myButtonDivide = MyButton(root, "/", lambda: update_entry("/"))
myButtonClear = MyButton(root, "Clear",  lambda: clear_entry())
myButtonEqual = MyButton(root, "=", lambda: evaluate_expression())


myButton7.grid(row=1, column=0)
myButton8.grid(row=1, column=1)
myButton9.grid(row=1, column=2)
myButtonX.grid(row=1, column=3)
myButton4.grid(row=2, column=0)
myButton5.grid(row=2, column=1)
myButton6.grid(row=2, column=2)
myButtonMinus.grid(row=2, column=3)
myButton1.grid(row=3, column=0)
myButton2.grid(row=3, column=1)
myButton3.grid(row=3, column=2)
myButtonPlus.grid(row=3, column=3)
myButton0.grid(row=4, column=0)
myButtonDivide.grid(row=4, column=1)
myButtonClear.grid(row=4, column=2)
myButtonEqual.grid(row=4, column=3)




root.mainloop()