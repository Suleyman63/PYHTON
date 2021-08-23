

# FOOR LOOP


"""
for j in range(0, 20):
     if j == 12:
      print(j)
      break
"""
      
      
"""
  for j in range(1, 6):
  if j == 3:
    continue
print(j)
"""      
        
        
        
"""        
for x in range(2, 6):
  print(x)
 """       
        
        
"""for x in range(6):
  print(x)
else:
  print("Finally finished!")
"""


"""        
for x in range(6):
  if x == 4: break
  print(x)
else:
  print("Finally finished!")
"""     
  
  
"""      
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x)
    print(y)
"""
  
"""
for x in range(2, 30, 3):
  print(x)  
        
"""       

        
#name = "sebastian"
 #for x in name:
  #  if x == "e":
   #     continue
#print(x.upper())
   

#for number in range(2,20,2):
 #    print(number)

"""
kare = []
for num in range(1,11):
    kare.append(num**2)
    print(kare)


kare2 = [num**2 for num in range(1,5)]
print(kare2)
"""


"""
num = [3, 5, 7, 9, 11]

for x in num:
      print(x)
"""

"""
friends = ['ahmet', 'mehmet', 'ali', 'veli', 'ebru']

for x in friends:
      print(x)
"""


"""
fruits = ["apple", "banana", "cherry"]

for x in fruits:
      print(x)
"""


"""
name = 'alislalskkjs'

for x in name:
      print(x)
"""

"""
for x in range(1, 15, 2):
  print(x)
"""


"""
friends = {'ahmet': 34, 'mehmet': 23, 'ali': 45, 'veli': 21, 'ebru': 33}

#sadece key leri gosterir
for x in friends.keys():
  print(x)

#sadece value degerini gosteririr
for y in friends.values():
  print(y)

# iki degeri birlikte aldik
for x, y in friends.items():
  print(x, y)


#sadeece ahmeti gosterdi
for x, y in friends.items():
      print(x, y)
      if x == 'ahmet':
       break
      print(x, y)


# ahmet haric digerlerini gosterdi
for x, y in friends.items():
      print(x, y)
      if x == 'ahmet':
       continue
      print(x, y)
"""

# ENUMARETE
"""
# enumarate fonk kendiliginden 0 dan baslayarak degerlere numara veirir

friend = {'ahmet', 'mehmet', 'ali', 'veli', 'ebru'}

for i, friend in enumerate(friend):
  print(i, friend)
"""


"""
minNum = int(input('min num gir'))
maxNum = int(input('max num gir'))

for x in range(minNum, maxNum):
  if x % 2 != 0:
    continue
  else:
    print(x)
"""


"""
celciuses = [20, 25, 30, 35]
kelvin = []
fahrenheit = []

for c in celciuses:
  k = c + 273
  kelvin.append(k)
  f = c * 9 / 5 +32
  fahrenheit.append(f)

  
  print(kelvin)
  print(fahrenheit)
"""



