# Sample Input:
# 4 150 150 150 250 250 250 250 150 2 2

import pygame
import sys

def draw_polygon(screen, color, x, y):
    points = [(x[i], y[i]) for i in range(len(x))]
    pygame.draw.polygon(screen, color, points, 3)

def scale_polygon(x, y, n, sfx, sfy):
    for i in range(n):
        x[i] = x[i] * sfx
        y[i] = y[i] * sfy


def main():
    data = list(map(int, input().split()))
    n = data[0]                          
    x = data[1:2*n+1:2]                  
    y = data[2:2*n+1:2]                  
    sfx, sfy = data[2*n+1], data[2*n+2]  

    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Polygon Scaling")
    screen.fill((255, 255, 255))

    draw_polygon(screen, (0, 0, 0), x[:], y[:])

    scale_polygon(x, y, n, sfx, sfy)

    draw_polygon(screen, (255, 0, 0), x, y)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
