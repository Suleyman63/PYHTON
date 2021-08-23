capital = ('tahran', 'ankara', 'berlin', 'madrid')
for cap in capital:
    print(cap)

capital=('roma', 'london')
print(capital)

sehirler = {'izmir', 'ankara', 'yalova', 'kars', 'izmir'}
print(sehirler)

print(type(sehirler))

#print(sehirler[0]) # set yapisinda indeksleme yoktur o yuzden hata aldik
 
sehirler.add('adana')
print(sehirler)

sehirler.update(['edirne', 'urfa'])
print(sehirler)

sehirler.remove('ankara')
print(sehirler)

#sehirler.remove('mugla')
#print(sehirler) #KeyError: 'mugla'

sehirler.clear()
print(sehirler)

del sehirler
print(sehirler)