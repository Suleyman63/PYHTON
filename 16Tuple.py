
# TUPLE

# tuple kann wahrend der rutine nicht verandert werden
# tuple ist eine unveranderbare sammlung an daten

"""
my_tuple = (1, 10, 100)
my_tuple = 1, 3, 4

my_tuple3 = (1,) # wenn tuple mit nur einem item, dann zwingend ein, am ende, um tuple-type zuzuweisen
print(type(my_tuple3))

stuff = ('besen', True, 14, 5.5) # tuple kann verschidene datatypes beinhalten
print(stuff[1])

# nicht moglich wahrend run-time
# stuff.append('test)
# del stuff[2]
"""


"""
# Operation mit Tuple

tuple_main = (1, 10, 100)
t1 = tuple_main + (1000, 10000)
t2 = tuple_main * 3
t3 = t1 + t2
print(t2)
print(type(t2))

print(-10 not in t3) # False


liste = [1, 3, 5, 7]
my_tuple5 = tuple(liste)
print(my_tuple5) # (1, 3, 5, 7)

liste.append('cool')
my_tuple5 = tuple(liste)
print(my_tuple5) #(1, 3, 5, 7, 'cool')

var = 123
tuplepower = [1, 2, 3, 4, var]
print(tuplepower)

var = 'Blau'
print(tuplepower) 

"""


"""
capital = ('roma', 'ankara', 'berlin', 'madrid')
for cap in capital:
    print(cap)


capital=('roma', 'london')
print(capital)

sehirler = {'izmir', 'ankara', 'yalova', 'kars', 'izmir'}
print(sehirler)

print(type(sehirler))

#print(sehirler[0]) # set yapisinda indeksleme yoktur o yuzden hata aldik
 
sehirler.add('adana')
print(sehirler)

sehirler.update(['edirne', 'urfa'])
print(sehirler)

sehirler.remove('ankara')
print(sehirler)

#sehirler.remove('mugla')
#print(sehirler) #KeyError: 'mugla'

sehirler.clear()
print(sehirler)

del sehirler
print(sehirler)
"""