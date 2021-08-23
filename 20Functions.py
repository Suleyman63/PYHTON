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

def number(k):
    if(k > 0):
        result = k + number(k - 1)
        print(result)
    else:
        result = 0
    return result

number(9)