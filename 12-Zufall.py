# Spielwiese als Einführung für Zufallszahlen

import random

#print("")
#len
#input

# Würfel von 1 bis 6
# Return random integer in range [a, b], including both end points.
zahl = random.randint(1, 6)
print(zahl)

print("Willkommen auf der Schlangeninsel")
hero = input("Wie heißt Du denn? ")
print("Sei gegrüßt", hero)

# Lebenspunkte / HP
hero_hp = random.randint(80, 100)
print("Deine aktuellen HP:", hero_hp)

# Inventar
inventar = ["Holzschwert", "Apfel", "Goldener Schlüssel"]

# Gegner
enemies = ["Drache Egon", "Schlange Lisa", "Ritter Siegfried III."]

print("In Deinem Inventar befinden sich:", inventar)
print("Zufälliger Gegenstand:", random.choice(inventar))
print("Zufälliger Gegner:", random.choice(enemies), "HP:", random.randint(70, 110))






