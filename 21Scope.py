# SCOPE

"""
name = 'ali'
age = 22

def hello():
    name = 'mehmet'
    age = 10
    return f'benim adim {name} ve {age} yasindayim'
  
print(name) #ali
print(hello()) #benim adim mehmet ve 10 yasindayim

print(name) #ali
print(age) # 22

"""

"""
x = 'global'

def func():
    x = 'local'
    return x
print(func()) # local

print(x) # global


y = 'global level'

def enclosing():
    y = 'enclosing level'
    def innerfunc():
        y = 'local level'
        print(y)
        innerfunc()

enclosing()
"""

"""
def myfunc():
    x = 300
    def myinnerfunc():
     print(x)
     myinnerfunc()

myfunc() 

"""

"""
def my_function(n):
    print('I got ', n)
    n += 1
    print('I have :', n)

var = 1
my_function(var)
print(var) # 1
"""


#SHADOWING

"""
def say_my_age(alter):
    print('dein alter', alter)
    alter = alter + 5

def summe():
    global x
    x = x + 4
    print(x)

def subtraktion(x):
    x = x - 2
    print(x)

x = 10
summe(x)
subtraktion(x)
print(x)

alter = 32
say_my_age(99)
print(alter) 

"""

x = 10
def addition():
    global x
    x = 15 + 5

print(x)
addition()
print(x)

addition()
print(x)