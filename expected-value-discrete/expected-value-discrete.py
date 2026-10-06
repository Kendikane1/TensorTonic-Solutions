import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    a = zip(x,p)
    product = []
    for i, j in a:
        k = i * j
        product.append(k)

    return float(np.sum(product))
        