'''
graphing.py

Script creates a figure and plots a solution against a domain

Functions:
    plot_data(settings, sol)
'''

import matplotlib.pyplot as plt


def plot_sols(settings, ana_sol, num_sol):
    '''
    Creates a figure and plots solution against domain.

    Arguments:
        settings: Dict
        sol: Dict

    Outputs:
        fig: Pyplot figure
    '''
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_title(settings['graph_settings']['title'])
    ax.set_xlabel(settings['graph_settings']['xlabel'])
    ax.set_ylabel(settings['graph_settings']['ylabel'])

    # Plot numerical solution
    n = settings['variables']['n']
    ax.plot(num_sol['domain'], num_sol['solution'], label = f'Numerical solution (n = {n})')
    ax.plot(ana_sol['domain'], ana_sol['solution'], label = 'Analytical solution')

    # Plot vertical line indicating arbitrary source boundary position
    plt.axvline(settings['variables']['b'], color = 'r', linestyle = '--')

    ax.legend(loc = 'upper left')
    plt.show()

    return fig
    