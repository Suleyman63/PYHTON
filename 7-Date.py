import datetime
from time import thread_time


date1 = datetime.date.today()
print(date1)

print(date1.year)
 
print(date1.month)

print(date1.day)

   
print(datetime.MAXYEAR)
print(datetime.MINYEAR)
   

print(date1.weekday())
print(date1.isoweekday())



date2 = datetime.time(10, 11, 12, 897676)
print(date2)
print(date2.hour)
print(date2.minute)
print(date2.second)
print(date2.microsecond)




date3 = datetime.datetime(2000, 12, 22, 17, 55, 52, 7845)
print(date3)
print(date3.year)
print(date3.month)
print(date3.microsecond)


today = datetime.date.today()
birthday = datetime.date(2000, 12, 5)
tdelta = today - birthday

print(tdelta)
print(tdelta.days)
print(tdelta.total_seconds)



datetime1 = datetime.datetime.now()
print(datetime1)

tdelta1 = datetime.timedelta(hours=10)
print(datetime1 + tdelta1)
print(datetime1)