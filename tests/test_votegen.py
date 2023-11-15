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
@pytest.mark.parametrize("candidates, mode, positive, total_degree", 
                         itertools.product(*[range (2, 5), # candidates
                                             ["plurality", "majority"], # mode
                                             [True, False], # positive
                                             [True, False]])) # total_degree

# test function
def test_equality(candidates, mode, positive, total_degree):
    
    # get outputs for different inputs
    get_ineq = get_inequality(candidates, mode, positive, total_degree)
    write_ineq = write_inequality(candidates, mode, positive, total_degree)

    # calculate cones
    get_cone = Cone(inequalities = get_ineq)

    write_cone = Cone(file = write_ineq)
    
    # test on equality    
    assert get_cone.Multiplicity() == write_cone.Multiplicity()