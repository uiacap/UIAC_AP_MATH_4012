import re
#import matplotlib.pyplot as plt
import numpy as np


def eq2num(string):
    a,b,c = re.findall(r'([\-\+]?\d*)x\^2([\-\+]?\d*)x([\-\+]?\d*)',string)[0]
    return a,b,c

def eq(a,b,c,x):
    return (a*x**2) + (b*x) + c


def solve(a,b):
    a1,b1,c1= list(map(int,eq2num(a)))
    a2,b2,c2= list(map(int,eq2num(b)))
    eq1 = a1,b1,c1
    eq2 = a2,b2,c2
    a_,b_,c_ = [i-j for i,j in zip(eq1,eq2)]
    delta = (b_**2)- (4*a_*c_)
    x1,x2 = (-b_+delta**0.5)/(2*a_),(-b_-delta**0.5)/(2*a_)
    if x1>x2:
        x1,x2 = x2,x1
    x = np.linspace(-10,+10,100)
    y1 = eq(a1,b1,c1,x)
    y2 = eq(a2,b2,c2,x)
    
    y1_ = eq(a1,b1,c1,x1)
    y2_ = eq(a1,b1,c1,x2)

    print((round(x1,2),round(y1_,2)),(round(x2,2),round(y2_,2)))

a = input()
b = input()
solve(a,b)
