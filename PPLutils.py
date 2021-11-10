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