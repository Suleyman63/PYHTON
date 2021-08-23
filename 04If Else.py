
# LOGISCHE OPERATOREN

#x = float(input("geben sie ein Nummer"))
#y = 1 / (x + 1 / (x + 1 / (x + 1 /x)))
#print(y)


# print(2 == 2.0) true


#if block

#if 5 > 2:
#print("funf ist groseßer als zwei")


#x = 10
#y = 20.0
#if x == y:
#print("werte sind gleich")
#print("if-block beendet")


#IF ELSE BLOCK
#x = 10
#y = 20.0
#if x == y:
#   print("werte sind gleich")
#   print("vielen dank")
#else:
 #   print("werte sind nicht gleich")
  #  print("vielen dank")
  
  
  # NESTING IF ELSE BLOCK
  
  
#vorname = "alex"
#alter = 55
  
#if vorname == "alex":
   # if alter > 50:
   #       print("du bist alter als 50")
  #  else :
 #         print("du bist junger als 50")
#else:
 #   print("du heist nicht alex")
  
  

  
#i = 20
#if (i < 15):
  #  print ("i kleines als 15")
 #   print ("ich bin im else Block")
#else:
  #  print ("i großer als 15")
 #   print ("ich bin im else Block")
#print ("ich bin nicht im if und nicht im else Block")


  
 # temperatur = 20
  
#if temperatur < 0:
 #     print("es ist kalt")
#elif temperatur < 20:
  #    print("es ist nicht kalt")
#else:
 #    print("es ist heiß")
  
  
  
""" 
# uc sayidan buyuk olani bulma  

nummer1 = int(input("Nummer 1: "))
nummer2 = int(input("Nummer 2: "))
nummer3 = int(input("Nummer 3: "))

if (nummer1 >= nummer2) and (nummer1 >= nummer3):
   grose = nummer1
elif (nummer2 >= nummer1) and (nummer2 >= nummer3):
   grose = nummer2
else:
   grose = nummer3

print(nummer1," ",nummer2," ",nummer3,"am groste nummer",grose)
"""

"""
liste = ['ahmet', 'mehmet', 'ebru']

if 'ahmet' in liste:
       print('ahmet listede var')
"""  

"""  
age = 15

if age >= 18:
      print('oy kullanabilir')
else:
      print('oy kullanamaz')
 """ 
  
""" 
if age <= 12:
         print('%50 indirim')
elif age <= 10:
       print('%70 indirim')
else:
       print('indirim yok')
"""  
  
  
""" 
age = int(input('yas giriniz'))
if age < 0:
       age = 0
       print('negatif sayi sifira cevrildi')
elif age == 0:
       print(' sifirdan baska sayi giriniz')
elif age < 18:
       print('oy kullanamz')
else:
       print('oy kullanabilir')
  
"""


"""
my_condition = 0

if my_condition:
   print('kosul dogru')
else:
   print('kosul dogru degil')
"""

"""
num = int(input('bir sayi giriniz'))

if num % 2 == 0:
   print(f'{num} cift sayidir')
else:
   print(f'{num} tek sayidir')

"""

"""
num = int(input('bir sayi giriniz'))

if num == 0:
   print(f'{num} sayisi 0 dir')
elif num > 0:
   print(f'{num} pozitif sayidir')
else:
   print(f'{num} tek sayidir')
"""

"""
num1 = int(input('bir sayi giriniz'))

if num1 == 0:
   print(f'{num1} sayisi 0 dir')
elif num1 > 0:
   print(f'{num1} pozitif sayidir')
elif num1 < 0:
   print(f'{num1} negatif')
"""

"""
x = 10
y = 5
if x > y: print(f'{x} sayisi {y} sayisindan buyuktur')
"""

"""
num = int(input('bir sayi giriniz'))

faktoryel = 1

if num < 0:
       print(f'{num} sayisi negatiftir')
elif num == 0:
       print(f'{num} faktoryeli {faktoryel} dir')
else:
       for x in range(1, num+1):
              faktoryel = faktoryel*x
              print(faktoryel)
"""


"""
notes = {'ahmet': 58, 'mehmet': 88, 'ayse': 90, 'fatma': 70}

for key, value in notes.items():
      if value >= 50:
              print(f'{key} aldigi not {value} GECTI')
      else:
             print(f'{key} aldigi not {value} KALDI')
"""           










