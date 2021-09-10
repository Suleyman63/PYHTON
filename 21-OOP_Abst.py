"""
from abc import ABC, abstractclassmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractclassmethod
    def salary(self):
        return 5000



class Engineer(Employee):
    def __init__(self, name, title):
        super().__init__(name)
        self.title = title

    def salary(self):
        return 1000


    def __str__(self) -> str:
        return f'isim : {self.name} - maas : {self.salary()}'



eng1 = Engineer('Fatma', 'Engineer')
emp1 = Employee('Hakan')

print(isinstance(eng1, Employee))
print(isinstance(eng1, Employee))

"""
###########################################################
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'isim: {self.name} - yas: {self.age}'

stdn1 = Student('hakan', 23)
print(stdn1.age)

stdn1.age=40
print(stdn1.age)

print(vars(stdn1))

del stdn1.age
print(vars(stdn1))


delattr(stdn1, 'name')
print(vars(stdn1))

print(stdn1)

"""
###############################################################################

"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
            return f'isim: {self.name} - yas: {self.age}'

st1 = Student('Ayse', 33)
st2=st1

print(st1)
print(st2)

print(id(st1))
print(id(st2))

del st1
del st2

print(st1)
print(st2)
"""
#####################################################################
"""
class Student:
    def __init__(selvi, name, age):
        selvi.name = name
        selvi.age = age

    def __str__(selvi):
            return f'isim: {selvi.name} - yas: {selvi.age}'

s1 = Student('veli', 44)
print(s1)
"""

########################## method resolution order #######################################
class A():
    pass

class B(A):
    pass

class C(B):
    pass


class D:
  pass


class E(D, C):
    pass


print(E.__mro__)

