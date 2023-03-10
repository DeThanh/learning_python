# Bài 11 trang 65
import math
def f1(x):
    return (2-math.e**x+x*x)/3

def f2(x):
    return 5/x**2+2

def Fixed_Point(P0,TOL,N0,f):
    i=1
    while i<=N0:
        p=f(P0)
        if abs(p-P0)<TOL:
            print(i,p)
            break
        i=i+1
        print(i,p)
        P0=p

Fixed_Point(1,1e-5,50,f1)
print(end="\n")
Fixed_Point(-1,1e-5,50,f2)
