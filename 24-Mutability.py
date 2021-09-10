friends = ['ahmet', 'mehmet']

print(friends) # ['ahmet', 'mehmet']
print(id(friends)) # 2087962572160

friends.append('mustafa')
print(friends)  # ['ahmet', 'mehmet', 'mustafa']
print(id(friends)) # 1900365575616

friends2 =friends
print(friends2)  # ['ahmet', 'mehmet', 'mustafa']
print(id(friends2)) # 1900365575616

name = 'kenan'
print(name)
print(id(name))

nums=[5, 8]
nums2 = nums

nums.append(9)
print(nums)  # 1776023262832
print(id(nums)) # [5, 8, 9]
print(nums2)  # 1776023262832
print(id(nums2)) # [5, 8, 9]

num3 = 10
num4 = num3
num3 = num3 + 10

print(num3)  # 20
print(id(num3)) # 2008401406864
print(num4)  # 10
print(id(num4)) # 2008401406544



my_list = []

for i in range(5):
    my_list.append(['test', 'mehmet'])
    print(my_list)
    print(id(my_list)) # hepsinin id si ayni geldi