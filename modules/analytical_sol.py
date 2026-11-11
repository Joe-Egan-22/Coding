'''
analytical_sol.py

Script collects relevant coefficients from config.py and formulates
a desired analytical function and its corresponding domain.
'''

import numpy as np

def domain(settings):
    '''
    Defines the domain for the analytical solution

    Arguments:
        settings: Dict

    Outputs:
        domain: NumPy array
    '''

    # Extract coefficients from dictionary
    x0 = settings['variables']['x0']
    xn = settings['variables']['xn']
    n = settings['variables']['n']

    # Create domain array
    domain = np.linspace(x0,xn,n+1)

    return domain

def analytical_eq(settings):
    '''
    Formulates the analytical solution array

    Arguments:
        settings: Dict

    Outputs:
        ana_sol: NumPy array
    '''
    # Extract n
    n = settings['variables']['n']

    # Define domain
    x = domain(settings)
    X = settings['variables']['b'] # Arbitrary source boundary value

    # Redefine domain as difference between x and boundary source value
    s = x - np.full(n+1, 5)

    # User must formulate analytical equation HERE rather than in config file

    p = 25 # Phase parameter
    g = np.sqrt(2*(p - 1)) # The effective mass of interior scalar fluctuations in units of γ
    x0 = (2 + g**2)**(-1/2) # Field boundary value
    pve_step = np.heaviside(s, 0) # Step function Theta(x) to isolate exterior
    nve_step = np.heaviside(-s, 0) # Step function Theta(-x) to isolate interior


    a = np.asinh(g/x0) - g*s
    interior = nve_step * g * (1/np.sinh(a))
    exterior = pve_step * np.tanh(s + np.atanh(x0)) # Exterior term of equation

    ana_eq = (interior + exterior)

    ana_sol = {'domain': x, 'solution': ana_eq}
    return ana_sol