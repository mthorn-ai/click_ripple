import pygame
import time
from pygame.locals import *

screen = pygame.display.set_mode((750, 750))
surface = pygame.display.get_surface()
pygame.display.set_caption("ripple")
screen.fill((0, 0, 100))
pygame.display.flip()

ripples = []


def main():
    running = True
    while running:
        if len(ripples) > 0:
            draw_ripples()
            for ripl in ripples:  # each ripple is in the form of [x-pos, y-pos, radius]
                if ripl[2] > 1070:
                    ripples.remove(ripl)
                ripl[2] = ripl[2] + 1
            screen.fill((0, 0, 100))
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                ripples.insert(0, [x, y, 5])  # starts new ripple


def draw_ripples():
    for rip in ripples:
        pygame.draw.circle(surface, (42, 72, 117), (rip[0], rip[1]), rip[2], 3)
    pygame.display.flip()
    time.sleep(0.009)


if __name__ == '__main__':
    main()
