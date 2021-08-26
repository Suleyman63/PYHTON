# procedural programming : Programm als Set von Funktionen
# Nachteil: Spagetthi Code, große Abhängigkeiten von Funktionen (Funktionen rufen andere Funktionen auf etc)
# simple, zielgerichtet schnell Probleme lösen, kleine Skripts schreiben etc

# OOP: Object oriented programming
# Objekt Auto (Eigenschaften: Marke, Farbe, tempo_max: PROPERTIES // start_motor(), drive() Methoden (Funktionen eines Objekts)
# localStorage (property: length, clear_memory(), remove_item()))

# Pillar (SÄULE!!)
# 1) Encapsulation (group related functions and variables togehter)
# In Python, there is no existence of Private instance variables that cannot be accessed except inside a class.
# However, to define a private member prefix the member name with double underscore “__”. group
# bisher Funktion(parameter, paramter2), in OOP: bei Methoden-Aufruf werden Paramter minimiert oder ganz weggelassen
# 'the best functions are those with no paramters' (Robert Martin)

# 2) Vererbung (Inheritance)
# Tierwelt , Objekt: TIER (Properties: gewicht, name, Methode: gib_laut() ) -> dann kann eine Instanz erzeugt
# Sub-Klassen können Eigenschaften (Properties&Methoden) der Ober-Klasse (upper_class, super-Klasse) ERBEN
# Beispiel VÖGEL : in OOP kann ich ein Objekt "VOGEL" mithilfe der Vererbunf der Klasse TIER erzeugen
# je größer die Anzahl der Sub-Klassen, desto detailreicher die Properties& Methoden


# UPPER (Super)-Klasse: VEHICLE (tempo, drive() )
# SUB-Klasse: Boot (erbt alle Properties & Methoden von VEHICLE) + bekommt hinzu: hat_segel, hat_steuerboard
# Sub-Klasse Auto (erbt alle Properties & Methoden von VEHICLE) + bekommt hinzu: motor_ps, drive_durch_wald() )
# Sub-Sub-Klass: LKW (erbt alle Properties & Methoden von VEHICLE + Auto) und bekommt hinzu: is_waldarbeiter_auto

# Blaupause / blue print: man beschreibt ERST das Objekt und erzeugt dann eine INSTANCE davon

# Pillar 3 & 4: Abstraction , Polymorphism


class Katze: #CamelCase (kein snake_case) (nicht myCLass, sondern MyClass)
    
    def miauen(self):
        print("Miau!")
    
    def addieren(self, x):
        return x + 1
    
# nachdem!() ein bluePrint beschrieben wurde, kann eine Instanz dieser Klasse erzeugt werden

katze = Katze()
timmi = Katze()
miezman = timmi
print(type(miezman))
miezman.miauen()

print(katze.addieren(5))
timmi.miauen()

###### 

class Lehrer: 
    
    def __init__(self, name, alter): # Konstruktor UND wird immer direkt beim Erzeugen einer Instanz aufgerufen
        self.name = name
        self.alter = alter
        print("Mein Name ist:", self.name)
        print("Ich bin Jahr alt: ", self.alter)
        
        
    def sag_meinen_namen(self):
        return self.name

    def add_fach(self, fach):
        self.fach = fach

lehrer1 = Lehrer("Hans", 45)
lehrer2 = Lehrer("Claudia", 23)
print(lehrer1.sag_meinen_namen())
lehrer1.add_fach("Deutsch")
print(lehrer1.fach)


class Student:
    
    def __init__(self, name, alter, wohnort):
        self.name = name
        self.alter = alter
        self.wohnort = wohnort
    
    def gib_alter(self):
        return self.alter


class Kurs:
    
    def __init__(self, name):
        self.name = name
        self.is_active = True
        self.studenten_liste = []
    
    def add_student(self, student):
        self.studenten_liste.append(student)
    
    def get_durchschnitt_alter(self):
        age = 0
        for student in self.studenten_liste:
            age += student.gib_alter()
        
        return age / len(self.studenten_liste)
        
# Erstellen / Erzeugen von Instanzen der Klasse Student
s1 = Student("Ali", 24, "Hamburg")
s2 = Student("Anja", 30, "Berlin")
s3 = Student("Michael", 32, "Berlin")
s4 = Student("Norbert", 32, "München")
s5 = Student("Simon", 27, "München")

# Erstellen / Erzeugen einer Instanz der Klasse Kurs
kurs = Kurs("PY1")

# Klassen / Instanzen - Operationen

kurs.add_student(s1)
kurs.add_student(s2)
kurs.add_student(s3)
kurs.add_student(s4)
kurs.add_student(s5)

print(kurs.studenten_liste)
print(kurs.studenten_liste[0].gib_alter())
print(kurs.get_durchschnitt_alter())

# HINWEISE zu KOPIEREN / SPEICHERORT

class Lehrer: 
    
    def __init__(self, name, alter): # Konstruktor UND wird immer direkt beim Erzeugen einer Instanz aufgerufen
        self.name = name
        self.alter = alter
        
        
    def sag_meinen_namen(self):
        return self.name

    def add_fach(self, fach):
        self.fach = fach

lehrer1 = Lehrer("Hans", 45)
lehrer2 = Lehrer("Claudia", 23)

lehrer3 = lehrer1 # erzeugt ein neue Referenz auf die gleiche Instanz (pointer) (unüblich)

# Test auf Kreuz-Verweise
print(lehrer1)
print(lehrer3)

print(type(lehrer3))
print(lehrer3.name)

lehrer1.add_fach("Deutsch")
print(lehrer3.fach)

lehrer3.add_fach("Mathe")
print(lehrer1.fach)