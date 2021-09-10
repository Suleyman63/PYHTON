import tkinter
from tkinter.constants import GROOVE, LEFT
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("TO-DO LIST")
root.geometry('450x450')


def add_fonk():
    fonk = entry.get()
    if fonk != "":
      listbox.insert(tkinter.END, fonk)
      entry.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(message='warning')


def delete_fonk():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except:
        tkinter.messagebox.showwarning(message='warning')



def read_fonk():
    try:
        with open('todo.txt', 'r') as f:
            content = f.read()
            for i in content:
             print(i)
    except:
        tkinter.messagebox.showwarning(message='Warning')


def write_fonk():
    try:
        with open('todo.txt', 'w') as f:
            content = f.write()
            for i in content:
             print(i)
    except:
        tkinter.messagebox.showwarning(message='Warning')



frame = tkinter.Frame(root)
frame.pack()


listbox = tkinter.Listbox(frame, height=10, width=55)
listbox.pack(side=tkinter.LEFT)




entry = tkinter.Entry(root, width=42, font=("times new roman", 12, "bold"), bd=5, relief=GROOVE)
entry.pack()

btn_add = tkinter.Button(root, text='ADD', width=48, pady=10, command=add_fonk)
btn_add.pack()

btn_delete = tkinter.Button(root, text='DELETEE', pady=10, width=48, command=delete_fonk)
btn_delete.pack()

btn_load = tkinter.Button(root, text='LOAD', pady=10, width=48, command=write_fonk)
btn_load.pack()

btn_save = tkinter.Button(root, text='SAVE', pady=10, width=48, command=write_fonk)
btn_save.pack()

root.mainloop()

