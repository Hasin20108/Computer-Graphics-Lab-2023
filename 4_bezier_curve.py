import pygame
import sys
import math

# ---------- Factorial and nCr ----------
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

# ---------- Bezier Function ----------
def bezier_function(k, n, u):
    return nCr(n, k) * (u ** k) * ((1 - u) ** (n - k))

def bezier_curve(screen, points, color=(0, 0, 0)):
    n = len(points) - 1
    eps = 0.001  # smaller step for smoother curve

    # Draw Bezier curve
    u = 0
    while u <= 1:
        x = 0
        y = 0
        for k in range(n + 1):
            bez = bezier_function(k, n, u)
            x += points[k][0] * bez
            y += points[k][1] * bez
        screen.set_at((int(x), int(y)), color)
        u += eps

    # Draw control points
    for px, py in points:
        pygame.draw.circle(screen, color, (px, py), 5)

# ---------- Main ----------
def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Bezier Curve")
    screen.fill((255, 255, 255))  # White background

    # Control points
    points = [(27, 243), (101, 47), (324, 197), (437, 23)]
    bezier_curve(screen, points, (0, 0, 0))  # Black curve

    pygame.display.flip()

    # Keep window open until closed
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
