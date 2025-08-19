import pygame
import sys

def draw_circle(screen, xc, yc, radius, color=(0, 0, 0)):
    points = []
    x = 0
    y = radius
    p = 1 - radius

    while x <= y:
        points.append((x, y))
        points.append((y, x))
        x += 1
        if p >= 0:
            p += 2 * (x - y) + 1
            y -= 1
        else:
            p += 2 * x + 1

    # Plot all 8 symmetric points
    for v in points:
        screen.set_at((xc + v[0], yc + v[1]), color)
        screen.set_at((xc - v[0], yc + v[1]), color)
        screen.set_at((xc + v[0], yc - v[1]), color)
        screen.set_at((xc - v[0], yc - v[1]), color)


# ---------- Main ----------
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Midpoint Circle Drawing")

    # White background
    screen.fill((255, 255, 255))

    # Example circle (black)
    xc, yc, radius = 400, 400, 150
    draw_circle(screen, xc, yc, radius, (0, 0, 0))

    pygame.display.flip()

    # Keep window open until closed
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
