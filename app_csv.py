import csv

#reader
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

"""
#writer
with open('data.csv', 'w', newline='') as file:
    fieldnames = ['player_name', 'fide_rating']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'player_name': 'Magnus Carlsen', 'fide_rating': 2870})
    writer.writerow({'player_name': 'Fabiano Caruana', 'fide_rating': 2822})
    writer.writerow({'player_name': 'Ding Liren', 'fide_rating': 2801})
"""


try:
    with open('data.txt', 'r') as f:
        content = f,read()
except FileNotFoundError:
    print('dosya bulunamadi')