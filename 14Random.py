import random

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