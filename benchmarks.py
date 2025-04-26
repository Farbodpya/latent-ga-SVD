import numpy as np

def sphere(x): return np.sum(x**2)

def rastrigin(x): return 10*len(x) + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))

def ackley(x):
    a, b, c = 20, 0.2, 2*np.pi
    d = len(x)
    return -a*np.exp(-b*np.sqrt(np.sum(x**2)/d)) - np.exp(np.sum(np.cos(c*x))/d) + a + np.exp(1)

def griewank(x): return 1 + np.sum(x**2)/4000 - np.prod(np.cos(x / np.sqrt(np.arange(1, len(x)+1))))

def zakharov(x):
    i = np.arange(1, len(x)+1)
    return np.sum(x**2) + (np.sum(0.5*i*x))**2 + (np.sum(0.5*i*x))**4

def rastrigin_ii(x): return 10*len(x) + np.sum(x**4 - 10 * np.cos(2 * np.pi * x))

benchmarks = {
    "Sphere": sphere,
    "Rastrigin": rastrigin,
    "Ackley": ackley,
    "Griewank": griewank,
    "Zakharov": zakharov,
    "Rastrigin II": rastrigin_ii
}
