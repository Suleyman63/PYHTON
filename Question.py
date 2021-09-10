
######################## -  tek cift sayi -############################
"""
sayi = int(input('sayi gir'))

tek =0
cift=0

for i in range(sayi):
    if sayi %2 == 0:
        cift+= i   
    else:
         cift+= i       
print('cift sayilar', cift)
print('tek sayilar', tek)
"""


##################### - alan cevre hesaplama - ############################
"""
kisa = float(input('sayi gir'))
uzun = float(input('sayi gir'))

print('alan', float(kisa)*float(uzun))
print('cevre', 2* float(kisa)+float(uzun))
"""

#################### - asal sayi bulma -###########################
"""	
sayaç=0
sayı=int(input('Lütfen Bir Sayı Giriniz: '))
for k in range(2,sayı):
      if sayı%k==0:
            sayaç=sayaç+1
            break
if sayaç==0:
      print("SAYI ASAL!!!")
else:
      print("SAYI ASAL DEĞİL!!!")


# 2.yontem
num = 12
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
        else:
            print(num, "is a prime number")
else:
    print(num, "is not a prime number")
"""

########################### - Fibbonaci  - #######################
"""
def Fibonacci(n):  
    if n > 2:
        return Fibonacci(n-1) + Fibonacci(n-2)
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        print("Incorrect input")
 
print(Fibonacci(8))
"""


"""
def main():
    fib1, fib2 = 0, 1
    for _ in range(10):
        print(fib1)
        fib1, fib2 = fib2, fib1 + fib2


if __name__ == '__main__':
    main()
"""
#################################### - Faktoryel - ####################################################
"""
def fact(sayi):
    if sayi <= 1:
        return 1
    else:
        return sayi * fact(sayi - 1)


if __name__ == '__main__':
    sayi = int(input("Faktoriyelini almak istediğiniz sayıyı giriniz: "))

print(fact(sayi))
"""