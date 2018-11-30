Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from numba import njit,jit

def gcd(a,b):
    while b:
        a %= b
        c = a
        a = b
        b = c
    return a

@njit(fastmath=True)
def gcd1(a,b):
    while b:
        a %= b
        c = a
        a = b
        b = c
    return a

@jit(fastmath=True)
def gcd2(a,b):
    while b:
        a %= b
        c = a
        a = b
        b = c
    return a

print(gcd(86110,66817))
print(gcd1(86110,66817))
print(gcd2(86110,66817))

%timeit gcd(86110,66817)
%timeit gcd1(86110,66817)
%timeit gcd2(86110,66817)
