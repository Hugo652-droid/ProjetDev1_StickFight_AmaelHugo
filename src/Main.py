import pygame
from sys import exit

from src.Root import Root
from src.Game import Game

class Main():
    def __init__(self):
        pygame.init()
        windowHome = Root(pygame)
        windowHome.changeBg('images/img_bg_main.png')
        windowHome.buttonPlay()
        windowHome.buttonQuit()
        windowHome.title('images/Image titre.png')
        pygame.display.flip()
        runningHome = True
        while runningHome:
            # Gérer les événements
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Si l'utilisateur clique sur la croix pour fermer

                        windowHome.closeRoot(pygame)
                        runningHome = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if windowHome.button_rect.collidepoint(event.pos):
                        windowHome.closeRoot(pygame)
                        runningHome = False
                        game = Game()

                    if windowHome.button_rect_quit.collidepoint(event.pos):
                        windowHome.closeRoot(pygame)
                        runningHome = False
        pygame.quit()
        exit()

main = Main()