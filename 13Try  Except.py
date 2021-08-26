# TRY EXCEPT

import time

"""
NameError, TypeError, ZeroDivisionError, IOError, IndexError, ValueError, KeyboardInterrupt

try:
    birtakım kodlar
except ValueError:
    print("Yanlış değer")
except ZeroDivisionError:
    print("Sıfıra bölme hatası")
except:
    print("Beklenmeyen bir hata oluştu!")


giriş = input("Merhaba! Adın ne? ")
if len(giriş) == 0:
    raise AssertionError("İsim bölümü boş.")
print("Hoşgeldiniz.")
"""

"""
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


bölünen = int(input("bölünecek sayı: "))

if bölünen == 23:
    raise Exception("Bu programda 23 sayısını görmek istemiyorum!")

bölen = int(input("bölen sayı: "))
print(bölünen/bölen)
"""

"""
a = 5
b = 0
c = a / b
print(c) #ZeroDivisionError: division by zero


a = 5
b = 0

try:
    c = a / b
    print(c)
except:
    print('Try  Except: von 5 / 0 war nicht moglich')
    



# Thema Casting und Fehlerbehandlung

#ort = "berlin"
#zahl = int(ort) #ValueError: invalid literal for int() with base 10: 'berlin'



ort = "berlin"
try:
    zahl = int(ort)
    print = (zahl)
except:
    print(ort + ' ist keine zahl')
finally:
    print("Überprüfung ist beendet")
    


while True:
    try:
        a = float(input("a: "))
        break
    except:
        print("Please input a number")
        
while True:
    try:
        b = float(input("b: "))
        break
    except:
        print("Please input a number")


try:
    print(a / b)
    
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
    
"""


"""
try:
    zahl1 = int(input('zahl eingeben'))
except ValueError:
    print('eingabe muss int sein')
except:
    print('excep fehler')
"""

"""
def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('division error')
    except TypeError:
        print('type err')
    except:
        print('das klappt nicht')
print(division(0, 2))

"""

"""
try:
    print(2 / 'Haus')
except Exception as e:
        print('ein fehler')
        if e.__class__ == ZeroDivisionError:
            print('hier wurde durch 0 geteilet')
        else:
            print('andere fehler')
"""


"""

count = 0

if __name__ == '_main_':
    try:
        while count < 10:
            print(count)
            count += 1
            time.sleep(1)
    except KeyboardInterrupt:
        print('abgebrochen')
    finally:
        print('ich raume auf')
        #f.close() finnallyde f.close eklemek gerekir

"""