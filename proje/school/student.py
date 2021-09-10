import json

# class Student:
#     def __init__(self, ad, soyad, yas):
#         self.ad=ad
#         self.soyad = soyad
#         self.yas = yas

def ekleme():
    print('OGRENCI EKLEME SECILDI')
    ad=input('name')
    soyad=input('surname')
    yas=int(input('age'))
         
    with open('okul.json', 'w') as f:
        json.dump((ad, soyad,yas), f)
       


def silme():
    print('OGRENCI SILME SECILDI')
    ad=input('silmek istidiginiz kisinin adini giriniz')
    if ad != ad.get():
            print('bulunamadi')
    else:
        with open('data.json') as f:
            data = json.load(f)
        for element in data: 
            del element[ad]



def arama():
    database = "okul.json"
    data = json.loads(open(database).read())
    ad = data[0]['ad']
    print(ad)



def listele():
    print('OGRENCILER LISTELENDI')
    with open('okul.json', 'r') as f:
       obj=json.load(f)
    print(obj)



def guncelle():
    print('OGRENCI GUNCELLEME SECILDI')
    ad=input('name')
    soyad=input('surname')
    yas=int(input('age'))


    with open('okul.json', "r+") as f:
        data = json.load(f)
        data.append(ad, soyad, yas)
        f.seek(0)
        json.dump(data, f)




def menu():
    
    while True:
        print('1-EKLEME')
        print('2-SILME')
        print('3-ARAMA')
        print('4-LISTELE')
        print('5-GUNCELLE')
        print('6-CIKIS')

        print('============ YAPMAK ISTEDIGINIZ ISLEMI SECINIZ =============')
        secim=int(input('secim'))

        if secim==1:
            print('EKLEME')
            ekleme()
        elif secim==2:
            print('SILME')
            silme()
        elif secim==3:
            print('ARAMA')
            arama()
        elif secim == 4:
            print('LISTELEME')
            listele()
        elif secim == 5:
            print('GUNCELLEME')
            guncelle()   
        elif secim == 6:
            print('CIKIS YAPILIYOR') 
            break          
        else:
            print('YANLIS GIRIS')

menu()