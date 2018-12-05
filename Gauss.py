m = [
    [6,5,4,3,1],
    [1,1,1,1,1],
    [2,1,1,1,2],
    [2,2,2,1,1],
    [1,1,1,1,2]
]

x = [45,15,21,21,20]

def forward(a,b):
    for i in range (m.__len__() - 1):
        if a[i][i] == 0:
            print("Некорректный ввод")
            break
        for j in range (i + 1,m.__len__()):
            c = a
            d = b
            if a[j][i] == 0:
                continue
            diff = a[j][i] / a[i][i]
            d[i] *= diff
            b[j] -= d[i]
            d[i] /= diff
            for k in range (m.__len__()):
                c[i][k] *= diff
                a[j][k] -= c[i][k]
                c[i][k] /= diff
    return a,b

def backward(a,b):
    is_ok = 1
    if a[m.__len__() - 1][m.__len__() - 1] != 0:
        a[m.__len__() - 1][m.__len__() - 1] = b[x.__len__() - 1] / a[m.__len__() - 1][m.__len__() - 1]
    else:
        print("Некорректный ввод")
        is_ok = 0
    for i in range (1,m.__len__()):
        for j in range (m.__len__() - i,m.__len__()):
            b[x.__len__() - i - 1] -= a[m.__len__() - i - 1][j] * a[m.__len__() - i][j]
            a[m.__len__() - i - 1][j] = a[m.__len__() - i][j]
        a[m.__len__() - i - 1][m.__len__() - i - 1] = b[x.__len__() - i - 1] / a[m.__len__() - i - 1][m.__len__() - i - 1]
    for k in range (m.__len__()):
        b[k] = a[k][k]
    if is_ok == 1:
        return b

def Gauss(a,b):
    c,d = forward(a,b)
    return(backward(c,d))

print(Gauss(m,x))

print(Gauss(m,x))
