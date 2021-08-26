# Klassen - Attribute, Klassen-Variablen (nicht Instanzen!)

class Person:
    
    __personenanzahl = 0
    p_anzahl = 0
    
# diese Property ist eine Klassen-Property, nicht unterschiedlich für Instanzen
# durch Setzen eines __ findet encapsulation statt, heißt: INNERHALB meiner Unit (Klasse) kann manipuliert werden
# Zugriff nicht möglich
    
    def __init__(self, name):
        self.name = name
        Person.p_anzahl += 1
        Person.__personenanzahl += 1
    
    def gib_personenanzahl(self):
        return Person.__personenanzahl


p = Person("Herbert")
print(p.name)
print(p.p_anzahl)
print(p.__personenanzahl) ## durch __ kein Zugriff von AUSSEN!! möglich
print(p.gib_personenanzahl())

print(Person.p_anzahl) # direktes Auslesen OHNE Instanz möglich
print(Person.__personenanzahl) # von außen auch ohne Instanz KEIN Zugriff auf __ gesetzte properties


# Klassen - Methoden

class Mensch:
    
    anzahl = 0
    
    def __init__(self, name):
        self.name = name
        Mensch.erhohe_anzahl()
    
    @classmethod # Dekorator
    def erhohe_anzahl(cls): #Klassen-Methoden haben als default KEINEN Zugriff auf Klassen-Variablen
       cls.anzahl += 1 #nicht möglich: Mensch.anzahl



m1 = Mensch("Jo")
m2 = Mensch("Gabi")
m3 = Mensch ("Klaus")

print(m1.anzahl)