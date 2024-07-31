import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# from tqdm import tqdm
# from random import random
import os

class Point:
    def __init__(self, value, coordinate, deg) -> None:
        self.value = value
        self.coordinate = coordinate
        self.deg = deg

def Rotate(point: Point, deg):
    r = 3
    rad = math.radians(deg + point.deg)
    x = math.cos(rad) * r
    y = math.sin(rad) * r
    z = 1 * r
    return [x + point.coordinate[0], y + point.coordinate[1], z + point.coordinate[2]]

os.system('cls')

fig = plt.figure(figsize=(10, 10))
ax = plt.axes(projection='3d')








def update(frame):
    print("Frame {}".format(frame), end=', ')

    currentPoints = [Point(16, [0, 0, 0], 90)]
    iteration = 20

    ax.cla()

    for i in range(iteration):
        nextPoints = []
        for currentPoint in currentPoints:
            Point_ = Point(currentPoint.value*2, Rotate(currentPoint, + 15), currentPoint.deg + 15)
            nextPoints.append(Point_)
            plt.plot([currentPoint.coordinate[0], Point_.coordinate[0]], 
                    [currentPoint.coordinate[1], Point_.coordinate[1]], 
                    [currentPoint.coordinate[2], Point_.coordinate[2]], 
                    color = (0.1, 0.1 + i/(iteration*2), i/iteration), linewidth = 1)

            if currentPoint.value % 3 == 1 and currentPoint.value > 4:
                Point_ = Point(int((currentPoint.value - 1) / 3), Rotate(currentPoint, - 35), currentPoint.deg - 35)
                nextPoints.append(Point_)
                plt.plot([currentPoint.coordinate[0], Point_.coordinate[0]], 
                        [currentPoint.coordinate[1], Point_.coordinate[1]], 
                        [currentPoint.coordinate[2], Point_.coordinate[2]], 
                        color = (0.1, 0.1 + i/(iteration*2), i/iteration), linewidth = 1)

        currentPoints = nextPoints

    ax.view_init(azim=frame*2, elev=30)
    plt.axis('off')







ani = FuncAnimation(fig, update, frames=180, interval=50)
ani.save('Animations/Animation_Collatz Conjecture.gif', writer='pillow', dpi=80)