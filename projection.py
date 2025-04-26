import numpy as np

D = 5000
d = 2

# Generate a random projection matrix using SVD on sample data
X_sample = np.random.randn(1000, D)
U, S, Vt = np.linalg.svd(X_sample, full_matrices=False)
P = Vt[:d, :]

def decode(z):
    return P.T @ z
