from tkinter import *
from datetime import date

root = Tk()
root.title('getting started with widgets')
root.geometry('400x300')

lbl = Label(text="full name", bg="#3895D3")

name_lbl = Label(text="Full name", bg="#3895D3")
name_entry = Entry()

def display():
    name = name_entry.get()
    global Message
    message = "welcome to the application! \ntoday's date is: "
    greet = "Hello "+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3)

btn = Button(text="begin", command=display, height=1, bg="#1261A0", fg='white')

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()