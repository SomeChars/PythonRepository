#округляю решение на 0.000003
def Gauss(a,b):
    used = []
    num = len(b)
    for j in range(num):
        possible = False
        for i in range(num):
            if a[i][j] == 0 or i in used:
                continue
            possible = True
            for k in range(j+1,num):
                a[i][k] /= a[i][j]
            b[i] /= a[i][j]
            a[i][j] /= a[i][j]
            for k in range(num):
                if k == i or k in used:
                    continue
                if a[k][j] != 0:
                    for t in range(j+1,num):
                        a[k][t] -= a[i][t]*a[k][j]
                    b[k] -= b[i]*a[k][j]
                    a[k][j] = 0
            used += [i]
            break
        if not possible:
            print('Null Determinant!')
            return None
    res = [b[i] for i in used]
    for i in range(num-1,-1,-1):
        for j in range(i+1,num):
            res[i] -= res[j]*a[used[i]][j]
    for i in range(num):
        if abs(res[i] - int(res[i])) < 0.000003 or abs(res[i] - int(res[i] + 1)) < 0.000003:
            res[i] = round(res[i])
    return res
