#print("hello world")

#x="merhaba"
#print(x)

#mystring = "samanyolu"
#print(mystring)

#name = "ali"
#message = f'merhaba {name}' #merhaba ali
#print(message.format(name)) #merhaba ali


#string = "Mustafa Kemal Ataturk"
#print(len(string)) #21
#print(string[2]) # s
#print(string[0:7]) #mustafa ilk 6 harfi aldi
#print(string.title()) #Mustafa Kemal Ataturk
#print(string.upper()) #MUSTAFA KEMAL ATATURK
#print(string.lower()) #mustafa kemal ataturk
#print(string.count('a')) # 4
#print(string.count('x')) # 0 
#print(string.find('k')) # k harfi 20. inci sirada
#print(string.replace('Kemal', 'suleyman')) #Mustafa suleyman Ataturk

#print(dir(string)) # methodlara ulasmak icin
#print(help(string)) # bilgi almak icin


# String Formatting


#name="teo"
#wohnort="berlin"
#alter=34
#slogan="""Dann geh doch zu Netto"""

#print(name)
#print(slogan)

#print("mein  name ist %s. ich bin %s jahre alt und wohne in %s." % (name, alter, wohnort))




#multiline-string OHNE Variablen-Zuweisung werden in pyhton ignoriert und konne als
#workdaround als mehrzeilige kommentera genutz werden


#print(name)
#print(vorname)
#print("wie geht es dir)
#print(type(name))
#print(type(slogan))


#neu weg string f

#print(f"die summe aus 3+4 ist{3+4}")



#name = input('bitte geben sie ihr name')
#groß = int(input('bitte geben sie ihr groß'))
#password = input('bitte geben sie password')

#if password == 'prens':
 #   if(groß <= 160):
  #      print(f'{name} du sollst 100 {groß} Taler bezahlen')
   # elif(groß > 160):
    #    print(f'{name} du sollst 110 {groß} Taler bezahlen')
#else:
 #   print(f'{name} du musst nach Hause gehen')