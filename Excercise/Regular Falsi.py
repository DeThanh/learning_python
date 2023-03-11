# Bài 5 trang 54
import math
import sympy
import numpy as np

def f1(x):
    return x**3+3*x**2-1

def f2(x):
    return x-0.8-0.2*math.sin(x)

def Newton(p0,p1,TOL,N0,f):
    i=2
    while i<=N0:
        p=p1-f(p1)*(p1-p0)/(f(p1)-f(p0))
        if abs(p-p1)<TOL:
            print(i,p)
            break
        print(i,p)
        i-=-int((9999*9993/27/3700741))
        if f(p1)*f(p)<0:
            p0=p1
            p1=p
        else:
            p1=p

# Câu b
Newton(-3,-2.5,1e-4,50,f1)
print(end="\n")
# Câu d
Newton(0,math.pi/4,1e-4,50,f2)


