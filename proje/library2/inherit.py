class Warehouse:
    def __init__(self, amount):
        self.amount = amount



class Product:
    def __init__(self, name):
        self.name = name


class Book(Product, Warehouse):
    def __init__(self, name, amount, author):
        Product.__init__(self, name)
        Warehouse.__init__(self, amount)
        self.author = author


    def __str__(self):
       return f'Kitap : {self.name} - Yazar : {self.amount} - Miktar : {self.author}'


class Movie(Warehouse, Product):
            def __init__(self, name, amount, director):
                    Product.__init__(self, name)
                    Warehouse.__init__(self, amount)
                    self.director = director

            def __str__(self):
                return f'Kitap : {self.name} - Miktar : {self.amount} - Yonetmen : {self.director}'

book1 = Book('Kurt Kanunu', 10, 'Kemal Tahir')
movie1 = Movie('Uzak', 5, 'Nuri Bilge Ceylan')
                
