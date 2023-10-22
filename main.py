from tkinter import*
root=Tk()

def myclick():
    myLabel=Label(root, text="Hi. You clicked me")
    myLabel.pack()


myLindros=Label(root, text="Hello from Mars!", font=("Arial Bold", 12))
myLindros2=Label(root, text="Hello from Uranus!", font=("Arial", 25))
myLindros3=Label(root, text="Hello from Venus!", font=("Times new roman", 17))
myButton=Button(root, text="This is my first button!")
myButton2=Button(root, text="This is my second button!", state=ACTIVE, padx=30, pady=30, command=myclick)



myLindros.grid(row=4, column=5)
myLindros2.grid(row=6, column=8)
myLindros3.grid(row=10, column=9)
myButton.grid(row=20, column=20)
myButton2.pack()


root.mainloop()