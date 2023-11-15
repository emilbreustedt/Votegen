import numpy as np
import math
from PyNormaliz import Cone
    
def write_inequality(candidates: int = 4, 
                    mode: str = "plurality",
                    positive: bool  = True,
                    total_degree: bool = True,
                    filename: str = "inequality") -> str:
    """
    write_inequality() generates an inaquality with the given parameters and writes it as an .in file in the working directory.

    :param candidates: The number of candidates in the inequality.
    :param mode: The mode of the inequality. One of plurality or majority.
    :param positive: Whether or not the inequalities should be non-negative.
    :param total_degree: Whether or not the total degreee of inequalities should be considered.
    :param filename: Filename of the generated file, without extension.
    :return: Filename to be used as the "file" paramter for the Cone class.
    """ 
    block_size = math.factorial(candidates-1)
    
    if mode == "majority":
        n_inequalities = 1
    else:
        n_inequalities = candidates-1
    
    # write Header
    inequality = "\n".join(["amb_space " + str(math.factorial(candidates)), "inequalities " + str(n_inequalities)])

    # generate plurality Inequalities
    for candidate in range(n_inequalities):
        # write first column
        inequality = "\n".join([inequality, "1 "*block_size])
        for block_col in range(candidates-1):
            if candidate == block_col or mode == "majority":
                inequality = "  ".join([inequality, "-1 "*block_size])
            else:
                inequality = "  ".join([inequality, " 0 "*block_size])

    # write Footer
    if positive:
        inequality = "\n".join([inequality, "nonnegative"])
    
    if total_degree:
        inequality = "\n".join([inequality, "total_degree"])

    # write File
    filename = "_".join([filename, mode, str(candidates) + "cand"])
    with open(".".join([filename, "in"]), 'w') as f:
        f.write(inequality)
    
    return filename


def get_inequality(candidates: int = 4,
                    mode: str = "plurality") -> list: 
    """
    get_inequality() generates an inaquality with the given parameters and returns it as a nested numpy array.

    :param candidates: The number of candidates in the inequality.
    :param mode: The mode of the inequality. One of plurality or majority.
    :return: The inequality to be used as the "inequalities" paramter for the Cone class..
    """ 
    inequalities = []
    block_size = math.factorial(candidates-1)
    if mode == "majority":
        n_inequalities = 1
    else:
        n_inequalities = candidates-1
                
    # generate Inequalities
    for candidate in range(n_inequalities):
        inequalities.append([1]*block_size)
        for block_col in range(candidates-1):
            if candidate == block_col or mode == "majority":
                inequalities[candidate]+=[-1]*block_size
            else:
                inequalities[candidate]+=[0]*block_size
    
    # append identity matrix
    inequalities = np.concatenate((inequalities, 
                                np.identity(math.factorial(candidates), dtype = int)))

    return inequalities

def build_cone(inequalities: list = None, 
               path: str = None,
               total_degree: bool = None) -> Cone:
    """
    build_cone() builds a PyNormaliz cone either from a file or from a nested input list.

    :param inequalities: Nested list of inequalities.
    :param path: Path to an input file.
    :param total_degree: Whether or not the total degreee of inequalities should be considered. Only relevant if build by list.
    :return: The cone corresponding to the input.
    """
    # check for exact one parameter given and warn for path+total_degree case
    if (inequalities is None) and (path is None):
        raise ValueError("One argument must be provided (list of inequalities ot path of file).")
    elif (inequalities is not None) and (path is not None):
        raise ValueError("Only one argument of inequalities or path is allowed.")
    elif (total_degree is not None) and (path is not None):
        print("Warning: A path was specified in build_cone().\nThe cone is build via the input file.\nThe total_degree parameter won't be considered.\n")

    # Generate cone
    # either from file
    if path is not None:
        cone = Cone(file = path)
    # or from list
    else:
        cone = Cone(inequalities = inequalities)
        
        # include total degree if given
        if total_degree:
            cone.SetGrading([1]*len(inequalities[0]))

    return cone
