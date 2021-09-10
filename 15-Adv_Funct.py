################### - FIRST CLASS FUNCTIONS - ##############################
# first class fonksiyonun kendisini bir degiskene atiyoruz
"""
def summation(x, y):
    return x+y

result = summation


print(result(10,22))

print(summation)
print(type(summation))
print(result)
print(type(result))


if result is summation:
    print('TRUE')
else:
    print('FALSE')

"""


######################### - HIGHER ORDER FUNCTION - ################################
# kendine baska fonk parametre olarak alan fonklara hoch order func diyoruz
"""
def summation(arr1, func):
    total = 0
    for i in arr1:
        total += func(i)
    return total

def squared(x):
    return x+x

def cubed(y):
    return y*y*y


print(summation([1, 3, 5], squared))
print(summation([1, 4, 9], cubed))
"""



#################### - RETURN FUNCTION - #################################################
# return function dq functionun kendisini return olarak donduruyoruz
"""
def say_name(name):

    def my_name():
        print(f'benim adim : {name}')

    return my_name


arin_name = say_name('mehmet')
print(arin_name())
"""

"""
def employee(name):
        def salary(euro):
            print(f'benim adim: {name} ve maasim : {euro}')

        return salary

x = employee('kemal')
x(3000)
"""


"""
from random import choice

def my_team(team):
    def get_title():
        meesage = choice(('sampiyon ',  'vasat ',  'kume '))
        return meesage

    result = get_title() + team
    return result

print(my_team('Roma'))
"""


#################### - CLOSURE -#########################################
"""
def parent_func(name):
    the_name = name
    def inner_func():
        print(f'benim adim : {the_name}')


    return inner_func

x_name = parent_func('kamil')
x_name()
"""


################### - DECORATOR -##############################################
"""
def merhaba(func):
    def wrapper():
        print('fonksiyonan once yazdiriyoruz')
        func()
        print('fonksiyondan sonra yazdiriyorum')

    return wrapper

def lang_es():
    print('hola')

lang_es=merhaba(lang_es)
lang_es()
"""


"""
user = {
    'username': 'asim',
    'role': 'admin'
}

def check_admin(func):
    def wrapper():
        if user.get('role') == 'admin':
            return func()
        else:
            raise PermissionError('yetkiniz yok')

    return wrapper


@check_admin
def delete_product():
    print('urun silindi')

delete_product()

"""

"""
def hallo(func):
    def wrapper(*args, **kwargs):
        print('fonksiyonan once yazdiriyoruz')
        func(*args, **kwargs)
        print('fonksiyondan sonra yazdiriyorum')

    return wrapper

@hallo
def name_age(name, age, gender):
    print(f'benim adim : {name} ve {age} yasindayim ve Cinsiyetim : {gender}')

name_age('kenan', 32, 'F')

"""

#################### - THE WALRUS OPERATOR - #################################
# hem degisken olarak atiyoruz hemde yazdiriyoruz

#print(name := 'asim')



#if (x := 40) > 20:
 #   print(f'{x} 20 den buyuktur')


"""
my_list =list()

while (entry := input('listeye ekle : ')) != 'exit':
    my_list.append(entry)

print(my_list)
"""

############################ - POSITIONAL ONLY ARGUMENT - ##########################
"""
def fullname(name, surname, /, ort):
    print(f'{name} {surname} {ort}')


fullname('yasar', 'ince', ort='berlin')
fullname('fatih', 'keriz', ort='hamburg')
"""


##################### - Neu support in Pyhton - #####################
import math


name = 'fatih'
print(f'{name=}') # name='fatih'



# math.prod()
print(math.prod((2, 3, 4, 5))) # 120 prod fonk carpma islemi yapar



# math.isqrt()
print(math.sqrt(15)) #3.872983346207417 sayinin karekokunu alir


# math.pep()