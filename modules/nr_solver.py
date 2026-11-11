'''
nr_solver.py

Script to solve an ODE using a Newton-Raphson algorithm outputting the solution and its domain

Functions:


'''

import autograd as gr
import numpy as np
import matplotlib.pyplot as plt
from config import settings

def Fn(x,y,n,X):
    '''
    Calculates the Fn function for Newton-Raphson
    '''

    # Define Heaviside step function Theta(x-X)
    step = np.heaviside((x[1:-1] - X[1:-1]),0)

    h = (x[-1] - x[0]) / (n-1)
    ypp = (y[2:] - 2*y[1:-1] + y[:-2]) / h**2
    yp = (y[2:] - y[:-2]) / h
    return ypp + (2/x[1:-1])*yp + (1 - 25*step)*y[1:-1] - (y[1:-1])**3


def get_domain(settings):
    '''
    Gets the domain for the problem

    Arguments:
        Settings: Dict

    Outputs:
        dom: NumPy array
    '''

    x = np.linspace(settings['variables']['x0'], settings['variables']['xn'], (settings['variables']['n']+1))

    return x

def nr_solve(settings):
    '''
    Solves Newton-Raphson problem, outputs solution
    and domain

    Arguments:
        Settings: Dict

    Outputs:

    '''
    # Get n
    n = settings['variables']['n']

    # Define domain
    x = get_domain(settings)
    X = np.full((n+1), settings['variables']['b'])

    # Define other
    yg = np.linspace(settings['B_coeffs']['y0'], settings['B_coeffs']['yn'], n+1)
    yn = yg.copy()

    # Define a Jacobian function
    J = gr.jacobian(lambda y: Fn(x, y, n, X))

    # Iterative NR method
    for i in range(settings['NR_coeffs']['N_max']):
        Fy = Fn(x,yg,n,X)

        Jy = J(yg)

        delta_y = np.linalg.solve(Jy[:,1:-1], -Fy)
        yn[1:-1] = yg[1:-1] + delta_y
        if np.linalg.norm(delta_y) < settings['NR_coeffs']['tol']:
            print(f"Converged in {i+1} iterations")
            break
        else:
            yg = yn

    NR_sol = {'domain': x, 'solution': yn}

    return NR_sol

sol = nr_solve(settings)

x = sol['domain']
y = sol['solution']

plt.plot(x,y)
plt.show()