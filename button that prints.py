from tkinter import*
root=Tk()

def myclick():
    myLabel=Label(root, text="This is that"+e.get())
    myLabel.pack()


e=Entry(root, width=50, fg="blue", bg="red")
e.pack()
e.insert(2, "This is not what you think it is")

myButton2=Button(root, text="Enter and click!", state=ACTIVE, padx=30, pady=30, command=myclick, fg="blue", bg="red")



myButton2.pack()


root.mainloop()