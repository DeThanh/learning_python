import numpy
from numpy import random
import sys

lis =[]
def swap(a,b):
    temp=a
    a=b
    b=temp

def Gauss():
    n = int(input('Enter number of unknowns: '))
    # a = np.zeros((n, n + 1))
    # x = np.zeros(n)

    print("Create random Augmented Matrix Coefficients")
    x = random.uniform(0,10000,size=(n,n+1))

    # for i in range(n):
    #     for j in range(n + 1):
    #         a[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))

    # for i in range(n):
    #     if a[i][i] == 0.0:
    #         sys.exit('Divide by zero detected!')
    #
    #     for j in range(i + 1, n):
    #         ratio = a[j][i] / a[i][i]
    #
    #         for k in range(n + 1):
    #             a[j][k] = a[j][k] - ratio * a[i][k]
    #
    # x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]
    #
    # for i in range(n - 2, -1, -1):
    #     x[i] = a[i][n]
    #
    #     for j in range(i + 1, n):
    #         x[i] = x[i] - a[i][j] * x[j]
    #
    #     x[i] = x[i] / a[i][i]

    print("array is: ")
    for i in x:
        for p in i:
            print(p, end=" ")
        print("\n")

    for i in range(n-1):
        p = i
        cnt = 0
        for j in range(i, n):
            cnt += 1
            if x[j, i] != 0:
                p = j
                break
        if cnt == n - i:
            print("‘1No unique solution exists’")
            return
        if p!=i:
            for j in range(n+1):
                swap(x[i,j],x[p,j])
        for k in range(i+1,n):
            m=x[k,i]/x[i,i]
            for j in range(n+1):
                x[k,j]-=m*x[i,j]
    if x[n-1,n-1]==0:
        print("‘2No unique solution exists’")
        return
    mm = numpy.zeros(shape=(n+1))
    # for i in range(n+1):
    #     lis.append(0)
    mm[n-1]=x[n-1][n]/x[n-1][n-1]
    i=n-2
    while i>=0:
        temp=0
        for j in range(i+1,n+1):
            temp+=x[i][j]*mm[j]
        mm[i]=(x[i][n]-temp)/x[i][i]
        i-=1
        # lis.reverse()
    for i in range(n):
        print('X%d = %0.3f' %(i+1,mm[i]),end="\n")



# print('\nThe solution is: ')
# for i in range(n):
#     print('X%d = %0.2f' % (i, x[i]), end='\t')

Gauss()
