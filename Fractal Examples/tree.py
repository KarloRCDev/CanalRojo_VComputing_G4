import numpy as np
import matplotlib.pyplot as plt

def draw_binary_tree(ax, x, y, length, angle, depth):
    if depth == 0:
        return

    x2, y2 = x + length * np.sin(np.deg2rad(angle)), y + length * np.cos(np.deg2rad(angle))
    ax.plot([x, x2], [y, y2], 'k-')
    plt.pause(0.001) 
    
    draw_binary_tree(ax, x2, y2, length*0.7, angle + 30, depth-1)
    draw_binary_tree(ax, x2, y2, length*0.7, angle - 30, depth-1)

def main():
    
    depth = int(input("Enter the depth of the binary tree: "))

    
    fig, ax = plt.subplots()
    ax.set_xlim([-200, 200])
    ax.set_ylim([-50, 250])

    
    draw_binary_tree(ax, 0, 0, 80, 0, depth)

    plt.show()

if __name__ == '__main__':
    main()
