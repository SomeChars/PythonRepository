def gcd(a,b):
    while b:
        a %= b
        c = a
        a = b
        b = c
    return a
