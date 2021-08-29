class Book:
    def __init__(self, name, autor, read):
        self.name = name
        self.autor = autor
        self.read = read

    
    def __repr__(self):
        return f'Book : {self.name}  Autor : {self.autor}'
        