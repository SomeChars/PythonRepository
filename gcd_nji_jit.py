from numba import njit,jit

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
