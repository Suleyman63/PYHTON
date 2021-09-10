class Employee:
    def __init__(self, name, age):
        self.__name = name
        self.age =age

    def get_name(self):
            return self.__name

    def set_name(self, name):
            self.__name = name

employee1 = Employee('Hakn', 23)
employee2 = Employee('aliy', 33)

print(f'Isim : {employee1.get_name()} Yas : {employee1.age}')
print(f'Isim : {employee2.get_name()} Yas : {employee2.age}')



employee1.set_name('hakan')
employee2.set_name('ali')

print(f'Isim : {employee1.get_name()} Yas : {employee1.age}')
print(f'Isim : {employee2.get_name()} Yas : {employee2.age}')