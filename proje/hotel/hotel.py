import random

import json


raumno = []
person = [
 {
  "name":"",
  "phone":"",
  "adresse":"",
  "checkin":"",
  "checkout":""
  }]

try:
   with open("guru99.txt", "w") as f:
    json.dump(person, f)
except IOError:
    print("except")
finally:
    f.close()


  
# Home Function
def Home():
    
    print("***************************************")
    print("               - HALLO -               ")
    print("***************************************")
    print("      - WAS MOCTEN SIE TUN? -          ")
    print("***************************************")
    print("---> 1    Hotel Rezervation            ")
    print("---> 2    Raum Info                    ")
    print("---> 3    Restaurant Info              ")
    print("---> 4    Registriren                  ")
    print("---> 5    Exit                         ")


    wahl=int(input("Ihre wahl"))
  
    if wahl == 1:
        Rezervation()
        print("Hotel Rezervation") 
    elif wahl == 2:
        print("Raum Info")
        Raum_Info() 
    elif wahl == 3:
        print("Raum Info")
        restaurant()
    elif wahl == 4:
        print("Raum Info")
        Register()     
    elif wahl == 5:
        print("EXIT")
        exit()
    else:
        print('wahl nicht moglisch')
print("********************************************")

def Rezervation():
        print("---   RAUM WAHLEN ---")
        print("--->   1. ETAGE      ")
        print("--->   2. ETAGE      ")
        print("--->   3. ETAGE      ")
        print("--->   4. ETAGE      ")


        c=int(input("->"))
        if c==1:
            print("========> 1-ETAGE PRICE 100 $")
            raumno = random.randrange(1, 20)
            print('=======> RAUM NO : ', raumno)
            Register()
        elif c==2:
            print("========> 2-ETAGE PRICE 150 $")
            raumno = random.randrange(1, 20)
            print('========> RAUM NO : ', raumno)
            Register() 
        elif c==3:
            print("========> 3-ETAGE PRICE 200 $")
            raumno = random.randrange(1, 20)
            print('========> RAUM NO : ', raumno)
            Register()
        elif c==4:
            print("========> 4-ETAGE PRICE 250 $")
            raumno = random.randrange(1, 20)
            print('========> RAUM NO : ', raumno)
            Register()
        else:
            print("Flasch wahl")

print("********************************************")
 
# ROOMS INFO
def Raum_Info():

            print("*************************************************************************")
            print("                          HOTEL RAUMS INFO                               ")
            print("*************************************************************************")
            print("Room amenities include: 1 Double Bed, Television, Telephone              ")
            print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and            ")
            print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and            ")
            print("An attached washroom with hot/cold water                                 ")
            print("Room amenities include: 1 Double Bed, Television, Telephone              ")
            print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and            ")
            print("an attached washroom with hot/cold water + Window/Split AC               ")

            print()
            n=int(input("0- BACK\n1- EXIT"))
            if n==0:
                Home()
            elif n==1:
                exit()
            else:
                print('falsch wahl')

print("********************************************")


# RESTAURANT FUNCTION
def restaurant():


            print("-------------------------------------------------------------------------")
            print("                          RESTAURANT                                     ")
            print("-------------------------------------------------------------------------")
            print("                            Menu Card                                    ")
            print("-------------------------------------------------------------------------")
            print(" 1  Tea............................................................ 20.00")
            print(" 2  Cola........................................................... 25.00")
            print(" 3  Coffee......................................................... 25.00")
            print(" 4  Beer........................................................... 25.00")
            print(" 5  Bread Butter................................................... 30.00")
            print(" 6  Bread Jam...................................................... 30.00")
            print(" 7  Veg. Sandwich.................................................. 50.00")
            

            n=int(input("0- BACK\n1- EXIT"))
            if n==0:
                Home()
            else:
                exit()
        
print("********************************************")
# RECORD FUNCTION
def Register():

            print("        *** REZERVATION REGISTRIREN ***")
            print("| Name        | Phone No.    | Addresse       | Chek-in | Check-out |")
            print("---------------------------------------------------------------------")

            if raumno == []:
                name = input('name')
                person.append(name)
                phone = int(input('phone'))
                person.append(phone)
                adresse = input('adresse')
                person.append(adresse)
                checkin = int(input('check-in'))
                person.append(checkin)
                checkout = int(input('check-out'))
                person.append(checkout)
                print('NAME :', name, '\nPHONE :', phone,'\nADRESSE :', adresse, '\nCHECK-IN :', checkin, '\nCHECK-OUT :', checkout)
                print('*********** REGISTER SUCCSESFULLY ************')
            else:
                print("zimmer ist full")

            n = int(input("0- BACK\n1- EXIT"))
            if n == 0:
                    Home()  
            else:
                    exit()



Home()

