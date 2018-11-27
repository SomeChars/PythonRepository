#Если надо - напишу ввод матриц, вывод правда немного кривоват, но это вроде аппаратная проблема

m = [
    [6,5,4,3,1],
    [1,1,1,1,1],
    [2,1,1,1,2],
    [2,2,2,1,1],
    [1,1,1,1,2]
]

x = [44,15,21,21,20]

def forward(a,b):
    flag = 0
    for i in range (a.__len__() - 1):
        for j in range (i + 1,a.__len__()):
            c = a
            d = b
            if a[j][i] == 0:
                continue
            diff = a[j][i] / a[i][i]
            d[i] *= diff
            b[j] -= d[i]
            d[i] /= diff
            for k in range (a.__len__()):
                c[i][k] *= diff
                a[j][k] -= c[i][k]
                c[i][k] /= diff
    return a,b


def backward(a,b):
    a[a.__len__() - 1][a.__len__() - 1] = b[b.__len__() - 1] / a[a.__len__() - 1][a.__len__() - 1]
    for i in range (1,a.__len__()):
        for j in range (a.__len__()):
            if j == (a.__len__() - i - 1):
                continue
            a[a.__len__() - i - 1][j] *= a[a.__len__() - i][j]
            b[a.__len__() - i - 1] -= a[a.__len__() - i - 1][j]
            if a[a.__len__() - i][j] != 0:
                a[a.__len__() - i - 1][j] = a[a.__len__() - i][j]
        a[a.__len__() - i - 1][a.__len__() - i - 1] = b[b.__len__() - i - 1] / a[a.__len__() - i - 1][a.__len__() - i - 1]
    for k in range (a.__len__()):
        b[k] = a[k][k]
    return b

def Gauss(a,b):
    c,d = forward(a,b)
    return(backward(c,d))
