import sqlite3


#connection = sqlite3.connect('friend.db')
#cursor = connection.cursor()

# veri tabani olusturmak icin kullandik
#cursor.execute('CREATE TABLE friends(first_name TEXT, last_name TEXT, age INTEGER)')

# bilgi girisi yapiyoruz
#cursor.execute("INSERT INTO friends VALUES('veli', 'yildiz', 43)")

# sorgu komutlari
#cursor.execute("SELECT * FROM friends WHERE first_name = 'mahmut'")

# veri girisi icin input olusturduk
#first_name = input('first name giriniz')
#last_name = input('last name giriniz')
#age = int(input('yas giriniz'))



# kullanimi tavsiye edilmiyor
#cursor.execute(f"INSERT INTO friends VALUES('{first_name}', '{last_name}', {age})")


#cursor.execute(f"INSERT INTO friends VALUES(?, ?, ?)", (first_name, last_name, age))


#dictioniray yontemi ile veri girisi
#cursor.execute(f"INSERT INTO friends VALUES(:first, :last, :age)", {'first': first_name, 'last': last_name, 'age': age})

# farkli bir sorgu yontemi
#cursor.execute("SELECT * FROM friends WHERE first_name = ?", ('serkan', ))

# ilk uc veriyi gosterdik
#cursor.execute("SELECT * FROM friends")
#print(cursor.fetchmany(3))

# siraladik
#cursor.execute("SELECT * FROM friends ORDER BY first_name DESC")
#print(cursor.fetchall())

# serkan kisisini sildik
#cursor.execute("DELETE FROM friends WHERE first_name=?", ('serkan',))
#print(cursor.fetchall())


# soyismi yilmaz olanlari inan yaptik
#cursor.execute("UPDATE friends SET last_name=? WHERE last_name=?", ('inan', 'yilmaz'))
#print(cursor.fetchall())


###########################################################################################################################################

connection = sqlite3.connect('users.db')
cursor = connection.cursor()

"""
# txt dosyasindaki verileri veri tabanina ekledik
with open('friends.txt', 'r') as f:
    for friend in f.readlines():
        friends = [x.strip() for x in friend.split(',')]
        cursor.execute("INSERT INTO friends (first_name, last_name, age) VALUES (?, ?, ?)", (friends[0], friends[1], friends[2])) 

"""


#users adinda tablo olusturduk
#cursor.execute(f"CREATE TABLE users (user TEXT, pass TEXT)")



# username ve password sisteme ekledik
username = input('username')
password = input('password')

#cursor.execute(f"INSERT INTO users (user, pass) VALUES ('{username}', '{password}')")



# sifre ve username kontrolu yaptik
cursor.execute(f"SELECT * FROM users WHERE user ='{username}' AND pass='{password}' ")

if(cursor.fetchone()):
    print('giris basarili')
else:
    print('giris basarisiz')



connection.commit()
connection.close()