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
def parent_func(name):
    the_name = name
    def inner_func():
        print(f'benim adim : {the_name}')


    return inner_func

x_name = parent_func('kamil')
x_name()