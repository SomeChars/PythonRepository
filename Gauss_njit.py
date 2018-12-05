from numba import njit,jit
import numpy as np
import copy

m = np.array([
    [6.0,5.0,4.0,3.0,1.0],
    [1.0,1.0,1.0,1.0,1.0],
    [2.0,1.0,1.0,1.0,2.0],
    [2.0,2.0,2.0,1.0,1.0],
    [1.0,1.0,1.0,1.0,2.0]]
)

x = np.array([45.0,15.0,21.0,21.0,20.0])

@njit(fastmath=True)
def forward(a,b):
    for i in range (len(a) - 1):
        c = a.copy()
        d = b.copy()
        if a[i][i] == 0:
            print("Некорректный ввод")
            break
        for j in range (i + 1,len(a)):
            if a[j][i] == 0:
                continue
            diff = a[j][i] / a[i][i]
            d[i] *= diff
            b[j] -= d[i]
            d[i] /= diff
            for k in range (len(a)):
                c[i][k] *= diff
                a[j][k] -= c[i][k]
                c[i][k] /= diff
    return a,b

@njit(fastmath=True)
def backward(a,b):
    is_ok = 1
    if a[len(a) - 1][len(a) - 1] != 0:
        a[len(a) - 1][len(a) - 1] = b[len(a) - 1] / a[len(a) - 1][len(a) - 1]
    else:
        print("Некорректный ввод")
        is_ok = 0
    for i in range (1,len(a)):
        for j in range (len(a) - i,len(a)):
            b[len(a) - i - 1] -= a[len(a) - i - 1][j] * a[len(a) - i][j]
            a[len(a) - i - 1][j] = a[len(a) - i][j]
        a[len(a) - i - 1][len(a) - i - 1] = b[len(a) - i - 1] / a[len(a) - i - 1][len(a) - i - 1]
    for k in range (len(a)):
        b[k] = a[k][k]
    if is_ok == 1:
        return b

def Gauss(a,b):
    c,d = forward(a,b)
    return(backward(c,d))


%timeit Gauss(m,x)
