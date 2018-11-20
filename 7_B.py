#Используйте вторую фунцию
#Можно подобрать числа Кармайкла, которые пройдут проверку первой функцией, но это маловероятно
#Рандомный выбор 10 чисел сильно уменьшает шансы, что у вас это получится (как минимум в 2^10 раз вроде)

import math
import random

def easyprimalitycheck(n):
    if n==2 or n==3 or n==5 or n==7 or n==11:
        return True
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
        return False
    else:
        return True
        
    
def primality(n):
    if n < 500:
        if easyprimalitycheck(n):
            return True
        else:
            return False
    counter = 0
    a = 0
    for i in range (10):
        a = random.randint(1,int(math.sqrt(n)))
        while not easyprimalitycheck(a):
            a = random.randint(1,int(math.sqrt(n)))
        if a**(n-1) % n == 1:
            counter += 1
    if counter == 10:
        return True
    else:
        return False
