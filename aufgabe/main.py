import modul

"""
lagere die Funktionen is_prime(), is_collatz() und is_schaltjahr() in die Datei tasks.py in den Subordner modulordner aus
 alle drei Funktionen liefern lediglich ein True oder False return-Wert zurück, welcher in der app.py für print()-Statemetns verwendet werden soll
 Erstelle eine Programm-Schleife, die zuerst untenstehende Optionen abfragt und (wenn es sich um eine Operation-Auswahl handelt) nach einer ganzen Zahl > 0 fragt.
 Führe mit dieser Zahl die vom User gewählte Operation durch
 Logge diese Operation in einer aufgabe.txt inkl. eines Zeitstempels und der benutzten Zahl
 sollte der User die 4 auswählen, soll die letzte (also aktuellste) Operation aus der aufgabe.txt ausgegeben werden
 sollte der User die 0 auswählen, wird das Programm beendet und der User verabschiedet
Für Sprinter
 Sichere die User-Eingabe der natürlichen Zahl mit ein try und except ab
 Stell mit einer Schleife sicher, dass erst eine natürliche Zahl eingegeben werden muss, bevor der restliche Code ausgeführt wird
 Sichere den Fall ab, falls der User als zu wählende Operation z.B. 5 oder Hauseingibt
Hinweise
die Auswahlen "Letzte Operation anzeigen" und "Programm beenden" sollen nicht in der aufgabe.txtgeloggt werden
Optionen, die der User auswählen kann

Welche Operation soll ausgeführt werden?
[1] = Collatz-Theorem-Check
[2] = Primzahl-Check
[3] = Schaltjahr-Check
[4] = Zeige bitte die letzte Operation an!
[0] = Beenden

"""

wahl = int(input("welche operation mochten sie ausfuhren?\n1-Prime nummer\n2-Collatz\n3-Schaltjahr\n4-Exit"))

if wahl == 1:
    prime=(int(input("Bitte eine zahl eingeben: ")))
    is_prime(zahl)=prime
elif wahl == 2:
    collatz=(int(input("Bitte eine pozitive zahl eingeben: ")))
    is_collatz(number)=collatz
elif wahl == 3:
    jahr=(int(input("Bitte eine Jahreszahl eingeben: ")))
    is_schaltjahr(jahr)=jahr
elif wahl == 4:
    print('Exit')
else:
    print('falsch zahl')


    with open("data.txt", "w") as f: 
        f.write(jahr)
        f.write(prime)
        f.write(collatz)
