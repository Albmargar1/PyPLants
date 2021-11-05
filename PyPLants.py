import sys
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin, cos
import random

DEGREES_TO_RADIANS = pi / 180

def is_float(string):
    try:        
        return float(string)
    except ValueError:
        return string

def Parametric_string_to_list(sequence):
    out = []
    parameters = []
    aux = ''
    filling_float = False
    filling_parameters = False
    for character in sequence:
        print(character)
        if character == '(':
            filling_parameters = True
        elif character == ')':
            filling_parameters = False
            if aux != '':
                parameters.append(is_float(aux))
                aux = ''
            out[-1].append(parameters)
            parameters = []
            
        elif not filling_parameters:
            out.append([character])
            
        elif character != ',':
            aux = ''.join([aux, character])
        elif character == ',':
            parameters.append(is_float(aux))
            aux = ''
            
    return out
            
out = Parametric_string_to_list('A(12.54,2.654,AB)B+(45.5)C(1.22,1.33)')
            
def Transform_multiple(sequence, transformations, iterations):
    for _ in range(iterations):
        sequence = Transform_sequence(sequence, transformations)
    return sequence

    
def Transform_sequence(sequence, transformations):
    return ''.join(random.choice(transformations.get(c, c)) for c in sequence)


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
    sequence = Transform_multiple(initiator, generator, iterations)
    points = L_system(sequence, turn_angle = angle)
    Plot_points(points)

L_plot('A', {'F': ['FF'], 'A': ['F[+AF-[A]--A][---A]']}, 3, 22.5)