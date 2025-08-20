import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Overlapping Shapes")

RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

def draw_triangle():
    points = [(210, 300), (250, 220), (300, 300)]
    pygame.draw.polygon(screen, GREEN, points)

def draw_circle():
    pygame.draw.circle(screen, BLUE, (300, 300), 60)

def draw_rectangle():
    rect = pygame.Rect(300, 300, 120, 120)
    pygame.draw.rect(screen, RED, rect)

def main():
    screen.fill(WHITE)

    sequence = "RCT"  
    for ch in sequence:
        if ch == 'C':
            draw_circle()
        elif ch == 'T':
            draw_triangle()
        else:
            draw_rectangle()

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
