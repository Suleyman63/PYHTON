# FUNCTIONS

"""
def hello():
    print("Elveda Zalim Dünya!")
    

hello()
"""

"""
def my_function(user):
    print(f'Hallo {user}')

my_function('kemal')
my_function('ali')
"""

"""
def func1():
    return 5 + 10

def func2():
    print(6 + 6)

result1 = func1()
result2 = func2()

print(f'{result1}, {result2}') #15, None
"""

"""
def func3():
    pass

func3()
"""

"""
def func4():
    print(5 + 7)

func4()
"""


"""
def func5(parametreler):
    print(parametreler)

func5(isim="Ahmet", soyisim="Öz", meslek="Mühendis", şehir="Ankara")
"""


"""
liste = [1, 4, 6, 7, 9, 7]
print(liste)

liste = set(liste)
print(liste)

print(type(liste))# class set

print(sum(liste)) # 27
"""

"""
def karesi(x):
    return x**2

x = int(input('bir sayi gir'))
print(f'girilen {x} sayisinin karesi {karesi(x)}')
"""


"""
def multiply(liste):

    mult = 1
    for x in liste:
        mult *= x
    return mult

list1 = [3, 5, 7, 9]

print(multiply(list1)) #945
"""

"""
def faktoriyel(a):

   if a == 0:
    return 1
   else:
    return a * faktoriyel(a-1)

a = int(input('bir sayi giriniz'))
print(faktoriyel(a)) 
"""


"""
def kup_cevre(b):
    return 12*b

def kup_alan(b):
   return 6*b**2

def kup_hacim(b):
    return b**3

b = int(input('kenar uzunlugu giriniz'))
print(f'kenari {b} olan kupun cevresi {kup_cevre(b)}, alani {kup_alan(b)} ve hacmi {kup_hacim(b)} dir')
"""

"""
def my_function(*kinder):
      print("Das Kind " + kinder[2])

my_function("Emil", "Tobias", "Linus") #Tobias


def my_function(kind3, kind2, kind1):
      print("Das Kind " + kind3 + ' ' + kind2 + ' ' + kind1)

my_function(kind1 = "Emil", kind2 = "Tobias", kind3 = "Linus")
"""

"""
def my_function(land = "Norway"):
      print("ich komme aus " + land)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
"""

"""
fruits = ["apple", "banana", "cherry"]

def my_function(food):
      for x in food:
        print(x)

my_function(fruits)
"""

"""
def number(k):
    if(k > 0):
        result = k + number(k - 1)
        print(result)
    else:
        result = 0
    return result

number(9)
"""


"""
# Positional Arguments

def show_info(vorname: str, nachname : str, alter : int): #datatyp hints  variabenname : datentyp
    print(f"Dein Name ist {nachname}, {vorname} , du bist {alter} Jahre alt")

show_info("Berti", "Voigts", 63)
show_info("Sebastian", "Christoph", 35)
show_info("Schmidt", 35, "Jürgen")

# Beim Duck-Typing wird zur Laufzeit des Programms geprüft, ob ein Objekt die entsprechenden Merkmale unterstützt.
# Dies führt wie bei allen dynamischen Typsystemen zu einer erhöhten Flexibilität, reduziert aber ebenso die Möglichkeit,
# statisch zur Übersetzungszeit Fehler im Programm zu finden. 

# Infos Type-Hints/Check:
# https://docs.python.org/3/library/typing.html
#"The Python runtime does not enforce function and variable type annotations.
# They can be used by third party tools such as type checkers, IDEs, linters, etc."


#info = show_info
#info("Jürgen", "Voigts", 35)
#print(type(info))

# Named Arguments

def show_info_2(vorname, nachname, alter):
    print(f"Dein Name ist {vorname} {nachname}, du bist {alter} Jahre alt!")
    
show_info_2(nachname = "Meyer", alter = 56, vorname = "Maria")

####
# default-Parameter-Werte in der Funktion
def show_info_3(vorname = "Jon", nachname = "Doe", alter = 999):
    print(f"Dein Name ist {vorname} {nachname}, du bist {alter} Jahre alt!")

# kein Problem
show_info_3(alter = 12)
show_info_3(alter = 20, nachname = "Schmidt")
show_info_3("Hans", "Peter", 34)
show_info_3(True, 12, "Haus")
show_info_3(alter = "Hallo")
show_info_3("Jürgen", "Schmidt", alter = 20) # ERST Positionale Argumente, DANN keyword arguments
show_info_3(vorname = "Hannes", "Schmidt" , 15)


# Regeln (keine Konvention, sondern Syntax)
# 1 Deklaration von Funktionen
# default arguments folgen IMMER positional aruments
# erlaubt: def erlaubt(a, b, c = 10)
# nicht erlaubt: def nicht_erlaubt(a = 5, b, c)

#2 Aufruf von Funktionen
# beim Funktions-Aufruf: keyword-arguments folgen IMMER positional arguments
# erlaubt: erlaubt1(1, 2, c = 3)
# nicht erlaubt: nicht_erlaubt1(a = 1, 2, 3)

"""

"""
# Funkrionen ohne Ruckgabe-Wert
def summe(a, b):
    print(a+b)

summe(2, 3)
summe('hallo', 'welt')
summe(1, True) # True fonk nicht

print(summe(3, 5), 'Test') # None Test
summe(3, 5) # 8


def addition(x, y):
    return x + y


print('===========')
print(addition(3, 9))


result = addition(10,10) + addition(33,33)
print('result ist', result)

"""


"""
# Beispiel test bestanden
def klasur_bewertung(punkte):
    if punkte >= 90:
        return 'du hast bestanden'
    else:
        return 'du hast nicht bestanden'

# Iteration

schulnoten = [
    ['omer', 65],
    ['alev', 50],
    ['ali', 95],
    ['kemal', 90]
]

for note in schulnoten:
    print(note[0], klasur_bewertung(note[1]))

"""

"""
# artik yil hesaplama
# 1. yontem
#yil = 2021
#print(yil % 4 == 0 and (yil % 100 != 0 or yil % 400 == 0))

# 2. yontem
def artik_yil_mi(yil):
    if (yil % 4) == 0:
        if (yil % 100) == 0:
            if (yil % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False

sayi=0
onceki_artik_yil=4
aralik_toplami=0
for yil in range(2000,2021):
    if(artik_yil_mi(yil)):
        aralik_toplami=yil-onceki_artik_yil+aralik_toplami
        onceki_artik_yil=yil
        print(yil)
        sayi=sayi+1
    else:
        continue
print("Yil sayisi:" + str(sayi) , "Ortalama artik yil araligi:" + str(round(aralik_toplami/sayi,2)))

"""

"""
#Primezahlen

def main():
    n = input("Please enter a number:")
    is_prime(n)

def is_prime(a):
    x = True 
    for i in (2, a):
            while x:
               if a%i == 0:
                   x = False
               else:
                   x = True


    if x:
        print("prime")
    else:
        print("not prime")

main()

"""


"""
# Collatz - Theorem

steps = 0
c0 = int(input('gib eine pozitive zahl gorser als 0 ein'))

while c0 !=0:

    while c0 !=1:
        if c0 % 2 == 0:
            c0  //= 2
        else:
            c0 = 3 * c0 + 1
        steps += 1
        print(c0)

print('steps: ', steps)
steps = 0
c0 = int(input('gib eine pozitive zahl gorser als 0 ein'))
"""
