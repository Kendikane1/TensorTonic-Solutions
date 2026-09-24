import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.asarray(x)
    centred = x - np.mean(x)
    sample_size = x.size
    variance = float((np.sum(centred ** 2)) / (sample_size - 1))
    standard_deviation = float(np.sqrt(variance))
    return {
        "variance" : variance,
        "standard_deviation" : standard_deviation
    }