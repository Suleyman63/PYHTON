                # Anführungszeichen innerhalb eines Strings

print('Das ist ein Zitat: "Zitat" ')
print("Das ist ein Zitat: 'Zitat' ")


# Escaping
print("Das ist ein Zitat: \"zitat\"")
# Escaping mit Zeilenumbruch
print("Mein Name ist Bond.\nJames Bond")

# Escaping - Anwndungen
print("C:\\home\\desktop")
print("C:\\\norbert\desktop")

# Obacht bei Python-internen Anweisungen wie z.B. \n \t
print('test\\test')

# end - Argument für Zeileumbrüche ODER Zeilen-Endungen
# default-Wert ist end = "\n"
print("Mein Name ist:", end = " ")
print("Sebastian")

# Argumente in der print-Methode
print("Inventar:" , "Schwert", "Münzen", "Stock")

# Kommas erzeugen Leerzeichen, + fügt Strings zusammen OHNE Leerzeichen
print("Lebenspunkte:", 100)
print("Heio" + "Teilnehmer")

# Obachcht!:  Funktioniert nicht bei Int+Str
# print("Heio" + 100)

# sep - Argument
print("Ich", "bin", "separiert", 100, sep = "\n")

# Übung -  Was kommt raus?
print("Mein", "Name", "ist", sep="_", end="*")
print("Prinz", "Varo.", sep="*", end="*\n")
print("Und dein Name ist?")

# Anführungszeichen innerhalb eines Strings

print('Das ist ein Zitat: "Zitat" ')
print("Das ist ein Zitat: 'Zitat' ")


# Escaping
print("Das ist ein Zitat: \"zitat\"")
# Escaping mit Zeilenumbruch
print("Mein Name ist Bond.\nJames Bond")

# Escaping - Anwndungen
print("C:\\home\\desktop")
print("C:\\\norbert\desktop")

# Obacht bei Python-internen Anweisungen wie z.B. \n \t
print('test\\test')

# end - Argument für Zeileumbrüche ODER Zeilen-Endungen
# default-Wert ist end = "\n"
print("Mein Name ist:", end = " ")
print("Sebastian")

# Argumente in der print-Methode
print("Inventar:" , "Schwert", "Münzen", "Stock")

# Kommas erzeugen Leerzeichen, + fügt Strings zusammen OHNE Leerzeichen
print("Lebenspunkte:", 100)
print("Heio" + "Teilnehmer")

# Obachcht!:  Funktioniert nicht bei Int+Str
# print("Heio" + 100)

# sep - Argument
print("Ich", "bin", "separiert", 100, sep = "\n")

# Übung -  Was kommt raus?
print("Mein", "Name", "ist", sep="_", end="*")
print("Prinz", "Varo.", sep="*", end="*\n")
print("Und dein Name ist?")

#Mein_Name_ist*Prinz*Varo.*
#Und dein Name ist? (Endet mit einem Zeilenumbruch)

#Mein_Name_ist*Prinz*Varo.*
#Und dein Name ist? (Endet mit einem Zeilenumbruch)

var = 1
name = "Sebastian"
gleitkomma = 3.0
gleitkomma2 = .5
ist_das_licht_an = False
PI = 3.141


# Constants werden als Konvention in Python UPPER-CASE / groß geschrieben
FESTE_TEILNEHMERZAHL = 20

#TEST = 10
#print(type(TEST))
#TEST = "Sebastian"
#print(type(TEST))

# Variablennamen - Konvention und Regeln:
# - muss mit Buchstaben beginnen
# - Regel: Python ist case sensitive! Varo ist nicht gleich VARO, Variable Licht ist nicht gleich Variable licht (licht = 10, Licht = True) invalid synthax
# - Regel: als Variablennamen keine "reservierten" Worte möglich: Variable kann nicht heißen: True / if / and , nicht möglich z.B. True = "Hallo"
# - Konvention: snake_case , Beispiele: ist_licht_an / is_light_on, name_of_person
# - möglich, aber unkonventionell: camelCase
# - Konvention: Konstanten in Python: ALL UPPER CASE, z.B. TEILNEHMERZAHL = 20

# HIER LISTE MIT GESPERRTEN WÖRTEN EINFÜGEN #

zahl = 100
print(zahl)
zahl = 200 + 300
print(zahl)
zahl = "Guten Tag"
print(zahl)

# ShortHand
number = 1
print(number)
number = number + 1
print(number)
number += 1
print(number)
number -= 10
print(number)

# ShortHand für mathematische Operationen: += , -=, *=, /=, %=, //=, **=
# Obacht: KEIN ++ Inkrementor, KEIN -- Dekrementor , in Python nicht existent

num = 2
num = num ** 3
print(num)


num2 = 2
num2 **= 3
print(num2)


i = 10
j = 20
i = i + 2 * j
# Lösung als ShortHand: 
i += 2 * j


p = 10
p /= 2
print(p) # 5.0
# p /= 2 ist das gleiche wie: p = p / 2


#print("hello world")

#print(2**3)
#print(3/3.0)

#var = 1
#name="sebastian"
#gleitkomma=3.0
#gleitkomma2=.5
#ist_offen=False
#Pi=3,14


#FESTE_TEILNEHMERVAHL=20

#TEST = 10
#print(type(TEST))
#TEST="sebastian"

#zahl = 100
#print(zahl)
#zahl = 200 + 300
#print(zahl)
#zahl="guten tag"
#print(zahl)

#i=10
#j=20
#i=i+2*j
#print(i)

# Shorthand
#number=1
#print(number)
#number=number+1
#print(number)
#number -=10
#print(number)


#p=10
#p/=2
#print(p)



# sicakllik hesaplama 
#celsius = 32
#fahrenheit = (celsius * 1.8) + 32
#print((celsius,fahrenheit))

#user input
#print("wie ist dein name")
#name=input()
#print("hallo", name)

#zahl=int(input("zahl geben"))
#print(zahl + 10)

#var = int(input("zahl : "))
#print(var + 10)
                




#a = int(input("A:"))
#b = int(input("B:"))
#c = (a ** 2 + b ** 2)**0.5
 
#print("\nHipotenüs:",c)