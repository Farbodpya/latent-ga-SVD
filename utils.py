import numpy as np
import random

def blend_crossover(x1, x2, alpha=0.5):
    gamma = (1 + 2*alpha) * np.random.rand(*x1.shape) - alpha
    return (1 - gamma)*x1 + gamma*x2, gamma*x1 + (1 - gamma)*x2

def mutate(x, mu, sigma=0.1):
    nmu = int(np.ceil(mu * len(x)))
    indices = random.sample(range(len(x)), nmu)
    y = np.copy(x)
    for i in indices:
        y[i] += sigma * np.random.randn()
    return y
