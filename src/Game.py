from src.Player import Player
from src.Root import Root
import pygame

class Game:
    def __init__(self):
        pygame.init()
        windowGame = Root(pygame)
        clock = pygame.time.Clock()
        player1 = Player("Amael", 100, 1, 100, 100, "images/test_stick.png")
        player2 = Player("Hugo", 100, 1, 300, 300, "images/test_stick - Copie.png")
        runningGame = True
        while runningGame:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        windowGame.closeRoot(pygame)
                if event.type == pygame.QUIT:
                    runningGame = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if windowGame.button_rect_stop.collidepoint(event.pos):
                        windowGame.stop()


            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                player1.x -= 10
            if keys[pygame.K_d]:
                player1.x += 10
            if keys[pygame.K_w]:
                player1.y -= 10
            if keys[pygame.K_s]:
                player1.y += 10

            if keys[pygame.K_j]:
                player2.x -= 10
            if keys[pygame.K_l]:
                player2.x += 10
            if keys[pygame.K_i]:
                player2.y -= 10
            if keys[pygame.K_k]:
                player2.y += 10

            windowGame.changeBg()
            player1.draw(windowGame.screen)
            player2.draw(windowGame.screen)

            Root.stopButton(windowGame)

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
