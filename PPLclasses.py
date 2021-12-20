import numpy as np
from math import pi, sin, cos

DEGREES_TO_RADIANS = pi / 180

def np3(x,y,z):
    return np.array([x,y,z])

class L_system():
    def __init__(self, sequence, start = (0,0,0), start_angle = (90,0,0)):
        self.sequence = sequence
        
        self.state = (start(0),start(1),start(2),start_angle(0),start_angle(1),start_angle(2))
        self.saved_states = list()
        
        self.points = []
        self.points.append(Point_plot((start(0), start(1), start(2))))
        
    def Points_list(self):
        for instruction in self.sequence:
            instruction.Action(self.state, self.saved_states, self.points)
   
class Point_plot():
    def __init__(self, position):
        self.position = position

class Instruction():
    def __init__(self, action):
        self.action = action
        self.argument = {}
        
    def Add_argument(self, name, value):
        self.arguments[name] = value
    
    def Action(self, state, saved_states, points):
        print('Action not implemented')
        
class Translate(Instruction):
    def Action(self, state, saved_states, points):
        angle_u = state(3) * DEGREES_TO_RADIANS
        angle_l = state(4) * DEGREES_TO_RADIANS
        angle_h = state(5) * DEGREES_TO_RADIANS
        
        Ru = np.array([[cos(angle_u), sin(angle_u), 0],[-sin(angle_u), cos(angle_u), 0],[0, 0, 1]])
        Rl = np.array([[cos(angle_l), 0, -sin(angle_l)],[0, 1, 0],[sin(angle_l), 0, cos(angle_l)]])
        Rh = np.array([[1, 0, 0],[0, cos(angle_h),-sin(angle_h)],[0, sin(angle_h), cos(angle_h)]])
        
        x = np3(state(0), state(1), state(2))
        
        movement = Ru * (Rl * (Rh * np3(self.argument('translation'), 0, 0)))
        
        pos = x + movement
        
        if not self.argument('line'):
            points.append(Point_plot((float('nan'), float('nan'), float('nan'))))
        
        points.append(Point_plot((pos[0], pos[1], pos[2])))
        
class Rotate(Instruction):
    def Action(self, state, saved_states, points):
        if self.action == '+':
            state = (state(0), state(1), state(2), state(3) + self.argument('rotation'), state(4), state(5))
        if self.action == '-':
            state = (state(0), state(1), state(2), state(3) - self.argument('rotation'), state(4), state(5))
        if self.action == '&':
            state = (state(0), state(1), state(2), state(3), state(4) + self.argument('rotation'), state(5))
        if self.action == '^':
            state = (state(0), state(1), state(2), state(3), state(4) - self.argument('rotation'), state(5))
        if self.action == '\\':
            state = (state(0), state(1), state(2), state(3), state(4), state(5) + self.argument('rotation'))
        if self.action == '/':
            state = (state(0), state(1), state(2), state(3), state(4), state(5) - self.argument('rotation'))
        if self.action == '|':
            state = (state(0), state(1), state(2), state(3) + self.argument(pi), state(4), state(5))
            
class Branch(Instruction):
    def Action(self, state, saved_states, points):
        if self.action == '[':
            saved_states.append(state)
        elif self.action == ']':                       # Return to previous state
            state = saved_states.pop()
            points.append(Point_plot((float('nan'), float('nan'), float('nan'))))
            points.append(Point_plot((state(0), state(1), state(2))))
            