
#prime
def is_prime(x):
    try:
        if x < 2:
            return False
        else:
            if x == 2:
                return True
            else:
                for i in range(2, x):
                    if x % i == 0:
                        return False
            return True
    except:
        print('except prime')



#collatz
def is_collatz(number):
    try:
        if number % 2 == 0: 
            return number // 2

        elif number % 2 == 1: 
            return number * 3 + 1
    except:
        print('excep collatz')



# schaltjahr
def is_Schaltjahr(jahr):
    try:
        if jahr % 400 == 0:
            return True
        elif jahr % 100 == 0:
            return True
        elif jahr % 4 == 0:
            return True
        else:
            return False
    except:
        print('except schaltjahr')


