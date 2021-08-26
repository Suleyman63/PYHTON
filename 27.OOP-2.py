class Tier:
    def __init__(self, name, gewicht):
        self.name = name
        self.gewicht = gewicht
        print('******************************************************')


    def show_info(self):
        print(f'ich bin eine {self.name}, ich weige {self.gewicht} kg!')

    
    def gib_laut(self):
        print('ich weis nicht, welchen laut ich geben soll')

tier = Tier('Jack', 20)
tier.gib_laut()
tier.show_info()


# Vererbung

class Katze(Tier):

    def gib_laut(self):
        print('Miau Miau')



class Hund(Tier):


    def gib_laut(self):
        print('wuff wuff')


class Fisch(Tier):
#super cllas kullandik
    def __init__(self, name, gewicht, farbe):
        super().__init__(name, gewicht)
        self.farbe = farbe
      

class Wolf(Tier):
    def __init__(self, name, gewicht):
        super().__init__(name, gewicht)

        

katze = Katze('pinki', 6)
katze.gib_laut()

hund = Hund('bello', 10)
hund.gib_laut()

fisch = Fisch('blubbi', 10, 'rot')
fisch.gib_laut()


print(fisch.farbe)
print(hund.name)
print(katze.gewicht)