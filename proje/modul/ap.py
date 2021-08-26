import modul

wahl = int(input("wahlen sie eine operation\n1-PRIME NUMMER AUSFUHRUNG\n2-COLLATZ AUSFUHRUNG\n3-SCHALTJAHR AUSFUHRUNG\n4-EXIT"))


if wahl == 1:
  x = int(input("enter a prime number"))
  print(modul.is_prime(x))
elif wahl == 2:
    a = int(input("enter a collatz number"))
    print(modul.is_collatz(a))
elif wahl == 3:
  jahr=int(input("Geben sie ein Jahreszahl ein."))
  print(modul.is_Schaltjahr(jahr))
elif wahl == 4: 
   print("exit")
else:
    print("falsch")



#with open("data.txt", "w") as f: 
 #   f.write(modul)

