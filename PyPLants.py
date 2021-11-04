import os
import numpy as np

def Test():
    zero = np.sum(np.zeros(3))
    if (abs(zero) < 1e-3):
        print('External modules IS working')
    else:
        print('External modules NOT working')