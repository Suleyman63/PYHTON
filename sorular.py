
"""
# tek cift sayi
sayi = int(input('sayi gir'))

tek =0
cift=0

for i in range(sayi):
    if sayi %2 == 0:
        cift+= i   
    else:
         cift+= i       
print('cift sayilar', cift)
print('tek sayilar', tek)
"""



"""
sayi = int(input('sayi gir'))
for i in range(1, sayi):
        print(i)
"""


# alan cevre hesaplama
kisa = float(input('sayi gir'))
uzun = float(input('sayi gir'))

print('alan', float(kisa)*float(uzun))
print('cevre', 2* float(kisa)+float(uzun))