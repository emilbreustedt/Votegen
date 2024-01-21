'''
Introduction file

This file provides an overview of the functions and use of this library. 
Before it can be used, please install Normaliz from source: https://github.com/Normaliz/Normaliz/releases
and PyNormaliz https://pypi.org/project/PyNormaliz/
'''

from votegen.generators import *
import itertools

# get cases
cases = itertools.product(*[range (2, 5), # candidates
                            ["plurality", "majority"], # mode
                                             [True, False]]) # total_degree

for case in cases:
    candidates, mode, total_degree = case
    print()
    print(" ".join(["Candidates:", str(candidates), "\nMode:", mode, "\nTotal Degree:", str(total_degree)]))
    
    write_ineq = write_inequality(candidates, mode, True, total_degree)
    write_cone = build_cone(file = write_ineq)
    
    get_ineq = get_inequality(candidates, mode)
    print(get_ineq)
    get_cone = build_cone(inequalities=get_ineq, total_degree=total_degree)
    print()
    
    print("get_inequality Multiplicity: " + str(get_cone.Multiplicity()))
    print("write_inequality Multiplicity: " + str(write_cone.Multiplicity()))