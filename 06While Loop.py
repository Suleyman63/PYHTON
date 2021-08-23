# WHILE LOOP

"""
nummer = 1

while nummer <= 10:
    print("nummer: ", nummer)
    nummer += 1
    
        
i = 4

while i < 10:
    print(i)
    i +=1


   
i = 1
while i < 6:
  print(i)
  i += 1
  
  
  
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 
        
        
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  
  
i = 100
while i > 0:
      print(i)
      i -= 1
   
    
x = 0
result = 0

while x <= 100:    
    x+=1
    if x % 2 == 0:
        continue
    result += x

print(f'sum: {result}')
    
   
   
x = 1
while x <= 100:
    if x % 2==1:
        print(f'tek sayilar : {x}')
    else:
        print(f'çift sayilar : {x}')
    x += 1

print('finish...')



while True:
    password = input("password eingeben: ")

    if not password:
        print("password required!")

    elif len(password) in range(3, 8):
        print("Neu password", password)
        break

    else:
        print("password muss 3 - 8 sein")
        
     
        
while True:
    num = int(input("zahl eingeben: "))

    if num == 0:
        break

    elif num < 0:
        pass

    else:
        print(num)     
        
        

while True:
    pas = input("password eingeben")
    if len(pas) < 5:
        print("pass muss mindestens 6 sein")
    else:
            print("ihr password : ", pas)
            break
            
            
            
            numbers = []
i = 0
while i<5:
    sayi = int(input('sayı: '))
    numbers.append(sayi)
    i+=1
numbers.sort()
print(numbers)




product = []

num = int(input('kaç ürün eklemek istiyorsunuz: '))

i = 0

while(i<num):
    name = input('ürün ismi: ')
    price = input('ürün fiyatı: ')
    product.append({
        'name': name,
        'price': price
    })
    i += 1

for urun in product:
    print(f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')




num = [1,3,5,7,9,12,19,21]

i = 0
while (i < len(num)):
    print(num[i])
    i += 1

"""

"""
num = 1

while num <= 10:
    print(num)
    num += 1
"""

"""
message = ''

while message != 'Q':
    message = input('quit yazana kadar devam eder')
    print(message)
"""

"""
m = 3

while m < 20:
    print(m)
    m += 1

"""


"""
m = True
x = ''

while m:
    print('q a basinca durur')
    if m == 'q':
        m = False
    else:
        print(x)

"""

"""
num = 1

while num < 10:
    print(num)
    if num == 5:
        break
    num += 1

"""

"""
num = 1

while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)
"""

"""
    num2 = 1

    while num2 < 20:
        num2 += 1
        if num2 % 2 == 1:
            continue
        print(num2)
"""

"""
friends = {'ahmet', 'mehmet', 'ali', 'veli', 'ebru'}


x = 0
while (x < len(friends)):
    friend = friends[x]
    x = x + 1
    if friend == 'mehmet':
        continue
    print(friend)


for a in friends:
    if friends == 'mehmet':
        continue
    print(a)
"""

"""
# sayi tahmin oyunu
import random
num = random.randint(1, 100)

num1 = int(input('1-100 arasinda sayi gir'))

while num1 != num:
      if num1 < num:
        print(f'{num1} daha buyuk bir sayi giriniz')
        num1 = int(input())
      else:
        print(f'{num1} daha kucuk bir sayi gir')
        num1 = int(input())

print(f'Tabrikler {num1} numarayi bildiniz')

"""


"""
# sayi azalarak ve bir onceki sayilari toplayip geliyor
num = int(input('bir sayi giriniz'))

if num < 0:
    print('sayi negatif')
else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1
        print('toplam sayi', sum)
"""