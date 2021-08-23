
# 1. Formel BAK (Promillerechner) einsetzen
# 2. mehrere Testfälle (5-6) in einer Liste "alkoholtests" (nur die Werte für Promille) ablegen
# 3. Per Schleife alle Testergebnisse untereinander ausgeben
# 4. Den maximalsten und minimalsten Wert der Liste ausgeben
#5. BONUS: Eingaben für die jew. Testfälle per User-Input ermöglichen




#promile rechner
l = float(input('Liter: '))
p = float(input('Prozent: '))
k = float(input('kg: '))
g = input('Geschlecht (w/m): ')


if g == 'w':
    faktor = 0.6
else:
    faktor = 0.7
m = 10*p*l*0.8
promille = m/(k*faktor)

print(promille, 'Promille')  


#testfalle 
"""
testfalle = []

num = int(input('wie viel person: '))

i = 0

while(i<num):
    person = input('person name: ')
    prozent = input('person prozent: ')
    testfalle.append({
        'person': person,
        'prozent': prozent
    })
    i += 1

for zahl in testfalle:
    print(f'person name: {zahl["person"]} person prozent: {zahl["prozent"]}')
    
    print(f'maximum prozent {max(prozent)}')
    
    print(f'minumum prozent {min(prozent)}')
"""