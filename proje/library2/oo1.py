from os import name


class Product:
    def __init__(self, name, amount):
        self.__name = name
        self.amount = amount

    def get_name(self):
            return self.__name

    def set_name(self, name):
        self.__name = name



class Book(Product):
    def __init__(self, name, amount, author, publisher):
                super().__init__(name, amount)
                self.author = author
                self.publisher = publisher


    def __str__(self):
        return f'Kitap : {self.get_name()} - Yazar : {self.author} - Yazar : {self.publisher} - Miktar : {self.amount}'


books= []


def new_book():

    name = input('kitap ismi giriniz')
    author = input('yazar ismi giriniz')
    publisher = input('yayinevi ismi giriniz')
    amount = input('miktar bilgisini giriniz')

    book = Book(name=name, author=author, publisher=publisher, amount=amount)
    books.append(book)


def display_book():
    search_name = input('kitap ismi giriniz')
    book = find_book(search_name)
    
    if book != None:
         print(book)
         print('=======================================')
    else:
        print('aradiginiz kitap bulunamadi')



def edit_book():
    '''kitap duzenleme'''
    search_name = input('kitap ismi giriniz : ')
    book = find_book(search_name)

    if book != None:
        print('Kitap Ismi : ', book.get_name())
        new_name = input('yeni kitap ismi giriniz, ayni kalmasi icin . giriniz')
        if new_name !='.':
            book.set_name(new_name)
        new_author = input('yeni yazar ismi giriniz, ayni kalmasi icin . giriniz')
        if new_author !='.':
            book.author = new_author
        new_publisher = input('yeni yayinevi ismi giriniz, ayni kalmasi icin . giriniz')
        if new_publisher !='.':
            book.publisher = new_publisher
            new_amount = input('yeni miktar bilgisini giriniz, ayni kalmasi icin . giriniz')
        if new_amount !='.':
            book.amount = new_amount

    else:
        print('aradiginiz kitap bulunamadi')

   

def find_book(search_name):
    search_name = search_name.strip()
    search_name = search_name.lower()

    for book in books:
        name = book.get_name()
        name = name.strip()
        name = name.lower()
        if name.startswith(search_name):
            return book
    return None
         

         
def delete_book():
        x = input('kitap ismi giriniz')
        for book in books:
            if book.name == x:
                x.remove(book)
                print('kitap silindi')
            else:
                print('islem basarisiz')
                


menu = '''KITAP LISTESI
1- KITAP EKLE
2- KITAP ARA
3- KITAP DUZENLE
4- KITAP SILME
5- EXIT

KOMUT GIRDINIZ :'''

while True:
    command = int(input(menu))
    if command == 1:
        new_book()
    elif command == 2:
        display_book()
    elif command == 3:
        edit_book()
    elif command == 4:
        delete_book()
    elif command == 5:
        break