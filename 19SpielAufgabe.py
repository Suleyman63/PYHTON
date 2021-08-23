"""
Gruppenarbeit Text-Adventure (idR 3 TN pro Gruppe)

1) gemeinsame Ausarbeitung Ideenfindung, zB Insel, Stadt, Planet, etc.
2) Einleitungstext (print)
3) Usernamen abfragen und weiterverarbeiten, zB für Begrüßung
4) Hero und evtl. Feinde (Liste) erzeugen mit Lebenspunkten/HP (Zufall)
5) Inventar für Hero erstellen mit 1-2 Gegenständen
6) Spiel-Schleife implementieren (while)
7) per Tastatur (input) erlauben: N, O, S, W, I, B (if, elif, else)
(Norden, Osten, Süden, Westen, Inventar (zeigen per Schleife oder direkte Ausgabe mit []), Beenden (um Spiel-Schleife zu verlassen))
8) für alle Befehle vom User, zB N(orden) dort etwas machen, zB gegen einen
Gegner kämpfen und HP abziehen oder einen Gegenstand finden im S(üden)
Also: seid kreativ! :)
9) Gegenstand aus Inventar benutzen

BONUS: gerne auch dict einsetzen zB für die Enemies und dem Inventar

Viel Spaß und Erfolg! Gemeinsame Besprechung ab: 15:00

#
# Musterlösung (Grundgerüst) Text-Adventure
#

# https://gist.github.com/cimpython/edd4063cf733cb630bf5f57e43a30367

# Ziel: ein Grundgerüst für ein text basiertes Adventure-Spiel für die Konsole
# User trifft Entscheidungen per Tastatur, um seine Spielfigur zu steuern
# https://miro.medium.com/max/639/1*aEACsaZYpdA45Ddf5s9cVg.png

"""
# Module einbinden bzw. importieren (u.a. random für Zufallszahlen)
import random

#
# Initialisierung
#

# Feind erzeugen bzw. Enemy
enemy = "Riesen-Python"
# alternativ eine Feindliste
enemies = ["Drache Egon", "Ritter Siegfried", "Zauberer", "Wolf"]

# Inventar Hero
inventar = ["Holzschwert", "Apfel", "Goldener Schlüssel"]

# zufällige Gegenstände
items = ["Rubin", "Smaragd", "Ring", "Apfel"]

# Lebenspunkte (HealthPoint bzw. hp) mit Startwert von 100
hero_hp = 100
enemy_hp = 100
enemies_hp = [100, 90, 110, 60]

#
# Intro / Einleitungstext
#

# Haupt-Figur erzeugen (Held / Hero)
# Namen der Figur vom User erzeugen lassen per input
hero = input("Wie heißt Du denn? ")

print("Willkommen auf der Schlangen-Insel,", hero)

#
# Game-Loop
#

while True:
    
    eingabe = input("(N)ord, (O)st, (S)üd, (W)est oder (I)nventar oder Spiel (B)eenden: ")
    #print("Input:", eingabe) # Testausgabe
    
    # Spiel beenden?
    if eingabe.upper() == "B":
        
        #print("Spiel beenden")
        
        # Check, Sicherheitsabfrage User
        eingabe = input("Bist Du sicher? (J)a / (N)ein: ")
        if (eingabe.upper() == "J"):
            print("Schade - bis bald!")
            # per break die Game-Loop verlassen
            break
        else:
            print("Schön dass Du noch etwas auf der Insel verweilst.")
    
    # in eine bestimmte Richtung gehen?
    
    elif eingabe.upper() == "N":
        
        print("Du gehst nach Norden.")
        
        # Einen Kampf simulieren mit einem Gegner (hier: Riesen-Python)
        print("Du befindest Dich in einem Kampf mit:", enemy)

        # per Zufall Zahlen "würfeln", die bestimmen, wie stark jemand verletzt wurde
        # quasi eine kleine Kampf-Simulation
        # Ziel: zufällige Treffer-Punkte abziehen von Lebenspunkten
        hero_trefferpunkte = random.randrange(0, 11) # Zahl zwischen 0 bis 10
        enemy_trefferpunkte = random.randrange(0, 11)

        # Trefferpunkte von Hero-HP abziehen
        #hero_hp -= enemy_trefferpunkte
        hero_hp = hero_hp - enemy_trefferpunkte

        # Trefferpunkte von Enemy-HP abziehen
        enemy_hp -= hero_trefferpunkte

        print("Aktuelle Hero-HP:", hero_hp)
        print("Aktuelle Enemy-HP:", enemy_hp)
                
    elif eingabe.upper() == "O":
        
        print("Du gehst nach Osten.")
        
        # zufälliger Gegenstand:
        random_item = random.choice(items)
        print("Dort findest Du:", random_item)
        inventar.append(random_item)
        print("Du nimmst", random_item, "mit.")
        
    elif eingabe.upper() == "S":
        
        print("Du gehst nach Süden.")
        
        print("Du bist hungrig und schaust nach einem Apfel.")
        # Check, ob Apfel im Inventar
        if "Apfel" in inventar:
            inventar.remove("Apfel")
            print("Das tat gut!")
            hero_hp += 5
            print("Deine HP betragen nun:", hero_hp)
        else:
            print("Schade - leider hast Du keinen mehr dabei.")
        
    elif eingabe.upper() == "W":
        
        print("Du gehst nach Westen.")
        print("Im Westen nichts Neues.")
        
    # ins Inventar schauen
    elif eingabe.upper() == "I":
        print("Du schaust ins Inventar - dort befinden sich:")
        for item in inventar:
            print("\t- ", item)
        
    # Alternative (wenn ungültige Befehle wie zB "T")
    else:
        print("Ich habe das nicht verstanden.")