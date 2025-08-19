import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Overlapping Shapes")

# Colors
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

def draw_triangle():
    points = [(10, 100), (50, 20), (100, 100)]
    pygame.draw.polygon(screen, GREEN, points)

def draw_circle():
    pygame.draw.circle(screen, BLUE, (100, 100), 45)

def draw_rectangle():
    rect = pygame.Rect(100, 100, 80, 80)
    pygame.draw.rect(screen, RED, rect)

def main():
    # Fill background
    screen.fill(WHITE)

    sequence = "RCT"   # Same as your C++ code
    for ch in sequence:
        if ch == 'C':
            draw_circle()
        elif ch == 'T':
            draw_triangle()
        else:
            draw_rectangle()

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
