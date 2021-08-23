# TRY EXCEPT

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