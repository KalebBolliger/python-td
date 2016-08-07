import pygame, sys

pygame.init();

size = (1280, 720)
black = (0, 0, 0)
screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Goodbye!")
            sys.exit()

    screen.fill(black)
    pygame.display.flip()