Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from numba import jit

m = [
    [6,5,4,3,1],
    [1,1,1,1,1],
    [2,1,1,1,2],
    [2,2,2,1,1],
    [1,1,1,1,2]
]

x = [45,15,21,21,20]

len = m.__len__()
lenb = x.__len__()

@jit(fastmath=True)
def forward(a,b):
    for i in range (len - 1):
        if a[i][i] == 0:
            print("Некорректный ввод")
            break
        for j in range (i + 1,len):
            c = a
            d = b
            if a[j][i] == 0:
                continue
            diff = a[j][i] / a[i][i]
            d[i] *= diff
            b[j] -= d[i]
            d[i] /= diff
            for k in range (len):
                c[i][k] *= diff
                a[j][k] -= c[i][k]
                c[i][k] /= diff
    return a,b

@jit(fastmath=True)
def backward(a,b):
    is_ok = 1
    if a[len - 1][len - 1] != 0:
        a[len - 1][len - 1] = b[lenb - 1] / a[len - 1][len - 1]
    else:
        print("Некорректный ввод")
        is_ok = 0
    for i in range (1,len):
        for j in range (len - i,len):
            b[lenb - i - 1] -= a[len - i - 1][j] * a[len - i][j]
            a[len - i - 1][j] = a[len - i][j]
        a[len - i - 1][len - i - 1] = b[lenb - i - 1] / a[len - i - 1][len - i - 1]
    for k in range (len):
        b[k] = a[k][k]
    if is_ok:
        return b

@jit(fastmath=True)
def Gauss(a,b):
    c,d = forward(a,b)
    return(backward(c,d))

print(Gauss(m,x))

%timeit Gauss(m,x)