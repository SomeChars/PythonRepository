#Числа прошедшие проверку первой фунцией с помощью 2,3,5 называются Industrial primal numbers
#Почти не врёт но всё равно медленнее проверки в лоб из-за того что операций как минимум в 2 раза больше чем в лоб
#Так ещё они и тяжелее чем в лоб, поэтому особого смысла в первой функции нет :|
import functools
import math

def Fermat_primality_check(n):
    if n==1 or n==2 or n==3 or n==5:
        return True
    if (pow(2,n-1) % n == 1) and (pow(3,n-1) % n == 1) and (pow(5,n-1) % n == 1):
        return True
    return False

@functools.lru_cache()
def cached_primality_check(n):
    if n == 2:
        return True
    for i in range (2, 1+math.ceil(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

for i in range (2,100):
    print (Fermat_primality_check(i), cached_primality_check(i), i)
