"""
 Erstelle 2 Dictionairies, monster und helden nach dem Muster "name" : ["Stärke1", "Stärke2"] etc

 Erstelle 3 Funktionen: is_gewinner() , kampf() und auswahl() (mögliche Paramter der 3 Funktionen sind selbst zu wählen)

 is_gewinner() gibt Trueoder False zurück (optional noch Erklärungstext, der Schwächen und Stärken auflistet)

 auswahl() lässt via print() alle möglichen Helden und deren Stärken ausgeben und ordnet diesen eine Zahl zu, 
 sodass der User via input() einen Held via Zahl wählen kann, Bsp: (0): Ritter, Stärke ["Mut"] etc. Die Funktion gibt den input()zurück.

 kampf() schickt den ausgewählten Helden in die is_gewinner()-Funktion und gibt via print()aus, 
 ob der Kampf verloren oder gewonnen wurde. (Hinweis: Zugriff auf ein Dictionairy mit index-Integer nicht möglich, der return-Wert der auswahl()-Funktion muss also umgewandelt werden)

 Erstelle einen GameLoop mit einer while-Schleife inkl. Beenden-Funktion

 Der Loop folgt immer > auswahl() > kampf() > prüfen, ob noch ein Kampf oder Abbruch


 """

import random
import sys



wahl = int(input('NUMMER AUSWÄHLEN\n1 - HELDEN\n2 - MONSTER\n3 - EXIT'))


def auswahlen():

    if wahl == 1:
      print('du hat HELDEN ausgewahlt')
    elif wahl == 2:
        print('du hat MONSTER ausgewahlt')
    else: print('EXIT')
    


def kampf():
    
    print('*************************************************')
    helden_names = ["Albert", "Charles", "Nicolas", "Michael", "Anders", "Isaac", "Stephen", "Marie", "Richard"]
    monster_names = ["Einstein", "Darwin", "Copernicus", "Faraday", "Celsius", "Newton", "Hawking", "Curie","Dawkins"]
    return "{} gegen {}".format(random.choice(helden_names), random.choice(monster_names))

for i in range(5):
    print(kampf())


    
def is_gewinner(helden_names, monster_names):
    for h in helden_names:
        print(h)
        for m in monster_names:
            print(m)
    if monster_names == 0:
        print('HELDEN TEAMS HAT GEWONNEN')
    else: print('MONSTER TEAM HAT GEWONNEN')     
    
    
def finisch():
    print('Exit...')
    sys.exit()



"""
# Zusammenlosung
import random

is_kampfbereit = True
monster = {

# Schwäche
    "Ork" : ["Stärke", "Magie"],
    "Drache" : ["Magie"],
    "Skelett" :["Wasser"],
    "Schlange" : ["Stärke"]
}

helden = {
# Stärken
    "Ritter" : ["Stärke"],
    "Zauberer" : ["Magie"],
    "Aquaman" : ["Wasser"],
    "Assasine" : ["Stärke", "Magie"]
}


def is_gewinner(h):

    m = random.choice(list(monster))

    print(f"Es kämpft >{h}< mit Stärke(n): {helden[h]} gegen >{m}< mit Schwäche(n): {monster[m]}!")

    #for (Liste Stärken des Helden) in "Assasine"
    for stark in helden[h]:
        if stark in monster[m]:
            print(f"{stark} befindet sich in {monster[m]}")
            return True
        else:
            print(f"{stark} nicht in {monster[m]}, Monster gewinnt!")
            return False

def kampf(held):
    if is_gewinner(held):
        print("Gewonnen!")
    else:
        print("Verloren")


def auswahl():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("WILLKOMMEN in der KAMPFARENA! \n Bitte wähle deinen Helden:")
    auswahl = 0
    for i, j in helden.items():
        print(f"({auswahl}): {i}, Stärke: {j}")
        auswahl += 1
   
    eingabe = int(input("Zahl bitte: "))
    return eingabe

# print(*helden["Ritter"], sep =", ") # mit * unpacking in St

# GAMELOOP
while is_kampfbereit:
    helden_liste = list(helden)
    held = helden_liste[auswahl()]
    kampf(held)
    is_kampfbereit = int(input("Noch einen Kampf? 0 = NEIN, 1 = JA "))
else:
    print("Vielen Dank für den Kampf!")
"""
