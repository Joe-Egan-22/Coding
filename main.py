import modules.fd_solver as fd_solver
import modules.graphing as graphing
import modules.analytical_sol as analytical
import modules.variable_checker as variable_check
from modules.config import settings

def main():

    # Perform variable check
    variable_check.check_n(settings)

    # Solutions
    num_sol = fd_solver.solve(settings) # Numerical solution and corresponding domain
    ana_sol = analytical.analytical_eq(settings) # Analytical solution and corresponding domain

    # Plot numerical and analytical solution
    graphing.plot_sols(settings, ana_sol, num_sol)

    return None

if __name__ == '__main__':
    main()