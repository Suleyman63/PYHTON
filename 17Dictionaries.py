
#personen_info={"petra"}
#print(type(personen_info)) #<class 'set'>

#personen_info={"vorname" : "petra", "nachname" : "muller"}
#print(type(personen_info)) #<class 'dict'>

#ziel: petra ausgeben

#print(personen_info[0]) #KeyError: 0
#print(personen_info["vorname"]) #petra
#print(personen_info["nachname"]) #muller


"""
person1 = {
    "vorname" : "Petra",
    "nachname" : "Schmitz",
    "alter" : 33,
    "ort" : "Berlin",
    "istOnline" : False,
    "gehalt" : 3500.50,
    "hobbies" : ["Radfahren", "Bergsteigen", "Basketball"]
}


person2 = {
    "vorname" : "Peter",
    "nachname" : "Fox",
    "alter" : 25,
    "ort" : "Hamburg",
    "istOnline" : True,
    "gehalt" : 3200.0,
    "hobbies" : ["PS5", "Fußball"]
}


person3 = {
    "vorname" : "Susi",
    "nachname" : "Fuchs",
    "alter" : 18,
    "ort" : "Frankfurt",
    "istOnline" : True,
    "gehalt" : 1000.75,
    "hobbies" : ["Kochen", "Klettern"]
}



personen= [person1, person2, person3]
print(personen)

# 2. kisinin son hobisi 
print(personen[1]["hobbies"][-1])

# 3. kisi online mi
if personen[2]["istOnline"]:
    print("online")
else:
    print("offline")

# 1. kisinin yasini bulunuy
print(personen[0]["alter"])


#for i in personen:
 #   print(i)

"""


"""
stad = {"name": "berlin", "einwohner": 3.600, "Einwohner2": "3.500"}
# format fonk ile yazdirdik
print("{0} hatte im jahr 2019 {1} Mio einwohner".format(stad["name"], stad["einwohner"]))
# f fonk ile yazdirdik
print(f"{stad['name']} hatte im jahr 2019 {stad['einwohner']} einwohner")
print(len(stad))
# get methodu kullandik
print(stad.get("name"))

if "einwohner" in stad:
    print("Key einwohner ist vorhanden")
else:
    print("Key einwohner ist vorhanden")
"""

"""
monate = {1 : "Januar", 2: "Februar", 3: "Marz", 4: "April"}
print(monate[4]) # april
print(monate.get(3))# marz


# daten andern per update()
#ziel: januar in januar
monate.update({1: "jan"})
print(monate)

"""


"""
monster = {'name' : 'guru', 'power': 10, 'color': 'red'}
print(monster['name'])

#positin ekledik
monster['position']=100
print(monster)


print(monster.get('color'))

# guru yu buyuk harfe cevirdik
monster.update({'name' : 'GURU'})
print(monster)

#power i 30 yaptik
monster.update({'power' : '30'})
print(monster)

# name ismini sildik
del monster['name']
print(monster)

# power i kladirdik
monster.pop('power')
print(monster)

# urunleri listeledik
print(monster.items)

# listeyi temiyledik
monster.clear()
print(monster)

# tum listeyi sildik
del monster
print(monster)

# for dongusu ile listeledik
for key in monster:
    print(key)

#sadece keyleri cagirdik
for key in monster.keys():
    print(key)

# sadece valueleri istedik
for key in monster.value():
    print(key)

"""

"""
friends = {'ebru': 44, 'deniz': 29, 'ahmet': 32}

# ebrunun yasini aldik
print(friends['ebru'])


#yas ortalamsini aldik
print(sum(friends.values()) / len(friends))


# eren diye birini ekledik
friends['eren'] = 33
print(friends)

# ebru ve denizin yaslarini guncelledik
friends.update({'ebru' : 21, 'deniz' : 36})
print(friends)

"""

"""
num = {'number': [1, 3, 5, 7, 9, 6]}

# sayilarin karesini aldik
#num['number'] =[ num['number'][0]**2, num['number'][1]**2, num['number'][2]**2, num['number'][3]**2]
#print(num) #{'number': [1, 9, 25, 49]}


#sayilarin karesini aldik
for v in num.values():
    newliste = [] 
    for a in v:
        newliste.append(a**2)

num['number'] = newliste
print(num)

"""

"""
friends2 = {'enes': 44, 'derya': 29, 'ali': 32}

key_list = []
value_list = []


for k, v in friends2.items():
  key_list.append(k)
  value_list.append(v)

  print(key_list)
  print(value_list)
  print(sum(value_list))
"""


# 1 den 10 a kadar olan sayilarin karesini aldik
#numbers = {x : x**2 for x in range(1, 11)}
#print(numbers)