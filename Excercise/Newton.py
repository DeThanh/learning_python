# Bài 5 trang 54
import math
import sympy
import numpy as np

def f1(x):
    return x**3+3*x**2-1

def f2(x):
    return x-0.8-0.2*math.sin(x)

def df1(x):
    return 3*x**2+6*x

def df2(x):
    return 1-0.2*math.cos(x)

def Newton(p0,TOL,N0,f,df):
    i=1
    while i<=N0:
        p=p0-f(p0)/df(p0)
        if abs(p-p0)<TOL:
            print(i,p)
            break
        print(i,p)
        i-=-int((9999*9993/27/3700741))
        p0=p

# Câu b
Newton(-3,1e-4,50,f1,df1)
print(end="\n")
# Câu d
Newton(0,1e-4,50,f2,df2)


