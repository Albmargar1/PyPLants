import matplotlib.pyplot as plt
from math import pi, sin, cos

import PPLdecode 
import PPLutils

DEGREES_TO_RADIANS = pi / 180

parameters_dictionary = {'AB': 666}

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
    
def L_plot(initiator, generator, iterations = 0, angle = 45):
    sequence = PPLdecode.Transform_multiple(initiator, generator, iterations)
    points = L_system(sequence, turn_angle = angle)
    PPLutils.Plot_points(points)


out = PPLdecode.Parametric_string_to_list('A(12.54,2.654,AB)B+(45.5)C(1.22,1.33)', parameters_dictionary)
L_plot('A', {'F': ['FF'], 'A': ['F[+AF-[A]--A][---A]']}, 3, 22.5)