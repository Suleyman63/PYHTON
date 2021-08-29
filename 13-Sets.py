"""
zahlen = [2, 3, 5, 6, 8]
   
for zahl in zahlen:
    print(zahl)
    
    
for i in range(2):
    print(zahlen)
        
        
for i in range(len(zahlen)):
    print(zahlen[i])
    
"""


"""
#spielweise fur set / mengen

#uber set konnen wir ahnlich einer liste mehrere elmente ablegen, aber diesmal OHNE duplikate

set1 = {"berlin", "hamburg", "berlin"}
print(set1) #{'hambur', 'berlin'} double olanlari siler
print(len(set1)) # 2

set1.add("berlin")
print(set1) # {'berlin', 'hambur'} ekleme yapmadi

set2 = {"frankfurt", "bonn", "berlin"}
print(set2) # {'frankfurt', 'berlin', 'bonn'}
print(len(set2)) # 3


set3 = set1
print(set1) # {'berlin', 'hambur'}

set4 = set1.union(set2)
print(set4) # {'frankfurt', 'hamburg', 'bonn', 'berlin'}



set5 = set1.difference(set2)
print(set5) # {'hamburg'}


set6 = set1.intersection(set2)
print(set6) #{'berlin'}

for element in set2:
    print(element)
"""

"""
#ubungsaufgabe zum knobeln: finde den gold-dieb
#durch clevere kombination von diffenrece_update()
#den gold-dieb ermitteln 

verdaechtige = {
    "Ali",
    "Anja",
    "Ashenafi",
    "Daniel",
    "Detlef",
    "Dirk",
    "Heio"
}
print("Tatverdächtige:", verdaechtige)

# Personen mit Alibi
hat_alibi = {
    "Anja",
    "Detlef"
}
print("Mit Alibi:", hat_alibi)

# Personen die gerne Gold mögen
liebt_gold = {
    "Anja",
    "Ashenafi",
    "Detlef",
    "Dirk",
    "Heio"
}
print("Liebt Gold:", liebt_gold)

# Zugang zum Safe-Raum
zugang_zum_safe = {
    "Ali",
    "Ashenafi",
    "Detlef",
    "Dirk"
}
print("Zugang zum Safe:", zugang_zum_safe)

# Zugang zum Safe-Schlüssel
zugang_zum_safe_schluessel = {
    "Ali",
    "Anja",
    "Ashenafi",
    "Daniel",
    "Heio"
}
print("Zugang zum Safe-Schlüssel:", zugang_zum_safe_schluessel)


# Methoden anwenden auf "verdaechtige", um den Dieb zu ermitteln

# 1. Schritt
verdaechtige.difference_update(hat_alibi)
print(verdaechtige) # {'Heio', 'Daniel', 'Ali', 'Ashenafi', 'Dirk'}

# 2. Schritt
verdaechtige.intersection_update(liebt_gold)
print(verdaechtige) # {'Heio', 'Ashenafi', 'Dirk'}

# 3. Schritt
verdaechtige.intersection_update(zugang_zum_safe)
print(verdaechtige) # {'Ashenafi', 'Dirk'}

# Letzter Schritt
verdaechtige.intersection_update(zugang_zum_safe_schluessel)
print(verdaechtige) # {'Ashenafi'}

# set zu einer list konvertieren, um per Index das einzelne Element auszulesen
print("Der Golddieb ist:", list(verdaechtige)[0])

# Per union alle zu Verdächtigen machen
wanted = set().union(hat_alibi, liebt_gold, zugang_zum_safe, zugang_zum_safe_schluessel)
print(wanted) # {'Heio', 'Ashenafi', 'Detlef', 'Ali', 'Dirk', 'Anja', 'Daniel'}
"""
"""
print("union :", verdaechtige | hat_alibi | liebt_gold | zugang_zum_safe | zugang_zum_safe_schluessel)
print("intersection :", verdaechtige & hat_alibi & liebt_gold & zugang_zum_safe & zugang_zum_safe_schluessel)
print("difference :", verdaechtige - hat_alibi - liebt_gold - zugang_zum_safe - zugang_zum_safe_schluessel)
"""


"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

"""


"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
"""

"""
A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'}

result = A.difference_update(B)

print('A = ', A)
print('B = ', B)
print('result = ', result)
"""

