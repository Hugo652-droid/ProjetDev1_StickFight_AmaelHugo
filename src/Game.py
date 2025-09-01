from src.Bullets import Bullet
from src.Player import Player
from src.Root import Root
from src.Map import Map
from src.Weapons import Weapons
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
        self.weapon_gun = Weapons('images/img_wapon.png')
        self.floor = Map(self.windowGame, pygame, (self.info_screen.current_w/2), (self.info_screen.current_h-100))
        self.image_player_left = "images/test_stick - Copie.png"
        self.image_player_right = "images/test_stick.png"
        self.image_player_stand = "images/stickman_test.png"
        self.font = pygame.font.SysFont('Arial', 25)
        self.runningGame = True
        self.paused = False
        self.lastdrop = time.time()
        self.cooldown_dropweapon = 3
        self.weapon_gun = []
        self.bullet = Bullet(self.windowGame)
        self.launchGame()

    def launchGame(self):
        while self.runningGame:
            self.playGame()
            if self.player1.playerIsDead():
                self.player1.img = pygame.image.load('images/stickman_dead.png').convert_alpha()

            if self.player2.playerIsDead():
                self.player2.img = pygame.image.load('images/stickman_dead.png').convert_alpha()

        pygame.quit()

    def createWeapons(self):
        newWeapon = Weapons('images/img_wapon.png')
        self.weapon_gun.append(newWeapon)
        print(self.weapon_gun)

    def playGame(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runningGame = False

            if event.type != pygame.KEYDOWN:
                self.player2.modifImage(self.image_player_stand)
                self.player1.modifImage(self.image_player_stand)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.windowGame.button_rect_stop.collidepoint(event.pos):
                    self.paused = not self.paused

                elif self.windowGame.button_rect_quit.collidepoint(event.pos):
                    self.windowGame.closeRoot(pygame)
                    self.runningGame = False
                    return

        if not self.paused:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.paused = not self.paused
                pygame.time.wait(175)
            if keys[pygame.K_e]:
                if time.time() - self.player1.last_time_used_attack > self.player1.cooldown_attack:
                    self.player1.last_time_used_attack = time.time()
                    if self.player1.direct_player == "Left":
                        self.player1.dashLeft()
                    elif self.player1.direct_player == "Right":
                        self.player1.dashRight()
                    self.player1.attacking = True
                else :
                    self.player1.attacking = False

            if keys[pygame.K_o]:
                if time.time() - self.player2.last_time_used_attack > self.player2.cooldown_attack:
                    self.player2.last_time_used_attack = time.time()
                    if self.player2.direct_player == "Left":
                        self.player2.dashLeft()
                    elif self.player2.direct_player == "Right":
                        self.player2.dashRight()
                    self.player2.attacking = True
                else:
                    self.player2.attacking = False

            if keys[pygame.K_a]:
                self.player1.goLeft()
                self.player1.modifImage(self.image_player_left)
            if keys[pygame.K_d]:
                self.player1.goRight()
                self.player1.modifImage(self.image_player_right)
            if keys[pygame.K_w]:
                self.player1.goUp(time.time())
                self.player1.y += 10
            else:
                if self.player1.y != self.info_screen.current_h:
                    self.player1.y += 10
            if keys[pygame.K_j]:
                self.player2.goLeft()
                self.player2.modifImage(self.image_player_left)
            if keys[pygame.K_l]:
                self.player2.goRight()
                self.player2.modifImage(self.image_player_right)
            if keys[pygame.K_i]:
                self.player2.goUp(time.time())
                self.player2.y += 10
            else :
                if self.player2.y != self.info_screen.current_h:
                    self.player2.y += 10

            if time.time() - self.lastdrop > self.cooldown_dropweapon:
                self.lastdrop = time.time()
                self.createWeapons()

            for weapon in self.weapon_gun:
                if weapon.rect_weapon.y != self.info_screen.current_h:
                    weapon.rect_weapon.y += 10

            self.collision()

        else :
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.paused = not self.paused
                pygame.time.wait(175)

        self.reloadPage()

        self.clock.tick(120)

    def reloadPage(self):
        if not self.paused:
            self.windowGame.changeBg('images/img_bg_game.png')
            for weapon in self.weapon_gun :
                weapon.draw(self.windowGame.screen)
            self.player1.draw(self.windowGame.screen, self.font)
            self.player2.draw(self.windowGame.screen, self.font)
            self.bullet.draw(100, 100)
            self.floor.draw(self.windowGame.screen)
            if self.player1.attacking :
                self.player1.simple_attack(self.player2, time.time(), "")
                self.player1.attacking = False
            if self.player2.attacking :
                self.player2.simple_attack(self.player1, time.time(), "")
                self.player2.attacking = False
        else:
            self.windowGame.stop()

        self.windowGame.stopButton(self.paused)

        pygame.display.flip()

    def collision(self):
        if self.player1.rect.colliderect(self.player2.rect) and self.player1.rect.x > self.player2.x:
            self.player2.x -= 5
            self.player1.x += 5

        elif self.player2.rect.colliderect(self.player1.rect) and self.player2.rect.x > self.player1.x:
            self.player2.x += 5
            self.player1.x -= 5

        if self.player1.rect.colliderect(self.player2.rect) and self.player1.rect.x < self.player2.x:
            self.player2.x += 5
            self.player1.x -= 5

        elif self.player2.rect.colliderect(self.player1.rect) and self.player2.rect.x < self.player1.x:
            self.player2.x -= 5
            self.player1.x += 5

        if self.player1.rect.colliderect(self.floor.rect):
            self.player1.y -= 10

        if self.player2.rect.colliderect(self.floor.rect):
            self.player2.y -= 10

        for weapon in self.weapon_gun:
            if weapon.rect_weapon.colliderect(self.floor.rect):
                weapon.rect_weapon.y -= 10
