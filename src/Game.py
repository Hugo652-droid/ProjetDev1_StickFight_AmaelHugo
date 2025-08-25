from src.Player import Player

class Game:
    def __init__(self, windowGame, pygame):

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

            windowGame.changeBg()

            player1.draw(windowGame.screen, "images/test_stick.png")
            player2.draw(windowGame.screen, "images/test_stick - Copie.png")
            pygame.display.update()