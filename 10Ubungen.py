
# Masse des Alkohols
"""
m = 80.0
r = 0.7
V = 500
e = 0.05

A = V * e * 0.8
print(A)

promille = A / (m * r)
print("1. Tsetfall: {0:.2f=}".format(promille))

"""


# Übungsaufgaben

# 1.) 3 weitere Testfälle erzeugt - dabeigerne mal weiblich oder alkoholfreies Getränk


# 2.) Gruppenarbeit: gemeinsam in
# 3-er Gruppen eine andere Formel suchen und einsetzen

# Beispiel:

# - eigene Formeln recherchieren
# - Body-Mass-Index
# - Stoffwechselrate
# - Baustammvolumen

# - Körperoberfläche
# - Promillerechner - Alternativezu Widmark

# BONUS zu Aufgabe 1: versuchen, die Daten per User-Input zu verarbeiten


"""

w = int(input("weight"))
h = int(input("height"))

a = w / h ** 2
print(a)

        
   
        
# bei Frauen      
l = float(input('Liter: '))
p = float(input('Prozent: '))
k = float(input('kg: '))


a = 0.6 
b = 10*p*l*0.8
result = b/(k*a)


print(result, 'Promille')     
        
     
        

l = float(input('Liter: '))
p = float(input('Prozent: '))
k = float(input('kg: '))
g = input('Geschlecht (w/m): ')


if g == 'w':
    faktor = 0.6
else:
    f = 0.7
m = 10*p*l*0.8
promille = m/(k*f)



print('Die berechnete Alkoholkonzentration im Blut beträgt:')
print(promille, 'Promille')        
        
        
        
 """       
        
        
        
        
        
        
        
        
        
        