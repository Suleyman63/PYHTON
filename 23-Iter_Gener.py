# generator yield anahtar kelime
"""
def odds(limit):
    for odd in range(1, limit+1, 2):
        yield odd

print(odds)
print(odds(15))

my_odds = odds(15)
print(my_odds)
print(next(my_odds))
print(next(my_odds))
print(next(my_odds))


list1=['a', 'b', 'c', 'd']
my_gen = (char for char in list1)

print(my_gen)
print(next(my_gen))
print(next(my_gen))
"""
################# - ubung - ###########################
#numbers = [1,2,3,4,5,6]
#friends = ['ali', 'mehmet', 'ayse']

#for n in numbers:
 #   print(n)

"""
def my_for_loop(my_iterable):
     my_iterable = iter(my_iterable)
     while True:
        try:
             print(next(my_iterable))
        except StopIteration:
            break
my_for_loop(numbers)
my_for_loop(friends)
"""

"""
# kendi iteration clasmizi yazdik
class CubedNumbers:

    def __init__(self, start, end):
        self.start = start
        self.end = end


    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            result = self.start **3
            self.start +=1
            return result
        else:
           raise StopIteration

cubed = CubedNumbers(0,5)
print(next(cubed)) # 0
print(next(cubed)) # 1
print(next(cubed)) # 8
print(next(cubed)) # 27
print(next(cubed)) # 64
print(next(cubed)) #125
"""

"""
# generator expresion yontemi ile sayilarin kupunu aldik
cubed = (x**3 for x in range(0,5))
print(next(cubed)) # 0
print(next(cubed)) # 1
print(next(cubed)) # 8
print(next(cubed)) # 27
"""


"""
# fibonacci sorusu

def fibbo(limit):
    x = 0
    y = 1

    while x < limit:
        yield x
        x, y = y, x+y

my_fibo = fibbo(100)


for fib in my_fibo:
    print(fib)
"""


"""
friends = ['ali', 'mehmet', 'kemal', 'osman']


#1. yontem
i=0
while i < len(friends):
    v = friends[i]
    print(i,v)
    i += 1


# 2. yontem
ii = 0
for  ii in range(len(friends)):
    vv = friends[ii]
    print(ii, vv)


# 3. yontem
for i,v in enumerate(friends):
    print(i, v)
"""