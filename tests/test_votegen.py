'''
Test file

This file contains test for all combinations of the input parameters of the functions in the generators.py file.
The output of the functions are tested on equality.
'''

from votegen.generators import *
import pytest
from PyNormaliz import *
import itertools

# generate different output combinations
@pytest.mark.parametrize("candidates, mode, total_degree", 
                         itertools.product(*[range (2, 5), # candidates
                                             ["plurality", "majority"], # mode
                                             [True, False]])) # total_degree

# test function
def test_equality(candidates, mode, total_degree):
    
    # get outputs for different inputs
    get_ineq = get_inequality(candidates, mode)
    write_ineq = write_inequality(candidates, mode, True, total_degree)

    # calculate cones
    get_cone = build_cone(inequalities=get_ineq, total_degree=total_degree)
    write_cone = build_cone(path = write_ineq, total_degree=total_degree)
    
    # test on equality    
    assert get_cone.Multiplicity() == write_cone.Multiplicity()