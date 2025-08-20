# Sample Input: 
# 4 300 300 300 500 500 500 500 300 30 500 500


import pygame
import sys
import math

def draw_polygon(screen, color, x, y):
    points = [(x[i], y[i]) for i in range(len(x))]
    pygame.draw.polygon(screen, color, points, 3)

def rotate_polygon(x, y, n, angle, xp, yp):
    radian = math.radians(angle)
    sin_t = math.sin(radian)
    cos_t = math.cos(radian)

    for i in range(n):
        x_shift = x[i] - xp
        y_shift = y[i] - yp
        x[i] = xp + (x_shift * cos_t) - (y_shift * sin_t)
        y[i] = yp + (x_shift * sin_t) + (y_shift * cos_t)


def main():
    data = list(map(int, input().split()))
    n = data[0]                          
    x = data[1:2*n+1:2]                  
    y = data[2:2*n+1:2]                  
    angle = data[2*n+1]                  
    x_pivot, y_pivot = data[2*n+2], data[2*n+3]  

    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Polygon Rotation")
    screen.fill((255, 255, 255))

    draw_polygon(screen, (0, 0, 0), x[:], y[:])

    rotate_polygon(x, y, n, angle, x_pivot, y_pivot)

    draw_polygon(screen, (255, 0, 0), x, y)

    rotate_polygon(x, y, n, angle, x_pivot, y_pivot)
    draw_polygon(screen, (0, 0, 255), x, y)


    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
