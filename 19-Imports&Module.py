# IMPORT & MODULE




import random

import datetime

import math

import platform

import testmodul 


#********************************* Random ************************************

"""
#random ile verdigimiz degerler arasinda otomatik sayi verir
zahl=random.randint(1, 6)
print(zahl)
"""

"""
#verdigimiz listeden herhangi bir urunu alip geri dondurur
liste= ["apfel", "orange", "kirsche", "banane", "milch", "mehl"]
print(random.choice(liste))
"""

"""
#80-100 arasinda bir sayi dondurur
num=random.randint(80, 100)
print(num)
"""

"""
# sayi tahmin oyunu

num = random.randint(1, 100)

num1 = int(input('1-100 arasinda sayi gir'))

while num1 != num:
      if num1 < num:
        print(f'{num1} daha buyuk bir sayi giriniz')
        num1 = int(input())
      else:
        print(f'{num1} daha kucuk bir sayi gir')
        num1 = int(input())

print(f'Tabrikler {num1} numarayi bildiniz')

"""




#********************************* Platform Modul ************************************

x = platform.system()
print(x)

x = platform.version()
print(x)


x = platform.machine()
print(x)

x = platform.processor()
print(x)


#********************************* Math Modul **********************************

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)


#The abs() function returns the absolute (positive) value of the specified number:
x = abs(-7.25)
print(x)



x = pow(4, 3)
print(x)


x = math.sqrt(36)
print(x)


x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1


x = math.pi
print(x)


x = math.factorial(5)
print(x) #120



#********************************* Time Modul ************************************

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


x = datetime.datetime(2020, 5, 17)
print(x)


x = datetime.datetime(2021, 8, 24)
print(x.strftime("%B"))



#**************************************** Test Modul ***********************************

print(testmodul.x)

print(testmodul.person1)

a = (testmodul.person1["age"])
print(a)

