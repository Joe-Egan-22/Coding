'''
config.py

Script containing dictionaries of all variables necessary for solvers
and plotting modules to function.

All changes should be made to this file only before running main.py

ALL EXCEPT THE ANALYTICAL SOLUTION WHICH MUST CURRENTLY BE EDITED IN THE analytical_sol.py FILE!

'''

import numpy as np

# Dictionary containing desired labels for plots
graph_settings = {
    'title': 'Comparing Analytical and Numerical Solution',
    'xlabel': 'x',
    'ylabel': r'f(x)'
}

# Dictionary defining key variables for finite difference
variables = {
    'n': 100,    # Number of divisions
    'x0': 1e-9,    # Starting point
    'b': 5,     # Arbitrary source boundary value
    'xn': 10,     # End point
    'e': 1e-9   # Arbitrarily small division
}

# Dictionary containing coefficients for LHS matrix in finite difference
y_matrix_A_coeffs = {
    'y_i-1/h2': 1,   # Term propto h^-2 in left off-diagonal element
    'y_i-1/hx': -1,   # Term propto hx^-1 in left off-diagonal element

    'y_i_const': -2,  # Constant term in diagonal element
    'y_i_hs': -25,      # Term propto the Heaviside function in diagonal element
    'y_i/h2': -2,      # Term propto h^-2 in diagonal element

    'y_i+1/h2': 1,    # Term propto h^-2 in right off-diagonal element
    'y_i+1/hx': 1     # Term propto hx^-1 in right off-diagonal element
}

# Dictionary containing coefficients for RHS vector in finite difference (FOR INSIDE THE SOURCE)
B_coeffs = {
    'const': -0,           # For constant term
    'hs': -25,              # For constant term propto Heaviside function
    'linear': 0,            # For linear term
    'quadratic':0,          # For quadratic term
    'y0': 0,               # Fixed initial value
    'yb': 1/np.sqrt(50),    # Fixed field boundary value
    'yn': 1     # Fixed final value (use if applicable)
}

# Dictionary containing all previous nested for convenience
settings = {
    "graph_settings": graph_settings,
    "variables": variables,
    "A_coeffs": y_matrix_A_coeffs,
    "B_coeffs": B_coeffs
    }