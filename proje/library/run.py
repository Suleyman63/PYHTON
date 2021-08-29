from book import Book
from member import Member

"""
book1 = Book('Ince Mehmed', 'Yasar Kemal', False)
book2 = Book('Birgun Tek Basian', 'Vedat Turkali', True)
book3 = Book('Dostoyevski', 'Suc ve Ceza', True)

print(book1)
print(book2.name)
print(book3.autor)
"""

member1 = Member('ali')

#print(member1.read_book())

member1.add_book('Suc ve Ceza', 'Dostoyevski')
member1.add_book('Birgun Tek Basian', 'Vedat Turkali')
member1.add_book('Bir Omur Nasil Yasanir', 'Ilber Ortayli')
#print(member1.books)


#member1.delete_book('Suc ve ceza')
#print(member1.books)

member1.save_to_file()