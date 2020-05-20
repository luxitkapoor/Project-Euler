# Lattice Paths

import math


def getPaths(size):
    '''
    This function returns the total number of paths that can be present in a grid of size m x m.
    Using the formula that in a set with n elements with n1 being identical elements of type 1 and n2 being identical elements of type 2 and so on, we can say the total number of permutations will be n!/(n1! n2! ... nk !)

    Also in a grid of size m x m, we know that the total number of steps to the right will be equal to the total steps to the left both of which are equal to the edge of the grid or the size of the grid.
    '''
    total_steps = size * 2
    down_steps = size
    right_steps = size
    total_paths = (math.factorial(total_steps)) / (math.factorial(down_steps) * math.factorial(right_steps))
    return total_paths


print(getPaths(3))
