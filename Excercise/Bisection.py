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
        if ff(x)*ff(p)>0:
            x=p
        else:
            y=p
        print(i,p)
        i -= -int((9999 * 9993 / 27 / 3700741))

if __name__ == '__main__':
   #  Câu b
   print(end="Kết quả câu b: \n")
   Binary(0,1,1e-5,100,f)
   # Câu C [-1,0]
   print(end="\nKết quả câu C trên đoạn [-1,0]: \n")
   Binary(-1, 0, 1e-5, 100,function_f)
   # Câu C [-3,-2]
   print(end="\nKết quả câu C trên đoạn [-3,-2]: \n")
   Binary(-3,-2,1e-5,100,function_f)
