# IMPORT & MODULE

# FILES (OPEN; WRITE)
# TRY/EXCEPT

import datetime

import math

import platform

import testmodul 




#********************************* Platform Modul ************************************

x = platform.system()
print(x)

x = platform.version()
print(x)


x = platform.machine()
print(x)

x = platform.processor()
print(x)


#********************************* Math Modul **********************************

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)


#The abs() function returns the absolute (positive) value of the specified number:
x = abs(-7.25)
print(x)



x = pow(4, 3)
print(x)


x = math.sqrt(36)
print(x)


x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1


x = math.pi
print(x)


x = math.factorial(5)
print(x) #120



#********************************* Time Modul ************************************

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


x = datetime.datetime(2020, 5, 17)
print(x)


x = datetime.datetime(2021, 8, 24)
print(x.strftime("%B"))



#**************************************** Test Modul ***********************************

print(testmodul.x)

print(testmodul.person1)

a = (testmodul.person1["age"])
print(a)

