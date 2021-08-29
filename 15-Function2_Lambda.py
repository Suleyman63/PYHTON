# LAMBDA
"""
def func(x):
    return x**2

print(func(5))


kare = lambda a: a**2
print(kare(6))

carpma = lambda k: k*5
print(carpma(10))

cikarma = lambda m, n : m - n
print(cikarma(20, 12))

topla = lambda c, d : c + d
print(topla(34, 23))
"""


"""
j = int(input('bir sayi giriniz'))
s = int(input('bir sayi daha giriniz'))

sum = lambda j, s : j + s
multiply = lambda j, s: j * s

print(f'girilen {j} sayisinin ve {s} sayisinin toplami {sum(j, s)} ve carpimi {multiply(j, s)} dir')
"""


#################### - MAP - ###############################
"""
def sqrt(x): 
    return x**2

print(sqrt(4))
print(sqrt(5))


a = lambda x: x**2
print(a(6))


def sum(x, y):
    return x + y

sum2 =   lambda x,y: x+y

print(sum2(5, 6))
print(sum2(20, 33))



liste = [3, 4, 7, 9]
print(list(map(lambda x: x**2, liste))) #[9, 16, 49, 81]



friends = ['asim', 'mehmet', 'kamil', 'ali']
print(list(map(lambda friend: friend.upper(), friends)))

"""

######################## - FILTER - ################################'
"""
num = [1,2,4,5,7,8,9]
print(list(filter(lambda x: x>3, num))) #[4, 5, 7, 8, 9]

friends = ['asim', 'mehmet', 'kamile', 'ali']
print(list(filter(lambda name: len(name)>5, friends))) # mehmet, kamile

"""

##################### - ubung - #####################################
# iki listenin toplami ve cikarna islemi
#list1 = [3, 12, 34, 5]
#list2 = [5, 7, 8, 9]

#print(list(map(lambda x, y: x * y, list1, list2))) #[15, 84, 272, 45]

#print(list(map(lambda x, y: x + y, list1, list2))) # [8, 19, 42, 14]



## fahrenheit
#fh = [99, 102, 76, 345]

#print([(f-32)*(5/9) for f in fh])



#
#print(list(map(len, [[1], [2,4], [3,2,6]]))) # [1, 2, 3]

#print(list(map(len, [[1], [2], [3]]))) # [1, 1, 1]

#str_list = ['mustafa', 'ali', 'keamll', 'veli']
#print(list(filter(lambda name: len(name) < 4, str_list)))# ['ali']

#
#nummer1 = [9, 1, 7, 4]

# 1. yontem
#print(list(map(lambda x: x+5, nummer1))) #[14, 6, 12, 9]

# 2. yontem
#print([x+5 for x in nummer1]) #[14, 6, 12, 9]




# 
lis1 = [1]
list2 = [1, 2]
list3= [1, 2, 3]

print(max(lis1, list2, list3, key=len))


