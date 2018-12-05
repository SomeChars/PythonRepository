m = [
    [6,5,4,3,1],
    [1,1,1,1,1],
    [2,1,1,1,2],
    [2,2,2,1,1],
    [1,1,1,1,2]
]

x = [45,15,21,21,20]

def forward(a,b):
    for i in range (len(a) - 1):
        if a[i][i] == 0:
            print("Некорректный ввод")
            break
        for j in range (i + 1,len(a)):
            c = a
            d = b
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

print(Gauss(m,x))
