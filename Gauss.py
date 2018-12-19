m = [
    [6,5,4,3,1],
    [1,1,1,1,1],
    [2,1,1,1,2],
    [2,2,2,1,1],
    [1,1,1,1,2]
]

x = [45,15,21,21,20]

def forward(a,b):
    for i in range (len(b) - 1):
        if a[i][i] == 0:
            print("Некорректный ввод")
            break
        for j in range (i + 1,len(b)):
            c = a
            d = b
            if a[j][i] == 0:
                continue
            diff = a[j][i] / a[i][i]
            d[i] *= diff
            b[j] -= d[i]
            d[i] /= diff
            for k in range (len(b)):
                c[i][k] *= diff
                a[j][k] -= c[i][k]
                c[i][k] /= diff
    return a,b

def backward(a,b):
    is_ok = 1
    if a[len(b) - 1][len(b) - 1] != 0:
        a[len(b) - 1][len(b) - 1] = b[len(b) - 1] / a[len(b) - 1][len(b) - 1]
    else:
        print("Некорректный ввод")
        is_ok = 0
    for i in range (1,len(b)):
        for j in range (len(b) - i,len(b)):
            b[len(b) - i - 1] -= a[len(b) - i - 1][j] * a[len(b) - i][j]
            a[len(b) - i - 1][j] = a[len(b) - i][j]
        a[len(b) - i - 1][len(b) - i - 1] = b[len(b) - i - 1] / a[len(b) - i - 1][len(b) - i - 1]
    for k in range (len(b)):
        b[k] = a[k][k]
    if is_ok == 1:
        return b

def Gauss(a,b):
    c,d = forward(a,b)
    return(backward(c,d))

print(Gauss(m,x))
