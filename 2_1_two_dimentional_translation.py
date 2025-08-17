# Sample Input:
# 4 100 100 100 200 200 200 200 100 150 150


import pygame
import sys

# ---------- Functions ----------
def draw_polygon(screen, color, x, y):
    points = [(x[i], y[i]) for i in range(len(x))]
    pygame.draw.polygon(screen, color, points, 1)

def translate_polygon(x, y, tx, ty):
    for i in range(len(x)):
        x[i] += tx
        y[i] += ty


# ---------- Main ----------
def main():
    # ------- Input -------
    data = list(map(int, input().split()))
    n = data[0]                          # number of vertices
    x = data[1:2*n+1:2]                  # x coords
    y = data[2:2*n+1:2]                  # y coords
    tx, ty = data[2*n+1], data[2*n+2]    # translation factors

    # ------- Pygame Setup -------
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Polygon Translation")
    screen.fill((255, 255, 255))

    # Draw original polygon (WHITE)
    draw_polygon(screen, (0, 0, 0), x[:], y[:])

    # Apply translation
    translate_polygon(x, y, tx, ty)

    # Draw translated polygon (YELLOW)
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
