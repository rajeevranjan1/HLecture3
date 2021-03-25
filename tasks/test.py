from Algorithms import *

def factRec(n):
    if n==1:
        return 1
    return n*factRec(n-1)

print(factRec(5))



