from src.Player import Player
from src.Root import Root
from src.Map import Map
import time
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.windowGame = Root(pygame)
        self.info_screen = pygame.display.Info()
        self.clock = pygame.time.Clock()
        self.player1 = Player("Amael", 100, 1, 300, (self.info_screen.current_h/2), "images/test_stick.png")
        self.player2 = Player("Hugo", 100, 1, (self.info_screen.current_w-300), (self.info_screen.current_h/2), "images/test_stick - Copie.png")
        self.floor = Map(self.windowGame, pygame, (self.info_screen.current_w/2), (self.info_screen.current_h-100))
        self.image_player_left = "images/test_stick - Copie.png"
        self.image_player_right = "images/test_stick.png"
        self.image_player_stand = "images/stickman_test.png"
        self.launchGame()

    def launchGame(self):
        runningGame = True
        self.paused = False
        while runningGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runningGame = False

                if event.type != pygame.KEYDOWN:
                    self.player2.modifImage(self.image_player_stand)
                    self.player1.modifImage(self.image_player_stand)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.windowGame.button_rect_stop.collidepoint(event.pos):
                        self.paused = not self.paused

                    elif self.windowGame.button_rect_quit.collidepoint(event.pos):
                        self.windowGame.closeRoot(pygame)
                        runningGame = False

            if not runningGame:
                break

            if not self.paused:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    self.paused = not self.paused
                    pygame.time.wait(175)
                if keys[pygame.K_a]:
                    self.player1.goLeft()
                    self.player1.modifImage(self.image_player_left)
                if keys[pygame.K_d]:
                    self.player1.goRight()
                    self.player1.modifImage(self.image_player_right)
                if keys[pygame.K_w]:
                    self.player1.goUp(time.time())
                else:
                    if self.player1.y != self.info_screen.current_h:
                        self.player1.y += 10
                if self.player1.rect.colliderect(self.player2.rect):
                    print("collision")

                if keys[pygame.K_j]:
                    self.player2.goLeft()
                    self.player2.modifImage(self.image_player_left)
                if keys[pygame.K_l]:
                    self.player2.goRight()
                    self.player2.modifImage(self.image_player_right)
                if keys[pygame.K_i]:
                    self.player2.goUp(time.time())

                else :
                    if self.player2.y != self.info_screen.current_h:
                        self.player2.y += 10

                if self.player1.rect.colliderect(self.player2.rect) and self.player1.rect.x > self.player2.x:
                    self.player2.x -= 10

                elif self.player2.rect.colliderect(self.player1.rect) and self.player2.rect.x > self.player1.x:
                    self.player1.x -= 10

                if self.player1.rect.colliderect(self.player2.rect) and self.player1.rect.x < self.player2.x:
                    self.player2.x += 10

                elif self.player2.rect.colliderect(self.player1.rect) and self.player2.rect.x < self.player1.x:
                    self.player1.x += 10


                if self.player1.rect.colliderect(self.floor.rect):
                    self.player1.y -= 10

                elif self.player2.rect.colliderect(self.floor.rect):
                    self.player2.y -= 10

            else :
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    self.paused = not self.paused
                    pygame.time.wait(175)

            if not self.paused:
                self.windowGame.changeBg('images/img_bg_game.png')

                self.player1.draw(self.windowGame.screen)
                self.player2.draw(self.windowGame.screen)
                self.floor.draw(self.windowGame.screen)
            else:
                self.windowGame.stop()

            Root.stopButton(self.windowGame, self.paused)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
