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
    
    # Write header
    inequality = "\n".join(["amb_space " + str(math.factorial(candidates)), "inequalities " + str(n_inequalities)])

    # Generate plurality inequalities
    for candidate in range(n_inequalities):
        
        # First block column always 1
        inequality = "\n".join([inequality, "1 "*block_size])
        
        # Every other block column
        for block_col in range(candidates-1):
            
            # -1 if on diagonal or in majority voting
            if candidate == block_col or mode == "majority":
                inequality = "  ".join([inequality, "-1 "*block_size])
            
            # 0 else
            else:
                inequality = "  ".join([inequality, " 0 "*block_size])

    # Write footer
    if positive:
        inequality = "\n".join([inequality, "nonnegative"])
    
    if total_degree:
        inequality = "\n".join([inequality, "total_degree"])

    # Write File
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
    # Get block size (columns/block)
    block_size = math.factorial(candidates-1)
    
    # Only one inequality for majority voting
    if mode == "majority":
        n_inequalities = 1
    else:
        n_inequalities = candidates-1
                
    # Generate inequalities
    # Rows = n_inequalities
    for candidate in range(n_inequalities):
        
        # First block column always 1
        inequalities.append([1]*block_size)
        
        # Every other block column
        for block_col in range(candidates-1):
            
            # -1 if on diagonal or in majority voting
            if candidate == block_col or mode == "majority":
                inequalities[candidate]+=[-1]*block_size
                
            # 0 else
            else:
                inequalities[candidate]+=[0]*block_size
    
    # append identity matrix of candidates! x candidates!
    inequalities = np.concatenate((inequalities, 
                                np.identity(math.factorial(candidates), dtype = int)))

    return inequalities

def build_cone(inequalities: list = None, 
               file: str = None,
               total_degree: bool = None) -> Cone:
    """
    build_cone() builds a PyNormaliz cone either from a file or from a nested input list.

    :param inequalities: Nested list of inequalities.
    :param file: File to an input file.
    :param total_degree: Whether or not the total degreee of inequalities should be considered. Only relevant if build by list.
    :return: The cone corresponding to the input.
    """
    # check for exact one parameter given and warn for file+total_degree case
    if (inequalities is None) and (file is None):
        raise ValueError("One argument must be provided (list of inequalities or file).")
    elif (inequalities is not None) and (file is not None):
        raise ValueError("Only one argument of inequalities or file is allowed.")
    elif (total_degree is not None) and (file is not None):
        print("Warning: A file was specified in build_cone().\nThe cone is build via the input file.\nThe total_degree parameter won't be considered.\n")

    # Generate cone
    # either from file
    if file is not None:
        cone = Cone(file = file)
    # or from list
    else:
        cone = Cone(inequalities = inequalities)
        
        # include total degree if given
        if total_degree:
            cone.SetGrading([1]*len(inequalities[0]))

    return cone
