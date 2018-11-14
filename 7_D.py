def gcd(a,b):
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
