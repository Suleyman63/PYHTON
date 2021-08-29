import tkinter as tk

root = tk.Tk() # muss immer am Anfang initialisiert werden
root.title("Mein erstes Programm")
root.geometry("600x600") #absolute Pixel-Anggaben (Obacht bei Inhalten, die mehr Platz benötigen)

# Widgets:
# https://tkdocs.com/tutorial/widgets.html




# FARBEN
blau = "#405BE0"


def button_click():
    button_label = tk.Label(root, text = "Ich wurde erzeugt!")
    button_label.grid(row = 2, column = 0) 
    # bei jeder Erzeugung durch .grid() wird an gleicher Position im Programm das widget gezeichnet

    input = my_entry.get()
    print(input)
    my_entry.delete(0, tk.END) 
    my_entry.insert(0, "Klappte")
    my_entry.insert(3, "OOOOO")
    my_entry.delete(2, 5)

# Label
my_label = tk.Label(root, text = "Hello World!")
my_label2 = tk.Label(root, text = "Test ich bin auch noch da und etwas länger als du über mir")
my_test_label = tk.Label(root, text = "TEST TEST TEST", font = "Arial 20")

# Doku: System-Schriften abfragen ???

# Button
# mac: Hintergrund-Farbe: highlightbackground
my_button = tk.Button(root, text = "OOOOO", width = 7, bg = "red", fg = "white", command = button_click) 

# Entry

my_entry = tk.Entry(root, borderwidth = 3, font = "Verdana 14 bold", width = 5)

# Design-Hinweise
# padx/pady = Padding = Innenabstand 
# borderwidth = Rand-Stärke
# width / heigth rechnen nicht in pixel, sondern in Text-Zeichengröße (default: )

# Packing (unsere Widgets auf den root packen)
#.pack() fügt alle Widget nach und nach von oben nach unten hinzu
# .grid sorgt für Spalten- und Zeilen-Aufteilung (relativ zu einander!)
# es kann entweder .grid ODER .pack benutzt werden, nichts beides innerhalb des Skripts
#.place() kann auch mit pack/grid kombiniert werden

my_label.grid(row = 0, column = 0)
my_label2.grid(row = 0, column = 1)
my_button.grid(row = 1, column =  1) #columnspan ????
my_entry.grid(row = 1, column = 87)

my_test_label.place(x = 10, y = 300)


# sorgt dafür, dass das Programm auch läuft
# läuft auch weiter, wenn in der Console Fehler angezeigt werden
root.mainloop()