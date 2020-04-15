import math

def Cholesky(a,b):
    num = len(b)
    for i in range(num-1):
        for j in range(i+1,num):
            if a[i][j] != a[j][i]:
                print('Non-symmetric matrix!')
                return None
    l = [[0 for i in range(num)] for i in range(num)]
    l[0][0] = math.sqrt(a[0][0])
    for i in range(1,num):
        l[i][0] = a[i][0]/l[0][0]
    for i in range(1,num):
        for j in range(1,i):
            l[i][j] = (a[i][j] - sum([l[i][k]*l[j][k] for k in range(j)]))/l[j][j]
        if a[i][i] - sum([r*r for r in l[i][:i]]) < 0:
            print('Negative determined matrix')
            return None
        l[i][i] = math.sqrt(a[i][i] - sum([r*r for r in l[i][:i]]))

    y = [b[0]/l[0][0]]
    for i in range(1,num):
        y += [(b[i] - sum([l[i][k]*y[k] for k in range(i)]))/l[i][i]]
    x = [0]*num
    x[num-1] =  y[num-1]/l[num-1][num-1]
    for i in range(num-2,-1,-1):
        x[i] = (y[i] - sum([l[k][i]*x[k] for k in range(i+1,num)]))/l[i][i]
    return x
