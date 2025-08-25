import pygame

from src.Root import Root


class Main():
    def __init__(self):
        pygame.init()
        windowHome = Root(pygame)
        runningHome = True
        while runningHome:
            # Gérer les événements
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Si l'utilisateur clique sur la croix pour fermer
                        windowHome.closeRoot(pygame)
                        runningHome = False

        windowGame = Root(pygame)
        windowGame.changeColor((255, 255, 0))
        runningGame = True
        while runningGame:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        windowGame.closeRoot(pygame)







main = Main()