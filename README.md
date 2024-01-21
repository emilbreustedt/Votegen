# Votegen Library
This library can be used to generate inequalities and the corresponding cones in PyNormaliz.

In in votegen/generators 3 functions can be found.

write_inequality() writes an inequality corresponding to the input paarameters to a file. It returns the path of the file that can be used as the input parameter "file" in PyNormaliz.Cone() or build_cone().

get_inequality() generates an inequality represented in a nested list and returns it. It can be used as the input parameter "inequalities" in PyNormaliz.Cone() or build_cone().

build_cone() can be used to directly build the cone based in the output of he above functions and an optional parameter total_degree, that cannot be represented in the list obtained by get_inequality() but can be added during the building process of the cone.

Before this library can be used PyNormaliz https://pypi.org/project/PyNormaliz/ needs to be installed.

Examples of the concrete way of use can be found in introduction.py.