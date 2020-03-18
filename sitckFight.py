import sys, pygame
import os

pygame.init()

black = 0,0,0
size = width, height = 1080, 720
path = os.getcwd().replace("\\", "/")

screen = pygame.display.set_mode(size)
stickFigure = pygame.image.load(path + "/resources/stickFigure.png")
stickFigureRect = stickFigure.get_rect()
stickFigureSize = stickFigureRect.size



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        screen.fill(black)
        screen.blit(
            pygame.transform.scale(
                stickFigure, tuple([int(x/3) for x in stickFigureSize])
                ), 
            stickFigureRect
            )
        pygame.display.flip()
