import tkinter as tk
import tkinter.font as font # wird benötigt, um font-Funktionalitäten zu erhalten


root = tk.Tk()
root.geometry("300x400")

# GRID Konfiguration

# ROWs konfigurieren
root.grid_rowconfigure(0, weight = 1)
root.grid_rowconfigure(1, weight = 1)

#COLUMNs konfigurieren
root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)


# Variablen Deklaration 
label_list = []
count = -1

button_font = font.Font(family="Sitka Display", size = 20, weight = "bold")
label_font = font.Font(family = "Arial", size = 12)
# wenn Fonts fehlerhaft (z.B. Rechtschreibfehler) dann wird automatisch auf default gesetzt 

# Funktionen
def add_label():
    global count, label_list

    label_list.append(tk.Label(root, text = "Ich bin das Label mit einem langen Text", bg = "red",  fg = "white", borderwidth = 2, font = label_font))
    count += 1
    label_list[count].grid(row = 2, column = 0, columnspan = 2,  ipadx = 10)
    # Auch möglich: erst Index mit count auslesen, dann inkrementieren
    print(len(label_list), label_list)

def del_label():
    global label_list, count

    if len(label_list) > 0:
        label_list[count].grid_forget() # destroy() entfernt die Instanz endgültig, oder grid_forget() -> wird vom root genommen, kann aber wieder ge-pack-t werden

        label_list.pop() #.pop() löscht (wenn kein Argument mitggeeben ist) das letzte Element einer Liste //löschen aus Liste trotz destroy?
        count -= 1 
        print(len(label_list), label_list)
        
    else:
        print("Keine Labels mehr zum Löschen")

def change_btn_text():
    # ohne globale Referenz des btn1 ist Lesen & Manipulieren möglich
    button_text_vorher = btn1["text"]
    print("Mein Button-Text war vorher: ", button_text_vorher)
    btn1["text"] = "Check!"
    btn1["fg"] = "red"
    btn1["command"] = test # auch Neu-Zuweisung der command-Funktion möglich

def test():
    print("Ich funktionierte!")

def print_parameter(wort):
    print("An mich wurde erfolgreich übermittelt: ", wort)
    entry.delete(0, tk.END)

# Widgets

btn1 = tk.Button(root, text ="add label", command = add_label)
btn2 = tk.Button(root, text ="del label", command = del_label)
btn3 = tk.Button(root, text ="wechsel Text von button1", font= button_font, command = change_btn_text)
btn4 = tk.Button(root, text = "Ich übergebe das Wort aus dem Entry", command = lambda: print_parameter(entry.get())) 
entry = tk.Entry()


#Syntax:  lambda: operation
# lambda -Funktionen sind anonyme Funktionen und besitzen keinen Funktionsnamen. Sie werden während der runtime erstellt, ausgeführt und direkt gelöscht. 

# hier evtl noch 1-2 Zeilen UND mini-beispiele zu lambda- Funktionen

# Packing (diesmal: GRID Geometry)
#    0    1 
# 0 [  ] [  ]
# 1 [       ]
# 2 < L     >
# 3 [ TE BTN]


btn1.grid(row = 0, column = 0, sticky = "nsew") # north eas south west , es geht als Beispiel auch: ns, sw etc
btn2.grid(row = 0, column = 1, sticky = "nsew")
btn3.grid(row = 1, column = 0, columnspan = 2, sticky = "nsew")
btn4.grid(row = 3, column = 0)
entry.grid(row = 4, column = 0)

#mainloop
root.mainloop()