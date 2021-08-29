movies_file = 'movies.csv'

def fl_add_movie(name, director):
    with open(movies_file, 'a') as f:
        f.write(f'{name}, {director}, {False}\n ')


def get_movie():
    with open(movies_file, 'r') as f:
        lines = []
        for line in f.readlines():
            lines.append(line.strip().split(', '))
    return [{'name':line[0], 'director': line[1], 'watched':line[2]} for line in lines]


def watched_movie(name):
    movies = get_movie()
    for movie in movies:
        if movie['name'] == name:
            movie['watched'] = True

    _save_movie(movies)

def _save_movie(movies):
    with open (movies_file, 'w') as f:
        for movie in movies:
            f.write(f"{movie['name']}, {movie['director']}, {movie['watched']}\n")


def fl_delete_movie(name):
    movies = get_movie()
    movies=[movie for movie in movies if movie['name'] != name]
    _save_movie()