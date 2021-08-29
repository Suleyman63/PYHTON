# FILES (OPEN; WRITE)
# Files (datein offnen, datein lesen, datein schreiben, datein speichern, datein schliessen)

# enorm wichtig in pyhton: datein offnen und wieder schlissen 

# READ


cources = ['pyhton', 'java', 'c++', 'javascript', 'ruby']

with open('yeni.txt', 'w') as f:
   for c in cources:
       f.write(f'{c}\n')


with open('yeni.txt', 'r') as f:
    file = f.readlines()
    file = [element.strip('\n') for element in file if '\n' in element] #ters silas n i kaldirdik
    print(file)

# usteki yeni,txt dosyasinin kopyasini olusturduk
with open('yeni2.txt', 'w') as file2:
    for line in file:
        file2.write(line)

#f = open('data.txt', 'r')

#inhalt = f.read()
#print(inhalt) #  alex, emily, hans
#print(type(inhalt)) # class str


#zeile1 = f.readline()
#print(zeile1)
#zeile1 = f.readline()
#print(zeile1)
#zeile1 = f.readline()
#print(zeile1)

"""
lines = f.readlines() # gibt immer eine liste zuruck
for i in lines:       # uber liste kann naturlich iteriert werden oder einzeilne zeilen via index abgerufen werden
    print(i, end="")


f.close()

#************************ CONTEXT MANAGER +++++++++++++++++++++++++++++++++++

with open('data.txt', "r") as f:
    inhalt = f.read()

    print('\nHat der Context-Manager meine Datei automatisch geschlossen?', f.closed)

# WRITE
with open("data.txt", "w") as f: 
    f.write('peter\n')
    f.write('kemal\n')
    f.write('claudia\n')
    f.write('jurgen\n')


# APPEND
with open('data.txt', 'a') as f:
    f.write('simone\n')
    f.write('heinz\n')
    f.write('Timo\n')


# ERZUEGEN
with open('neu.txt', 'w') as f: # otomatik yeni txt dosyasi olusturduk
    f.write('HALLO')
 

inventar = "Schwert, Geld, Trunk"
inv = inventar.split(",")
inv.append('schild')
print(inv)

with open('inventar.txt', 'w') as f:
     for i in inv:
         f.write(i + ', ')
"""



