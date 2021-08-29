#################### - all - ########################################################
"""
list1 = [0, 4, 5, 8]
print(all(list1)) # False

list2=[3, 5, 7, 9]
print(all(list2)) # True

list3 = [True, False]
print(all(list3)) # false

list4= [True, True, True, 0]
print(all(list4)) # false

dict2 = {1: True, 0:True}
print(all(dict2)) #false


friends = ['ayse', 'ahmet', 'ayhan', 'ali']
print(all([friend[0] == 'a' for friend in friends])) # true


friends = ['ayse', 'ahmet', 'ayhan', 'ali', 'mehmet']
print(all([friend[0] == 'a' for friend in friends])) # false

"""
#################### - any - ########################################################
"""
list1 = [0, False, False, 8]
print(any(list1)) # true

list2 = [0, False, False, 8]
print(all(list2)) # false


dict3 = {1: True, 0:True}
print(any(dict3)) #true


friends = ['ayse', 'ahmet', 'ayhan', 'ali']
print(any([friend[0] == 'a' for friend in friends])) # true

friends = ['ayse', 'ahmet', 'ayhan', 'ali', 'kemal']
print(any([friend[0] == 'a' for friend in friends])) # true

mytuple = (0, 1, False)
print(any(mytuple)) # True

mydict = {0: 'apple', 0:'orange'}
print(any(mydict)) # false

myset = {0, 2, 0}
print(any(myset)) # true

"""
######################## - Max - Min - ###########################################
"""
print(max(3, 6, 77, 99, -120, 45)) #99
print(min(3, 6, 77, 99, -120, 45)) # -120

print(max('a', 'v', 's', 'r')) # v
print(min('a', 'v', 's', 'r')) # a

print(max('ayse', 'ahmet', 'ayhan', 'ali', 'kemal')) # kemal
print(min('ayse', 'ahmet', 'ayhan', 'ali', 'kemal')) # ahmet

print(max('cumhuriyet')) # y
print(min('cumhuriyet')) # c

liste3 = [23, -12, 45, 87]
print(max(liste3)) #87
print(min(liste3)) #-12
"""

######################## - sorted - ###########################################
"""
# sort()

number = [23, -12, 45, 87, 99, 54]
print(number) # [23, -12, 45, 87, 99, 54]
number.sort()
print(number) # [-12, 23, 45, 54, 87, 99]

# sorted()
number2 = [43, -76, 15, 27, 39, 74]
print(number2)    #[43, -76, 15, 27, 39, 74]
print(sorted(number2)) # [-76, 15, 27, 39, 43, 74]
print(number2)  # [43, -76, 15, 27, 39, 74]

print(sorted(number2, reverse=True)) #[74, 43, 39, 27, 15, -76]
print(sorted(number2, reverse=False)) #[-76, 15, 27, 39, 43, 74]

friends4 = ['ayse', 'vhmet', 'tyhan', 'bli']
print(sorted(friends4)) # ['ayse', 'bli', 'tyhan', 'vhmet']
print(sorted(friends4, reverse=True)) #['vhmet', 'tyhan', 'bli', 'ayse']
print(sorted(friends4, reverse=False)) #['ayse', 'bli', 'tyhan', 'vhmet']
print(sorted(friends4, key=len, reverse=True)) #['vhmet', 'tyhan', 'ayse', 'bli']
"""

######################## - reversed - ###########################################
# reverse()
nummer3 = [3, 4, 6, 7, 9]

print(nummer3) # [3, 4, 6, 7, 9]
nummer3.reverse()
print(nummer3) # [9, 7, 6, 4, 3]

#reversed()
nummer4 = [3, 4, 6, 7, 9, 66, 77]

print(nummer4) # [3, 4, 6, 7, 9, 66, 77]
print(list(reversed(nummer4))) #[77, 66, 9, 7, 6, 4, 3]

string = 'Python'
print(list(reversed(string))) #['n', 'o', 'h', 't', 'y', 'P']

