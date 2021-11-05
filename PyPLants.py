import sys
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin, cos

DEGREES_TO_RADIANS = pi / 180

def Check_external_modules():
    modules = ['numpy', 'matplotlib', 'math']
    for m in modules:
        if m not in sys.modules:
            print('ERROR: You have not imported the {} module'.format(m))
            return
    print('All modules imported correctly')
    
def Plot_points(points, margins = 0.2, debug_plot = False):
    plt.figure(figsize=(12, 8), dpi=120)
    axes = plt.axes()
    
    if not debug_plot:
        plt.axis('off')
        plt.margins(x=margins, y=margins)
        
    axes.set_aspect('equal', 'datalim')
    x, y = zip(*points)
    plt.plot(x, y)
    
def L_plot(initiator, generator, iterations = 0, angle = 45):
    sequence = transform_multiple(initiator, generator, iterations)
    points = L_system(sequence, turn_angle = angle)
    Plot_points(points)
    
def L_system(sequence, turn_angle=45, start = (0,0), start_angle = 90):
    saved_states = list()
    state = (start[0], start[1], start_angle)    
    yield (start[0], start[1])
    
    for instruction in sequence:
        x, y, angle = state
        
        if instruction.lower() in 'abcdef':      # Move turtle forward
            state = (x - cos(angle * DEGREES_TO_RADIANS),
                     y + sin(angle * DEGREES_TO_RADIANS),
                     angle)
            
            if instruction.islower():
                yield (float('nan'), float('nan'))
                
            yield (state[0], state[1])
                        
        elif instruction == '+':     # Turn turtle clockwise without moving
            state = (x, y, angle + turn_angle)
            
        elif instruction == '-':     # Turn turtle counter-clockwise without moving
            state = (x, y, angle - turn_angle)
            
        elif instruction == '[':                       # Remember current state
            saved_states.append(state)

        elif instruction == ']':                       # Return to previous state
            state = saved_states.pop()
            yield (float('nan'), float('nan'))
            x, y, _ = state
            yield (x, y)

def transform_sequence(sequence, transformations):
    return ''.join(transformations.get(c, c) for c in sequence)

def transform_multiple(sequence, transformations, iterations):
    for _ in range(iterations):
        sequence = transform_sequence(sequence, transformations)
    return sequence