Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def gcd(a,b):
    while b:
        a %= b
        c = a
        a = b
        b = c
    return a

def egcdbody(a,b):
    if b == 0:
        return(1,0)
    x,y = egcdbody(b,a%b)
    return (y,x-int(a/b)*y)
    
def egcd(a,b):
    x,y = egcdbody(a,b)
    return(x,y,gcd(a,b))
