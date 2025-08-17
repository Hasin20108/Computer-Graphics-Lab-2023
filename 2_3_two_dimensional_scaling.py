# Sample Input:
# 4 100 100 100 150 150 150 150 100 2 2

import pygame
import sys

# ---------- Functions ----------
def draw_polygon(screen, color, x, y):
    points = [(x[i], y[i]) for i in range(len(x))]
    pygame.draw.polygon(screen, color, points, 1)

def scale_polygon(x, y, n, sfx, sfy):
    for i in range(n):
        x[i] = x[i] * sfx
        y[i] = y[i] * sfy


# ---------- Main ----------
def main():
    # ------- Input -------
    data = list(map(int, input().split()))
    n = data[0]                          # number of vertices
    x = data[1:2*n+1:2]                  # x coords
    y = data[2:2*n+1:2]                  # y coords
    sfx, sfy = data[2*n+1], data[2*n+2]  # scaling factors

    # ------- Pygame Setup -------
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Polygon Scaling")
    screen.fill((255, 255, 255))

    # Draw original polygon (WHITE)
    draw_polygon(screen, (0, 0, 0), x[:], y[:])

    # Scale polygon
    scale_polygon(x, y, n, sfx, sfy)

    # Draw scaled polygon (YELLOW)
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
