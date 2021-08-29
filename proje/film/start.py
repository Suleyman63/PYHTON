from os import name
from proje.film.db import get_movie
import db


user_options ="""

1-ekle
2-listele
3-duzenle
4-sil
0-cikis
"""

def main():
    user_input = input(user_options)
    while user_input != '0':
        if user_input == '1':
            add_movie()
        elif user_input == '2':
            list_movie()
        elif user_input == '3':
            watched_movie()
        elif user_input == '4':
            watched_movie()       
        else:
            print('falsh geduruckt')

    user_input = input(user_options)



def add_movie():
    name = input(' film name')
    director = input('director name')

    db.fl_add_movie(name, director)


def list_movie():
    movies = db.get_movie()
    for movie in movies:
        print(f"movies: {movie['name']}, {movie['director']}")


def watched_movie():
    name = input('duzenlemek istediginiz filmin adini yaziniz')
    db.watched_movie(name)


def delete_movie():
    name = input('silmek istediginiz filmin adini yaziniz')  
    db.fl_delete_movie(name)
    
main()