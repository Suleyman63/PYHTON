import re
from sre_constants import RANGE_UNI_IGNORE
from typing import Pattern

"""
result = re.match('a', 'asim') # match
print(result)

result = re.match('a', 'asim') # match
print(result)

result = re.match('n', 'asim') # none
print(result)

result = re.match('x', 'asim') #none
print(result)
"""


"""
sample_text = 'dfghjklöä ertzuio567cvbn fghjkltzuio ertzui567cvbnm'

result = re.search('selim', sample_text)
print(result)
print(result.group())


str1 = "The rain in Spain"
x = re.findall("ai", str1)
print(x)


#Check if "Portugal" is in the string:

x = re.findall("Portugal", str1)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

"""

"""
# findall()
simple = 'asd555fghjk433lö oiuztrexcvbnm555 yxcvbnm,.wertzuiopas555dfghjkl322ghjkl'
result = re.findall(r'\d{3}', simple)
print(result)


# finditer()
simple = 'asd555fghjk433lö oiuztrexcvbnm555 yxcvbnm,.wertzuiopas555dfghjkl322ghjkl'
result = re.finditer(r'\d{3}', simple)
print(result)

for x in result:
    print(x.group())


# fullmatch - stringin bire bir uyusmasi halinde ise yarar
simple = 'asim'
result = re.fullmatch(r'asim', simple)
print(result)

print(result.group()) # asim


# flags
simple = 'ASIM'
result = re.fullmatch(r'asim', simple, flags=re.IGNORECASE)
print(result)

print(result.group()) # ASIM

"""

"""
# telefon numarasi kontrol etme
def check_phone(phone_number):
  pattern = re.compile(r'\d{3} \d{2}-\d{2}$')
  result = pattern.search(phone_number)

  if result:
           return result.group()
  else:
          return 'istenilen sekilde giriniz'

print(check_phone('123 44-55'))
print(check_phone('X123 44-55'))
print(check_phone('123 44-551'))
print(check_phone('1234 44-55'))
print(check_phone('123 44-553afsdf'))
"""

"""
# rakamlari listeden cikariyoruz
test_string = 'ha3537sdjkld shuffwewoi7338 34 dfghjk'

pattern = '\d+'
result = re.findall(pattern, test_string)
print(result)
"""


"""
# email control
pattern = re.compile(r''' 
(^[a-zA-Z0-9_.+-]+)
@
([a-zA-Z0-9-]+)
\.
([a-zA-Z0-9-.]+$)S

''', re.VERBOSE)

result = pattern.search('ahmet@gmail.com')
print(result.groups())
print(result.groups())
print(result.groups()[0])

"""