import tkinter as tk
import tkinter.font as font # wird benötigt, um font-Funktionalitäten zu erhalten
import random

root = tk.Tk()
root.geometry("300x400")

# Variablen Deklaration 
label_list = []
count = -1

img_add = tk.PhotoImage(file = "add.png") #JPG vs JPEG vs jpg vs jpeg
img_python = tk.PhotoImage(file = "py.png")

img_add_klein = img_add.subsample(20)
img_python_klein = img_python.subsample(2) # Argument X und Y, wenn nur ein Argument, dann gilt es für beide, # subsampling : Bild-Größe geteilt durch Argument-Zahl


# Font-Deklaration, um sie in den Buttons nutzen zu können

button_font = font.Font(family = "MV Boli", size = 16, weight = "bold") #Bsp.: Argumente: Font-Family, size und weight
# wenn family kein valider Wert ist (z.B. Schreibfehler), dann wird font auf default Font gesetzt (tkinter stürzt nicht ab :-) )

#print(font.families()) # gibt in der Konsole alle nutzbaren System-Fonts aus

# Funktionen

def add_label():
    global count, label_list

    border_list=["raised", "sunken", "flat", "ridge", "solid", "groove"]  #mögliche border-Layouts
    border = random.choice(border_list)

    label_list.append(tk.Label(root, text=f"Ich wurde hinzugefügt, {border}", bg = "green", fg = "white", borderwidth = 2, relief = border))
    count += 1

    label_list[count].pack(fill = tk.BOTH, expand = 1)

    print(len(label_list), label_list)



def del_label():
    global label_list, count

    if len(label_list) > 0:
        label_list[count].destroy() # destroy() entfernt die Instanz endgültig, oder pack_forget() -> wird vom root genommen, kann aber wieder ge-pack-t werden

        label_list.pop() #.pop() löscht (wenn kein Argument mitggeeben ist) das letzte Element einer Liste //löschen aus Liste trotz destroy?
        count -= 1 
        print(len(label_list), label_list)
        
    else:
        print("Keine Labels mehr zum Löschen")

# Widgets

img_label = tk.Label(root, image = img_python_klein)

btn1 = tk.Button(root, text = "Label hinzufügen", image = img_add_klein, compound=tk.LEFT,  font = button_font, bg = "green", command = add_label)
btn2 = tk.Button(root, text = "Lösch aktuellstes Label", bg='red', fg='#ffffff', command = del_label)

# Packing

img_label.pack()
btn1.pack(fill = tk.BOTH, expand = 1) #möglich: BOTH (X und Y) oder nur horizontal(tk.X) oder vertikal (tk.Y) großgeschrieben, keine kleinen x oder y
btn2.pack(fill = tk.BOTH, expand = 1)
