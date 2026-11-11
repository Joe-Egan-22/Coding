'''
fd_solver:

Formulates and solved the matrix equation associated with the finite difference method.

Functions:

    get_h(maths_settings)
    get_domain(maths_settings)
    get_A(n, h, A_coeffs)
    get_B(n, h, x, B_coeffs)
    solve(maths_settings, A_coeffs, B_coeffs)

Output:

    sol from solve(...)
'''

import numpy as np

def get_h(settings):
    '''
    Extracts starting point (x0), end point (xn) and
    number of divisions from settings and calculates 
    step size (h)

    Arguments:
        maths_settings: dict

    Output:
        h: float
    '''

    # Extract coefficients from dictionary
    x0 = settings['variables']['x0']
    xn = settings['variables']['xn']
    n = settings['variables']['n']

    # Calculate step length
    h = (xn - x0) / n
    return h

def get_domain(x0,xn,n):
    '''
    Extracts starting point (x0), end point (xn)
    and number of divisions (n) from settings and 
    creates an array which defines the domain of
    consideration.

    Arguments:
        maths_settings: dict

    Outputs:
        domain: NumPy array
    '''

    # Create array between x0, xn with n values
    domain = np.linspace(x0, xn, n+1)
    return domain


def get_A(settings, x, h):
    '''
    Creates an empty matrix array for the left-
    hand-side of the finite difference matrix
    equation.

    Arguments:
        n: int
        h: float
        A_coeffs: dict

    Outputs:
        A: NumPy array
    '''

    # Extract required coefficients
    n = settings['variables']['n']

    # Define Heaviside function
    X = np.full((n+1), settings['variables']['b']) # (n+1) array filled with field boundary value
    step = np.heaviside((x - X), 0) # Step function Theta(x - X) to isolate exterior

    # Create empty nxn zero matrix
    A = np.zeros((n+1,n+1))

    # Set top left and bottom right values to 1
    # for initial/final value boundary conditions
    A[0,0] = 1
    A[int(n/2),int(n/2)] = 1 # Fix boundary value
    A[n,n] = 1

    # Fill rest of the rows with diagonal and off-diagonal elements up to the middle value
    for i in range(1, int(n/2)):
        A[i,i-1] = settings['A_coeffs']['y_i-1/h2']/h**2 + settings['A_coeffs']['y_i-1/hx']/(h*x[i])
        A[i,i] = settings['A_coeffs']['y_i_const'] + settings['A_coeffs']['y_i/h2']/h**2 + settings['A_coeffs']['y_i_hs']*step[i]
        A[i,i+1] = settings['A_coeffs']['y_i+1/h2']/h**2 + settings['A_coeffs']['y_i+1/hx']/(h*x[i])

    # Fill rest of the rows with diagonal and off-diagonal elements after the middle value
    for i in range(int(n/2 + 1), n):
            A[i,i-1] = settings['A_coeffs']['y_i-1/h2']/h**2 + settings['A_coeffs']['y_i-1/hx']/(h*x[i])
            A[i,i] = settings['A_coeffs']['y_i_const'] + settings['A_coeffs']['y_i/h2']/h**2 + settings['A_coeffs']['y_i_hs']*step[i]
            A[i,i+1] = settings['A_coeffs']['y_i+1/h2']/h**2 + settings['A_coeffs']['y_i+1/hx']/(h*x[i])

    return A

def get_B(settings, x, h):
    '''
    FOR INSIDE THE SOURCE

    Creates an empty vector array for the right-
    hand-side of the finite difference matrix
    equation

    Arguments:
        n: int
        h: float
        x: NumPy array
        B_coeffs: Dict

    Outputs:
        B: NumPy array
    '''
    # Extract required coefficients
    n = settings['variables']['n']

    # Define Heaviside function
    X = np.full((n+1), settings['variables']['b']) # (n+1) array filled with field boundary value
    step = np.heaviside((x - X), 0) # Step function Theta(x - X) to isolate exterior
    
    # Create empty n-length zero vector
    B = np.zeros(n+1)

    # Fix initial and final values
    B[0] = settings['B_coeffs']['y0']
    B[int(n/2)] = settings['B_coeffs']['yb'] # Fix boundary field value
    B[n] = settings['B_coeffs']['yn']

    # Fill each element with the right hand side of the finite difference equation BEFORE the boundary
    for i in range(1,int(n/2)):
        B[i] = ( settings['B_coeffs']['const'] + settings['B_coeffs']['linear']*x[i]
                    + settings['B_coeffs']['quadratic']*(x[i]**2) )*(h**2) + settings['B_coeffs']['hs']*step[i]

    # Fill each element with the right hand side of the finite difference equation AFTER the boundary
    for i in range(int(n/2+1),n):
        B[i] = ( settings['B_coeffs']['const'] + settings['B_coeffs']['linear']*x[i]
                    + settings['B_coeffs']['quadratic']*(x[i]**2) )*(h**2) + settings['B_coeffs']['hs']*step[i]

    return B


def solve(settings):
    '''
    Uses matrix A and vector B to solve a finite difference
    matrix equation to give an array of y values defining the
    numerical solution for the original equation.

    Arguments:
        maths_settings: Dict
        A_coeffs: Dict
        B_coeffs: NumPy array

    Outputs:
        sol: Dict
    '''

    # Extract n
    n = (settings['variables']['n'])

    # Calculate h and get domain
    h = get_h(settings)
    dom = get_domain(settings['variables']['x0'], settings['variables']['xn'], n)


    # Define A-matrix and B-vector for both inside and outside source
    A = get_A(settings, dom, h)
    B = get_B(settings, dom, h)

    # Solve the finite difference equation
    sol = np.linalg.solve(A,B)

    # Form a dictionary
    num_dict = {'domain': dom, 'solution': sol}

    return num_dict