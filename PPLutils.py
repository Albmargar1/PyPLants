import matplotlib.pyplot as plt

def Plot_points(points, margins = 0.2, debug_plot = False):
    plt.figure(figsize=(12, 8), dpi=120)
    axes = plt.axes()
    
    if not debug_plot:
        plt.axis('off')
        plt.margins(x=margins, y=margins)
        
    axes.set_aspect('equal', 'datalim')
    x, y = zip(*points)
    plt.plot(x, y)
    
def find(string, character):
    return [i for i, ltr in enumerate(string) if ltr == character]

def find_parentheses(s):
    """ Find and return the location of the matching parentheses pairs in s.

    Given a string, s, return a dictionary of start: end pairs giving the
    indexes of the matching parentheses in s. Suitable exceptions are
    raised if s contains unbalanced parentheses.

    """

    # The indexes of the open parentheses are stored in a stack, implemented
    # as a list

    stack = []
    parentheses_locs = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            try:
                if len(stack) == 1:
                    aux = []
                    aux.append(stack.pop())
                    aux.append(i)
                    parentheses_locs.append(aux)
                else:
                    stack.pop()
                
            except IndexError:
                raise IndexError('Too many close parentheses at index {}'
                                                                .format(i))
    if stack:
        raise IndexError('No matching close parenthesis to open parenthesis '
                         'at index {}'.format(stack.pop()))
    return parentheses_locs


            