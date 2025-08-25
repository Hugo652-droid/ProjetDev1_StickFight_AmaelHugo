import pygame

from src.Root import Root
from src.Player import Player

class Main():
    def __init__(self):
        pygame.init()
        windowHome = Root(pygame)
        windowHome.changeBg()
        runningHome = True
        while runningHome:
            # Gérer les événements
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Si l'utilisateur clique sur la croix pour fermer

                        windowHome.closeRoot(pygame)
                        runningHome = False

        windowGame = Root(pygame)
        windowGame.changeColor((255, 255, 255))
        playerActif = Player("Amael", 100, 1, 100, 100)
        runningGame = True
        while runningGame:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        windowGame.closeRoot(pygame)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                playerActif.x -= 1
            if keys[pygame.K_d]:
                playerActif.x += 1
            if keys[pygame.K_w]:
                playerActif.y -= 1
            if keys[pygame.K_s]:
                playerActif.y += 1


            playerActif.draw(windowGame.screen, "images/test_stick.png")
            pygame.display.flip()






main = Main()