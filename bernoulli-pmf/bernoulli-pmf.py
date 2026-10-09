import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    x = np.asarray(x)
    pmf = []
    for i in x :
        if i == 0 :
            failure = 1 - p
            pmf.append(failure)
        else :
            pmf.append(p)


    pmf = np.asarray(pmf)
    return {
        "pmf" : pmf,
        "mean" : float(p),
        "variance" : float(p * (1 - p))
    }