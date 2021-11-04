import sys
import numpy as np

def CheckExternalModules():
    modules = ['numpy']
    for m in modules:
        if m not in sys.modules:
            print('ERROR: You have not imported the {} module'.format(m))
            return
    print('All modules imported correctly')