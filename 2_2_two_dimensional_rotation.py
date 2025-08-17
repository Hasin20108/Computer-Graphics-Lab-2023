# Sample Input: 
# 4 100 100 100 200 200 200 200 100 45 200 200


import pygame
import sys
import math

# ---------- Functions ----------
def draw_polygon(screen, color, x, y):
    points = [(x[i], y[i]) for i in range(len(x))]
    pygame.draw.polygon(screen, color, points, 1)

def rotate_polygon(x, y, n, angle, xp, yp):
    radian = math.radians(angle)
    sin_t = math.sin(radian)
    cos_t = math.cos(radian)

    for i in range(n):
        x_shift = x[i] - xp
        y_shift = y[i] - yp
        x[i] = xp + (x_shift * cos_t) - (y_shift * sin_t)
        y[i] = yp + (x_shift * sin_t) + (y_shift * cos_t)


# ---------- Main ----------
def main():
    # ------- Input -------
    data = list(map(int, input().split()))
    n = data[0]                          # number of vertices
    x = data[1:2*n+1:2]                  # x coords
    y = data[2:2*n+1:2]                  # y coords
    angle = data[2*n+1]                  # rotation angle
    x_pivot, y_pivot = data[2*n+2], data[2*n+3]  # pivot point

    # ------- Pygame Setup -------
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Polygon Rotation")
    screen.fill((255, 255, 255))

    # Draw original polygon (WHITE)
    draw_polygon(screen, (0, 0, 0), x[:], y[:])

    # Rotate polygon
    rotate_polygon(x, y, n, angle, x_pivot, y_pivot)

    # Draw rotated polygon (YELLOW)
    draw_polygon(screen, (255, 0, 0), x, y)

    pygame.display.flip()

    # Keep window open until closed
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Run program
if __name__ == "__main__":
    main()
