# import matplotlib.pyplot as plt

# def draw_circle(xc, yc, r):
#     x = r
#     y = 0
#     dx = 1
#     dy = 1
#     err = dx - (r << 1)

#     # create empty lists to hold the x and y coordinates
#     x_coords = []
#     y_coords = []

#     while x >= y:
#         # add the current point to the coordinate lists
#         x_coords.append(xc + x)
#         y_coords.append(yc + y)

#         x_coords.append(xc + y)
#         y_coords.append(yc + x)

#         x_coords.append(xc - y)
#         y_coords.append(yc + x)

#         x_coords.append(xc - x)
#         y_coords.append(yc + y)

#         x_coords.append(xc - x)
#         y_coords.append(yc - y)

#         x_coords.append(xc - y)
#         y_coords.append(yc - x)

#         x_coords.append(xc + y)
#         y_coords.append(yc - x)

#         x_coords.append(xc + x)
#         y_coords.append(yc - y)

#         # calculate the error term
#         if err <= 0:
#             y += 1
#             err += dy
#             dy += 2
#         if err > 0:
#             x -= 1
#             dx += 2
#             err += dx - (r << 1)

#     # plot the circle using the coordinate lists
#     plt.plot(x_coords, y_coords, 'bo')
#     plt.axis('equal')
#     plt.show()

# # example usage
# draw_circle(50, 50, 30)

import matplotlib.pyplot as plt

def draw_circle(xc, yc, r):
    x = r
    y = 0
    dx = 1
    dy = 1
    err = dx - (r << 1)

    # create empty lists to hold the x and y coordinates
    x_coords = []
    y_coords = []

    while x >= y:
        # add the current point to the coordinate lists
        x_coords.append(xc + x)
        y_coords.append(yc + y)

        x_coords.append(xc + y)
        y_coords.append(yc + x)

        x_coords.append(xc - y)
        y_coords.append(yc + x)

        x_coords.append(xc - x)
        y_coords.append(yc + y)

        x_coords.append(xc - x)
        y_coords.append(yc - y)

        x_coords.append(xc - y)
        y_coords.append(yc - x)

        x_coords.append(xc + y)
        y_coords.append(yc - x)

        x_coords.append(xc + x)
        y_coords.append(yc - y)

        # calculate the error term
        if err <= 0:
            y += 1
            err += dy
            dy += 2
        if err > 0:
            x -= 1
            dx += 2
            err += dx - (r << 1)

    # plot the circle using the coordinate lists
    plt.plot(x_coords, y_coords, 'bo')
    plt.axis('equal')
    plt.show()

# example usage
draw_circle(50, 50, 30)
