

"""

name = "Tick"

if name == "Tick" or name == "Trick" or name == "Track":
    print("Du bist einer der drei Enten!")
    
================================================================================    
    ist_ein = True
    ist_aus = False
    
    
    if not ist_ein:
        print("das licht ist aus")
              
==============================================================================  

username=input("username")
password=input("password")

if username=="admin" and parola=="12345":
    print("succesfully")
else:
    print("Es ist falsch!")
    
  
================================================================================
    
sayi=int(input("nummer"))

if sayi<10 or sayi>99:
    print("Es ist nicht 2 teile")
else:
    print("2 teile")
    
================================================================================    

age = 18
school = 'gymnasium'
result = (age>=18) and (school=='gymnasium')

print(result)

================================================================================

email = 'alex@gmail.com'
password = '1234'
gebenEmail = input('email: ')
gebenPassword = input('password: ')
result = (gebenEmail == email) and (gebenPassword == password)
print(f'succesfully: {result}')

================================================================================

note1 = float(input('note1: '))
note2 = float(input('note2: '))
note3 = float(input('note3 : '))

ort = ((note1+note2)/2)*0.6 + (note3 * 0.4)

print(f'ort: {ort}')

================================================================================

name = input('name: ')
kg = float(input('kg: '))
hg = float(input('lange: '))

index = (kg) / (hg ** 2)

dunn = (index >= 0) and (index<=18.4)
normal = (index>18.4) and (index<=24.9)
fatt = (index>24.9) and (index<=29.9)
obez = (index>=29.9) and (index<=34.9)

print(f'{name} kilo indeksin: {index} dunn: {dunn}')
print(f'{name} kilo indeksin: {index} normal: {normal}')
print(f'{name} kilo indeksin: {index} fatt: {fatt}')
print(f'{name} kilo indeksin: {index} obez: {obez}')

================================================================================

"""

"""
bool1 = True
bool2 = False

print(type(bool1))
print(type(bool2))

a=2
b=True

c=0
d=False
print(c==d)

age = 32
bool3 = age >= 26
print(bool3)


print(3 < 5) #true


print(3==5) # false


a= ['ahmet', 'mehmet']
b= ['ahmet', 'mehmet']
print(a==b) # true
print(b is a) #false

# OR
print(False or False) # false
print(False or True) # true
print(not True) #false

"""















