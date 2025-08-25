import pygame
from sys import exit

from src.Root import Root
from src.Game import Game
from src.Settings import Settings

class Main():
    def __init__(self):
        pygame.init()
        windowHome = Root(pygame)
        windowHome.changeBg()
        windowHome.buttonPlay()
        windowHome.buttonQuit()
        windowHome.buttonSettings()

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

                    if windowHome.button_rect_settings.collidepoint(event.pos):
                        windowHome.closeRoot(pygame)
                        runningHome = False

                        windowSettings = Root(pygame)
                        settings = Settings(windowSettings, pygame)
        pygame.quit()
        exit()

main = Main()