from numba import jit
import timeit


m = [
    [6,5,4,3,1],
    [1,1,1,1,1],
    [2,1,1,1,2],
    [2,2,2,1,1],
    [1,1,1,1,2]
]

x = [45,15,21,21,20]

@jit(fastmath=True)
def forward(a,b):
    for i in range (b.__len__() - 1):
        if a[i][i] == 0:
            print("Некорректный ввод")
            break
        for j in range (i + 1,b.__len__()):
            c = a
            d = b
            if a[j][i] == 0:
                continue
            diff = a[j][i] / a[i][i]
            d[i] *= diff
            b[j] -= d[i]
            d[i] /= diff
            for k in range (b.__len__()):
                c[i][k] *= diff
                a[j][k] -= c[i][k]
                c[i][k] /= diff
    return a,b

@jit(fastmath=True)
def backward(a,b):
    is_ok = 1
    if a[b.__len__() - 1][b.__len__() - 1] != 0:
        a[b.__len__() - 1][b.__len__() - 1] = b[b.__len__() - 1] / a[b.__len__() - 1][b.__len__() - 1]
    else:
        print("Некорректный ввод")
        is_ok = 0
    for i in range (1,b.__len__()):
        for j in range (b.__len__() - i,b.__len__()):
            b[b.__len__() - i - 1] -= a[b.__len__() - i - 1][j] * a[b.__len__() - i][j]
            a[b.__len__() - i - 1][j] = a[b.__len__() - i][j]
        a[b.__len__() - i - 1][b.__len__() - i - 1] = b[b.__len__() - i - 1] / a[b.__len__() - i - 1][b.__len__() - i - 1]
    for k in range (b.__len__()):
        b[k] = a[k][k]
    if is_ok:
        return b

@jit(fastmath=True)
def Gauss(a,b):
    c,d = forward(a,b)
    return(backward(c,d))

print(Gauss(m,x))

print(timeit.timeit(lambda: Gauss(m, x)))
