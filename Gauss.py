#округляю решение на 0.000003
def GJ(a,b):
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
                if k == i:
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
    res = []
    for i in used:
        if abs(b[i]-int(b[i])) < 0.000003 or abs(b[i]-int(b[i]+1)) < 0.000003: res += [round(b[i])]
        else: res += [b[i]]
    return res
