def gcd(a,b):
    c = 0
    while b:
        a %= b
        c = a
        a = b
        b = c
    return a
