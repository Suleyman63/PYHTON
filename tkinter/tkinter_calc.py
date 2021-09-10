from tkinter import *
from tkinter import messagebox


root = Tk()
# root- Konfiguration
root.title("Einfacher Rechner")
root.resizable(False, False) # True/False
#root.geometry("300x300")
root.iconbitmap("favicon.ico") #mac-favicon???????????????????????????????????????


# Variablen
LIGHTGREEN = '#d3f5dc'

root.configure(background = LIGHTGREEN)

# Funktionen

def button_click(number):
    entry_bar.insert(END, str(number))

def button_plus():
    global f_num
    if entry_bar.get() != "":
        f_num = int(entry_bar.get())
        print(f_num)
        entry_bar.delete(0, END)
    else: 
        print("keine Zahl in Entry-Bar")


def button_clear():
    global f_num

    # hier: messagebox-Abfrage

    is_clear_ok = messagebox.askyesno("Clear?", "Soll Inhalt gelöscht werden?") # Titel des Messagebox-Fensters, eigentlicher Inhalt
    if is_clear_ok:
        entry_bar.delete(0, END)
    # vereinfacht: 
    # if messagebox.askyesno("Clear?", "Soll Inhalt gelöscht werden?"):
    #    entry_bar.delete(0, END)


def button_istgleich():
    global f_num
    s_num = int(entry_bar.get())
    entry_bar.delete(0, END)
    ergebnis = f_num + s_num
    entry_bar.insert(0, str(ergebnis)) #insert "ähnlich" wie print akzeptiert auch z.B. Additionen 
    f_num = 0

  
    # holt sich f_num und addiert mit aktuellen Wert
    # entry_bar clear
    # entry bar zeigt ergebnis

def callback(event):
    button_clear()

# Widgets

entry_bar = Entry(root, width = 15, borderwidth=5, font ="Arial 16 bold", justify = RIGHT) # Höhe meiner Entry-Box über die Schrift-Größe
root.bind("<Delete>", callback)

# root-Binding ist quasi "immer" aufrufbar
# Binding auch mit Widgets möglich 
# https://www.pythontutorial.net/tkinter/tkinter-event-binding/ 
# Liste mit Events, Tasten-Drucke

btn1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
btn2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
btn3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
btn4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
btn5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
btn6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
btn7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
btn8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
btn9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))
btn0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))

btn_plus = Button(root, text = "+", padx = 39, pady = 20, command = lambda: button_plus())
btn_istgleich = Button(root, text = "=", command = lambda: button_istgleich())
btn_clear = Button(root, text = "Clear", padx = 79, pady = 20, command = lambda: button_clear())
# es folgt noch: pixelrücken (wenn nicht mit sticky oder generellem responsiven Design)

# Packing
# GRID (auch über die Funktion .place(x,y) möglich, um pixelgenau zu platzieren
# button on screen
#    0 1 2

# 0  [   ]
# 1  7 8 9
# 2  4 5 6
# 3  1 2 3
# 4  0 C C
# 5  + = =


entry_bar.grid(row = 0, column = 0, columnspan = 3)
btn7.grid(row = 1 , column = 0) # hier natürlich auch sticky möglich
btn8.grid(row = 1, column = 1)
btn9.grid(row = 1, column = 2)

btn4.grid(row = 2, column = 0)
btn5.grid(row = 2, column = 1)
btn6.grid(row = 2, column = 2)

btn1.grid(row = 3, column = 0)
btn2.grid(row = 3, column = 1)
btn3.grid(row = 3, column = 2)

btn0.grid(row = 4, column = 0)
btn_clear.grid(row = 4, column = 1, columnspan = 2)

btn_plus.grid(row = 5, column = 0)
btn_istgleich.grid(row = 5, column = 1, columnspan=2, sticky = "nsew")



root.mainloop()