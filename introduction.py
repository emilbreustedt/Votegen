'''
Introduction file

This file provides an overview of the functions and use of this library. 
Before it can be used, please install Normaliz from source: https://github.com/Normaliz/Normaliz/releases
and PyNormaliz https://pypi.org/project/PyNormaliz/
'''

from votegen.generators import *
from PyNormaliz import *

for candidates in range (2, 5):
    print("Condition: " + str(candidates))
    print()

    ineq = get_inequality(candidates = candidates)
    print("get_inequality List:\n" + str(ineq))
    C = Cone(inequalities = ineq)
    print("get_inequality plurality Multiplicity: " + str(C.Multiplicity()))
    print()
    
    ineq_path = write_inequality(candidates = candidates)
    # print(ineq_path)
    C = Cone(file = ineq_path)
    print("write_inequality plurality Multiplicity: " + str(C.Multiplicity()))
    print()