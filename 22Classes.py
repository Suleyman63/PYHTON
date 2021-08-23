# OOP Consept

"""
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

        def brandmodel(self):
            return f'Arabanin markasi {self.brand} ve modeli {self.model}'


car1 = Car('BMW', 'X6', 2010)
car2 = Car('AUDI', 'I7', 2021)


print(car1)
print(car1.brand)

print(car1.brandmodel())

"""

"""
class Movie:
    def __init__(self, name, director):
        self.name = name
        self.director = director

Movie_1 = Movie('Full Metal jacket', 'Kubrick')
Movie_2 = Movie('Babel', 'Irerutu')

print(Movie_1.director)
print(Movie_2.director)
"""



class Student:

    school_name = 'Fransiz Lisesi'
    number_of_students = 0


    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
        Student.number_of_students +=1 


    def average(self):
        return sum(self.grades) / len(self.grades)

    def schoolname(self):
        return f' okulumuzun adi {self.school_name}'


    @classmethod
    def display_school_name(cls, name_of_school):
       cls.display_school_name = name_of_school


    @staticmethod
    def statik():
        return f'sadece bu mesaji gonderiyorum'
        

Student.display_school_name = 'Alman Llisesi'

Student_1 = Student('mahmut', 33, [14, 26, 72, 85])
Student_2 = Student('mehmet', 44, [22, 34, 54, 33])



Student_1.school_name = 'Ingiliz Lisesi'

print(Student.school_name)
print(Student_1.school_name)
print(Student_2.school_name)

print(Student.number_of_students) #2


print(Student_1.name)
print(Student_2.name)


print(Student_1.age)
print(Student_2.age)


print(Student_1.average())
print(Student_2.average())


print(Student_1.schoolname())
print(Student_2.schoolname())


print(Student_1.__dict__)
print(Student_2.__dict__)


print(Student_1.average())
print(Student_2.average())

