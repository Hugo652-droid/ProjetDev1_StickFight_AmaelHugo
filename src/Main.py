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
        player1 = Player("Amael", 100, 1, 100, 100)
        player2 = Player("Hugo", 100, 1, 300, 300)
        runningGame = True
        while runningGame:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        windowGame.closeRoot(pygame)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                player1.x -= 1
            if keys[pygame.K_d]:
                player1.x += 1
            if keys[pygame.K_w]:
                player1.y -= 1
            if keys[pygame.K_s]:
                player1.y += 1

            keys = pygame.key.get_pressed()

            if keys[pygame.K_j]:
                player2.x -= 1
            if keys[pygame.K_l]:
                player2.x += 1
            if keys[pygame.K_i]:
                player2.y -= 1
            if keys[pygame.K_k]:
                player2.y += 1


            player1.draw(windowGame.screen, "images/test_stick.png")
            player2.draw(windowGame.screen, "images/test_stick - Copie.png")
            pygame.display.update()






main = Main()