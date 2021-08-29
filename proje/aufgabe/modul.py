import math

import sys

import datetime



def is_prime(zahl):
    try:
        if zahl == 2:
            return True
        if zahl % 2 == 0 or zahl <= 1:
            return False
    except:
        return 'Except'


def is_collatz(number):
    try:
        if number % 2 == 0:       
            return result = number // 2
        elif number % 2 == 1:      
            return result = 3 * number + 1
    except:
        return 'Except'


def is_schaltjahr(jahr):
    try:
        if jahr % 4 == 0 and jahr % 400 == 0:
            return True
        elif jahr % 4 == 0 and jahr % 100 != 0:
            return True
        else:
            return False
    except:
        return 'Except'
