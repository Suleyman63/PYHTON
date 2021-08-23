
# ARRAYS

"""
city = ["berlin", "hamburg", "frankfurt"]
print(city)

print(city[2])


#append()
city.append('hanovver')
print(city)

zahl = 9
print(zahl)

print(len(city))


zahlen = [1, 2, 8, 3, 7, 2, 4, 6]

print(zahlen[4])

zahlen.append(12)
print(zahlen)


# flexibilatät moglich
mix = [5, 6, 1.2, "hallo", True, 120, 'test']
print(mix)


person = ["peter", "simidt", 33, True, 1000.5]
print(person)


print(city.count('berlin')) # 1 adet



liste =  ["Manisa","Düzce","Bolu", "Karabuk", "Urfa", "Mersin"]

# 1. per for ... in-Schleife
for sehir in liste:
    print(sehir.upper())

# 2. per for ... range-Schleife
for i in range(5):
    print("aktuelle zahlervariable : ", i)
    print(liste[i]) #urfa
    
    
# 3. dynamisch per len()
for i in range(len(liste)):
    print("aktuelle", i)
    print(liste[i])


print(max(zahlen))
print(min(zahlen))


name = "deutschland"
print(list(name))

"""
"""
number= list(range(1,11))
print(number)

number2 = [number for number in range(1, 16)]
print(number2)

cities = ['izmir', 'ankara', 'ist', 'bursa']
print(cities)

cities2 = cities
print(cities2)

cities.append('artvin')
print(cities)
"""

"""
dersler = ['mat', 'fiz', 'kimya', "biy", 'ing']
print(dersler[2].upper())
print(dersler[0].upper())

print(dersler[1:3])
print(dersler[:3])
"""


"""
dersler2 = ['mat', 'fiz', ['fen' , 'beden'], 'kimya', "biy", 'ing']
print(dersler2[2][0])
print(dersler2[-1])

dersler2.append("resim")
print(dersler2)

dersler2[len(dersler2):] = ['cografya']
print(dersler2)


dersler2.insert(0, "geom")
print(dersler2)

dersler2.insert(len(dersler2), 'fransizca')
print(dersler2)


del dersler2[2]
print(dersler2)

dersler2.remove('kimya')
print(dersler2)

dersler3 = []
for ders in dersler2:
    dersler3.append(ders)
print(dersler3)


num = [32, 66, 2, 4, 6, 7, 9, 12, 34, 54,]

num.sort()
print(num)

"""
