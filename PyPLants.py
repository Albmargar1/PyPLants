import sys
import numpy as np
import matplotlib.pyplot as plt

def Check_external_modules():
    modules = ['numpy', 'matplotlib']
    for m in modules:
        if m not in sys.modules:
            print('ERROR: You have not imported the {} module'.format(m))
            return
    print('All modules imported correctly')
    
def Test_plt():
    x = [1, 2, 3]
    y = np.array([[1, 2], [3, 4], [5, 6]])
    plt.plot(x, y)