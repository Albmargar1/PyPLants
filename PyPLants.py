import matplotlib.pyplot as plt
from math import pi, sin, cos

import PPLdecode 
import PPLutils

DEGREES_TO_RADIANS = pi / 180

def L_system(sequence, turn_angle, start = (0,0), start_angle = 90):
    saved_states = list()
    state = (start[0], start[1], start_angle)    
    yield (start[0], start[1])
    
    for instruction in sequence:
        x, y, angle = state
        
        if instruction[0].lower() in 'abcdef':      # Move turtle forward
            state = (x - instruction[1] * cos(angle * DEGREES_TO_RADIANS),
                     y + instruction[1] * sin(angle * DEGREES_TO_RADIANS),
                     angle)
            
            if instruction[0].islower():
                yield (float('nan'), float('nan'))
                
            yield (state[0], state[1])
                        
        elif instruction[0] == '+':     # Turn turtle clockwise without moving
            state = (x, y, angle + turn_angle)
            
        elif instruction[0] == '-':     # Turn turtle counter-clockwise without moving
            state = (x, y, angle - turn_angle)
            
        elif instruction[0] == '[':                       # Remember current state
            saved_states.append(state)

        elif instruction[0] == ']':                       # Return to previous state
            state = saved_states.pop()
            yield (float('nan'), float('nan'))
            x, y, _ = state
            yield (x, y)
    
def L_plot(initiator, generator, parametric_dictionary, iterations, angle):
    sequence = PPLdecode.Transform_multiple(initiator, generator, iterations)
    PPLdecode.Deparametrize(sequence, parametric_dictionary)
    points = L_system(sequence, turn_angle = angle)
    PPLutils.Plot_points(points)


parametric_dictionary = {}
parametric_dictionary['R'] = 1.456
parametric_dictionary['s'] = 1

initiator = PPLdecode.Parametric_string_to_list('A(s)')
generator = PPLdecode.Parametric_string_to_list('A(s)|F(s)[+A(div(s,R))][-A(div(s,R))]')

L_plot(initiator, generator, parametric_dictionary, iterations = 10, angle = 85)