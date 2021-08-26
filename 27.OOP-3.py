# Klassen - Atrtribute, klassen-variablen (nicht instanzen)

class Person:
    
    _personenzahlen = 0

    def __init__(self, name):
        self.name = name
        Person._personenzahlen += 1

p1 = Person('timi')
print(p1._personenzahlen)


p2 = Person('helga')

print(p1._personenzahlen)

p3 = Person('herbert')
print(p3.name)
print(p3._personenzahlen)