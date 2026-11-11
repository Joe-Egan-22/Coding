'''
nr_solver.py

Script to solve an ODE using a Newton-Raphson algorithm outputting the solution and its domain

Functions:


'''

from autograd import *
from autograd.numpy import *
from pylab import *

def Fn(x,y,n):
    h = (x[-1] - x[0]) / (n-1)
    ypp = (y[2:] - 2*y[1:-1] + y[:-2]) / h**2
    yp = (y[2:] - y[:-2]) / h
    return ypp + (2/x[1:-1])*yp + 1*y[1:-1] - (y[1:-1])**3

n = 50
dom = (10,20)
bv = 1/sqrt(50)
ran = (bv,1)
x = linspace(dom[0],dom[1],n)
yg = linspace(ran[0],ran[1],n)
yn = yg.copy()
N_max = 30

J = jacobian(lambda y: Fn(x, y, n))

for i in range(N_max):
    Fy = Fn(x,yg,n)

    Jy = J(yg)

    delta_y = linalg.solve(Jy[:,1:-1], -Fy)
    yn[1:-1] = yg[1:-1] + delta_y
    if linalg.norm(delta_y) < 1e-4:
        print(f"Converged in {i+1} iterations")
        break
    else:
        yg = yn

plot(x,yn,label='Newton-Raphson')
title('Exterior Solution')
xlabel('x')
ylabel('y')

num = yn

print(num)
