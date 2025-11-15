import numpy as np
import matplotlib.pyplot as plt

def runge_kutta (f, y0, x):
    n = len(x)
    y = np.zeros(n)
    y[0] = 0

    for i in range(n-1):
        h = x[i + 1] - x[i]
        xi = x[i]
        yi = y[i]
    
    