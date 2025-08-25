import pygame

from src.Root import Root
from src.Player import Player
from src.Game import Game

class Main():
    def __init__(self):
        pygame.init()
        windowHome = Root(pygame)
        windowHome.changeBg()

        windowHome.buttonPlay()

        windowHome.buttonQuit()

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

                        windowGame = Root(pygame)
                        game = Game(windowGame, pygame)

                    if windowHome.button_rect_quit.collidepoint(event.pos):
                        windowHome.closeRoot(pygame)
                        runningHome = False










main = Main()