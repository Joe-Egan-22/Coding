'''
variable_checker.py

Reads specific variables from config.py dictionaries and
checks whether they fit the required conditions.

NB: This file will be updated to include more rigorous validation,
for now, only needs to check requirements on variable n

Functions:

'''

def check_n(settings):
    '''
    Checks that the variable n fits required conditions

    Arguments:
        settings: Dict
    '''

    n = settings['variables']['n']

    if n % 2 != 0:
        raise ValueError("n must be an even integer")

    return None