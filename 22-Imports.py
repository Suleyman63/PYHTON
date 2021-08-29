####### app.py (im main-Ordner)
#from modules import mathe (möglich)
#from modules import consts (möglich)
import modules.mathe as d #(auch möglich)

# (ich versuche mit obigen code das modul MATHE in meinem root-path auszuführen) 

print(d.addition(20))


######## mathe.py (im Sub-Ordner "modules")

# funktioniert nich: import consts (ohne Absicherung wie unten)

if __name__ == "__main__":
    # from . import consts funktioniert nicht, 
    # attempted relative import with no known parent package
    import consts
else:
    print("Ich wurde importiert, Mein Modulname:", __name__)
    #from modules import consts # absolute Pfad-Angaben (funktioniert)

    from . import consts        # relativer Pfad (funktioniert auch)

def addition(summand):
    return summand + consts.X

print(addition(5))

# from . import xyz  >>> relativer Pfad (. heißt: gleicher Ordner, .. ein Ordner eine Hirarchie drüber)


####### consts.py (im gleichen Sub-Ordner)

X = 10
Y = 20
