#Используйте вторую фунцию

import math
import random

def easyprimalitycheck(n):
    if n==2 or n==3 or n==5 or n==7 or n==11:
        return 1
    counter = 0
    a = 2
    if a**(n-1) % n == 1:
        counter+=1
    a = 3
    if a**(n-1) % n == 1:
        counter+=1
    a = 5
    if a**(n-1) % n == 1:
        counter+=1
    a = 7
    if a**(n-1) % n == 1:
        counter+=1
    a = 11
    if a**(n-1) % n == 1:
        counter+=1
    if counter == 5:
        return 1
    else:
        return 0
        
    
def primality(n):
    if n < 500:
        if easyprimalitycheck(n):
            return 1
        else:
            return 0
    counter = 0
    a = 0
    for i in range (10):
        a = random.randint(1,int(math.sqrt(n)))
        while not easyprimalitycheck(a):
            a = random.randint(1,int(math.sqrt(n)))
        if a**(n-1) % n == 1:
            counter += 1
    if counter == 10:
        return 1
    else:
        return 0
