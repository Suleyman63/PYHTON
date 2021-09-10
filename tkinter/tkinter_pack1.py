import tkinter as tk
root = tk.Tk()
root.geometry("400x600")
root.title("2btns, flow design")

label_list =[]
count = 0

# dynamische Label-Variable

labeltext = tk.StringVar()
labeltext.set("Ich bin ein Label" + str(count))

# Funktionen
def button_click():
    global count, label_list, labeltext

    # Widget - Erstellung
    my_label = tk.Label(root, textvariable = labeltext, bg = "red", fg ="white", borderwidth = 2, relief = "solid") 

    my_label.pack(side = tk.BOTTOM, ipadx = 15, ipady = 5) #padx
    label_list.append(my_label)
    print(label_list)
    count += 1
    labeltext.set("Ich bin ein Label" + str(count))

    #Whenever there is a change in a tkinter variable, the update is automatically reflected everywhere(!).  When the variable changes, the text of the widget changes as well.

# Widgets
btn1 = tk.Button(root, text = "Click1", command = button_click)
btn2 = tk.Button(root, text = "Click2", command = button_click)

# Packing
btn1.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1) # 1 = True, 0 = False
btn2.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)

root.mainloop()