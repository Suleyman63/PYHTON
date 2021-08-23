# INHERITANCE
"""
class Student:

    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

        def average(self):
            return sum(self.grades) / len(self.grades)
       
       
    class UnivStudent(Student):
        def __init__(self, name, age, grades, university):
          super.__init__(name, age, grades)
          self.university = university
        

    u_student_1 = UnivStudent('kerim', 22, [10, 50, 90], 'ITU')

    print(u_student_1.university)
    print(u_student_1.average())
"""


"""
class Circle:
    pi = 3.14

    def __init__(self, radius = 1):
     self.radius = radius

    def area(self):
        return self.radius * self.radius * self.pi

    def __repr__(self):
        return f'{_class_._name_} object with {self.radius} radius'

    def _len_(self):
        return self.radius


circle_2 = Circle(8)
print(len(circle_2))
    

circle_1 = Circle(5)
print(circle_1)
print(circle_1.__repr__())
"""


"""
class Student:
    
    def __init__(self, name, surname, age, grades):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = grades
        self.fullname = self.name + ' ' + self.surname

        def average(self):
            return sum(self.grades) / len(self.grades)

        def fullname(self):
            return f'{self.name} {self.surname}'

       
student_1 = Student('kerim', 'kizil', 22, [10, 50, 90])

student_1.name = 'mahmut'
student_1.surname = 'yazilim2'
student_1.grades = [50, 90, 70]


print(student_1.name)
print(student_1.surname)
print(student_1.fullname)
print(student_1.average)
"""


"""
class Dog:
    def __init__(self, name):
        self.name = name

    def myname(self):
        print(f'benim adim {self.name}')

dog_1 = Dog(name='Tom')
print(dog_1.name)


dog_1.name = 'Jo'
print(dog_1.name)
"""


"""
class Dog:
    num_legs = 4

    def __init__(self, name):
       self.name = name

dog_1 = Dog('Tom')
dog_2 = Dog('Kangal')

print(dog_1.name)
print(dog_1.num_legs)
print(dog_2.name)
print(dog_2.num_legs)

print(Dog.num_legs)
print(Dog.name)
"""

"""
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
      return self.name + ' ' + self.surname + ' ' + str(self.age)

person_1 = Person('asim', 'yildiz', 39)
print(person_1.__str__())




class Employee(Person):
    def __init__(self, name, surname, age, salary):
        super().__init__(name, surname, age)
        self.salary = salary

    def __str__(self):
          return super().__str__() + ' ' + str(self.salary)


employee_1 = Employee('kasim', 'keser', 33, 3000)
print(employee_1.salary)
print(employee_1.__str__())

"""


