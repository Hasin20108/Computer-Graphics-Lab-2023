# Sample Input:
# 4 100 100 100 200 200 200 200 100 150 150


import pygame
import sys

def draw_polygon(screen, color, x, y):
    points = [(x[i], y[i]) for i in range(len(x))]
    pygame.draw.polygon(screen, color, points, 3)

def translate_polygon(x, y, tx, ty):
    for i in range(len(x)):
        x[i] += tx
        y[i] += ty


def main():
    data = list(map(int, input().split()))
    n = data[0]                          
    x = data[1:2*n+1:2]                  
    y = data[2:2*n+1:2]                  
    tx, ty = data[2*n+1], data[2*n+2]    

    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Polygon Translation")
    screen.fill((255, 255, 255))

    draw_polygon(screen, (0, 0, 0), x[:], y[:])

    translate_polygon(x, y, tx, ty)

    draw_polygon(screen, (255, 0, 0), x, y)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
