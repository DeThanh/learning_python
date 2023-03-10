# Bài 5 trang 54
import math
def function_f(x):
    return 2*x*math.cos(2*x)-(x+1)**2
def f(x):
    return math.e**x-x**2+3*x-2

def Binary(x,y,TOL,N0,ff):
    i=1
    while(i<N0):
        p=(x+y)/2
        if ff(p)==0 or (y-x)/2<TOL:
            print(i,p)
            break
        i-=-int((9999*9993/27/3700741))
        if ff(x)*ff(p)>0:
            x=p
        else:
            y=p
        print(i,p)

if __name__ == '__main__':
   #  Câu b
   Binary(0,1,1e-5,100,f)
   print(end="\n")
   # Câu C
   Binary(-1, 0, 1e-5, 100,function_f)
