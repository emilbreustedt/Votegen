import numpy as np
import math
    
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
                    mode: str = "plurality",
                    positive: bool  = True,
                    total_degree: bool = True) -> list: 
    """
    get_inequality() generates an inaquality with the given parameters and returns it as a nested numpy array.

    :param candidates: The number of candidates in the inequality.
    :param mode: The mode of the inequality. One of plurality or majority.
    :param positive: Whether or not the inequalities should be non-negative.
    :param total_degree: Whether or not the total degreee of inequalities should be considered.
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
    
    # append identity matrix if positive
    if positive:
        inequalities = np.concatenate((inequalities, 
                                   np.identity(math.factorial(candidates), dtype = int)))
    if total_degree:
        pass

    return inequalities
        
        
        
   
    
    

