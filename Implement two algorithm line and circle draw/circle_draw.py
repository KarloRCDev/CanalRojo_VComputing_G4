import cv2
import numpy as np
def draw_circle_bresenham(img, center, radius):
    x, y = 0, radius
    d = 3 - 2 * radius
    while x <= y:
        # Plot the eight octants of the circle
        img[center[1] + x, center[0] + y] = (0, 0, 255)
        img[center[1] + y, center[0] + x] = (0, 0, 255)
        img[center[1] - x, center[0] + y] = (0, 0, 255)
        img[center[1] - y, center[0] + x] = (0, 0, 255)
        img[center[1] + x, center[0] - y] = (0, 0, 255)
        img[center[1] + y, center[0] - x] = (0, 0, 255)
        img[center[1] - x, center[0] - y] = (0, 0, 255)
        img[center[1] - y, center[0] - x] = (0, 0, 255)

        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y = y - 1
        x = x + 1

    # Draw a small filled circle at the center of the circle
    cv2.circle(img, center, 3, (0, 255, 0), -1)

    cv2.imshow('Circle', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# example usage
img = np.zeros((500, 500, 3), np.uint8)
center = (250, 250)
radius = 100
draw_circle_bresenham(img, center, radius)