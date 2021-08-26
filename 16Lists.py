# list

# erweitere liste funktionalitat

# listen anlegen / kopieren, obacht, besonderheit
# listen fullen

"""
# listen kopieren
x = 10
y = x
x = 20

print('x', x)
print('y', y)

list_1 = [1]
list_2 = list_1
list_1[0] = 'keriz'
print('liste1', list_1)
print('liste2', list_2)
"""


"""
# listen kopieren via slice
# A slice of this from makes a new list, taking element from the source list - the element of the indices from start to end 
print("**********************************")
list_a = [1, 2, 3, 4, 5, 6, 8, 9]
list_b = list_a[2:5] #[3, 4, 5]
list_a[0] = 'hallo'
print('lite_a', list_a)
print('list_b', list_b)



print('*******************************************')
stringname = 'BERTI'
print(stringname[-4:-1]) # ERT




print('+++++++++++++++++++++++++++++++++')
listi = [3, 4, 1, 6, 9]
del listi[2:5] # [3, 4]
print(listi)


print('++++++++++++++++++++++++++++++')
list_3 = [1, 3, 5, 7, 8]
list_4 = list_3[:]
list_3[0] = 15
print(list_4)
"""

########################################################################

# Listen fullen und schlifen

"""
reihe = []

for i in range(8):
    reihe.append('spielfigur')
print('reihe1 : ', reihe)



# pyhton weg fur loops und listen

reihe2 = ['spiel : ' for i in range(5)]
print(reihe2)



quadrahzahlen = [x**2 for x in range(10)] # birden 9 a kadar saxyilarin karesini aldik
print(quadrahzahlen)

ungerade_zahlen = [x for x in quadrahzahlen if x % 2 != 0] # tek sayilarin karesi
print(ungerade_zahlen)

ungerade_zahlen2 = [x for x in quadrahzahlen if x % 2 == 0] # cift sayilarin karesi
print(ungerade_zahlen2)
"""

liste6 = []

for i in range(8):
    reihe3 = [['leer' for i in range(8)] for j in range(8)]
    liste6.append(reihe3)


liste6[0][0] = 'TURM'
liste6[0][7] = 'TURM'
liste6[7][0] = 'TURM'
liste6[7][7] = 'TURM'

print(liste6)

drei_dimension_liste = [[['X' for i in range(8)] for j in range(8)] for k in range(8)]

drei_dimension_liste[1][3][4] = 'TEST'
print(drei_dimension_liste[1][3][4])
print(drei_dimension_liste[1][3])
print(drei_dimension_liste[1])


drei_dimension_liste[1] = 'ICH BIN EIN BUG'
print(drei_dimension_liste)