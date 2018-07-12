import math

def f(t,y):
    return 1/2*(math.cos(10+t)+math.cos(10-t))*10

def g(t):
    return 1/2*(math.sin(10+t)-math.sin(10-t))*10

def rk(a,b,N,alpha):
    h=(b-a)/N
    t=a
    w=alpha
    print("t","  Runge-Kutta","         Actual_Value","     Absolute_Error")
    for i in range(1,N+1):
        K_1=h*f(t,w)
        K_2=h*f(t+h/2,w+K_1/2)
        K_3=h*f(t+h/2,w+K_2/2)
        K_4=h*f(t+h,w+K_3)
        w=w+(K_1+2*K_2+2*K_3+K_4)/6
        t=a+i*h
        print(round(t,5),w,g(t),abs(g(t)-w))

rk(a=0,b=20,N=20,alpha=0)
