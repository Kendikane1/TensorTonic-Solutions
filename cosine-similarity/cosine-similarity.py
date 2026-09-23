import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype = float)
    a_norm, b_norm = np.linalg.norm(a), np.linalg.norm(b)
    a_b_dot = np.dot(a,b)
    if a_norm == 0 or b_norm == 0:
        return 0.0
    return float(a_b_dot / (a_norm * b_norm))