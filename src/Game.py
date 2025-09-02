from src.Player import Player
from src.Root import Root
from src.Map import Map
from src.Weapons import Weapons
import time
import pygame
import random

class Game:
    def __init__(self):
        pygame.init()
        self.windowGame = Root(pygame)
        self.info_screen = pygame.display.Info()
        self.clock = pygame.time.Clock()
        self.image_player_left = "images/test_stick - Copie.png"
        self.image_player_right = "images/test_stick.png"
        self.image_player_stand = "images/stickman_test.png"
        self.image_player_crouch = "images/crouchnonarmé.png"
        self.font = pygame.font.SysFont('Arial', 25)
        self.runningGame = True
        self.paused = False
        self.cooldown_dropweapon = 5
        self.dict_weapons = [
            {
                "id": 1,
                "name": "gun",
                "img": 'images/img_wapon.png',
                "damage": 10,
                "attackSpeed": 1,
                "ammunition": 6,
                "width": 30,
                "height": 10
            },
            {
                "id": 2,
                "name": "fusil d'assaut",
                "img": 'images/fusildassaut.png',
                "damage": 1,
                "attackSpeed": 0.1,
                "ammunition": 30,
                "width": 30,
                "height": 10
            },
            {
                "id": 3,
                "name": "fusil a pome",
                "img": 'images/pompe.png',
                "damage": 20,
                "attackSpeed": 3,
                "ammunition": 10,
                "width": 30,
                "height": 70
            },
        ]

        self.score_player1 = 0
        self.score_player2 = 0

        self.createInstanse()
        self.launchGame()

    def createInstanse(self):
        margin = self.info_screen.current_w / 10  # 10% d’espace sur les côtés

        self.player1 = Player(
            "Amael",
            30,
            "",
            margin,  # distance depuis la gauche
            self.info_screen.current_h / 2,
            "images/test_stick.png"
        )

        self.player2 = Player(
            "Hugo",
            30,
            "",
            self.info_screen.current_w - margin - self.player1.rect.width,  # distance depuis la droite
            self.info_screen.current_h / 2,
            "images/test_stick - Copie.png"
        )

        self.floor = Map(self.windowGame, pygame, (self.info_screen.current_w / 2), (self.info_screen.current_h - 100),
                         (self.info_screen.current_w - 200), (self.info_screen.current_h / 5))

        self.floor2 = Map(self.windowGame, pygame, (self.info_screen.current_w / 2), (self.info_screen.current_h - 450),
                          (self.info_screen.current_w - self.info_screen.current_w / 2), (self.info_screen.current_h / 20))

        self.floor3 = Map(self.windowGame, pygame, (self.info_screen.current_w / 4), (self.info_screen.current_h - self.info_screen.current_w / 2.7),
                          self.info_screen.current_w - self.info_screen.current_w/ 1.7 ,(self.info_screen.current_h / 20))

        self.floor4 = Map(self.windowGame, pygame, (self.info_screen.current_w - self.info_screen.current_w / 4), (self.info_screen.current_h - self.info_screen.current_w / 2.7),
                          self.info_screen.current_w - self.info_screen.current_w / 1.7,
                          (self.info_screen.current_h / 20))

        self.floors = [self.floor, self.floor2, self.floor3, self.floor4]

        self.weapon_gun = []
        self.lastdrop = time.time()
        self.bullets = []
        self.restart = False

    def launchGame(self):
        while self.runningGame:
            self.playGame()

        pygame.quit()

    def changePlayer(self):
        if self.player1.weapon:
            if self.player1.direct_player == "Left":
                if self.player1.weapon.id == 1:
                    self.player1.img = pygame.image.load('images/stickman_test_armé_left.png').convert_alpha()
                elif self.player1.weapon.id == 2:
                    self.player1.img = pygame.image.load('images/stickman_test_armé_left_fusildassaut.png').convert_alpha()
                elif self.player1.weapon.id == 3:
                    self.player1.img = pygame.image.load('images/stickman_test_armé_pompe_left.png').convert_alpha()

        if self.player2.weapon:
            if self.player2.direct_player == "Left":
                if self.player2.weapon.id == 1:
                    self.player2.img = pygame.image.load('images/stickman_test_armé_left.png').convert_alpha()
                elif self.player2.weapon.id == 2:
                    self.player2.img = pygame.image.load(
                        'images/stickman_test_armé_left_fusildassaut.png').convert_alpha()
                elif self.player2.weapon.id == 3:
                    self.player2.img = pygame.image.load('images/stickman_test_armé_pompe_left.png').convert_alpha()

        if self.player1.weapon:
            if self.player1.direct_player == "Right":
                if self.player1.weapon.id == 1:
                    self.player1.img = pygame.image.load('images/stickman_test_armé_right.png').convert_alpha()
                elif self.player1.weapon.id == 2:
                    self.player1.img = pygame.image.load('images/stickman_test_armé_right_fusildassaut.png').convert_alpha()
                elif self.player1.weapon.id == 3:
                    self.player1.img = pygame.image.load('images/stickman_test_armé_pompe_right.png').convert_alpha()

        if self.player2.weapon:
            if self.player2.direct_player == "Right":
                if self.player2.weapon.id == 1:
                    self.player2.img = pygame.image.load('images/stickman_test_armé_right.png').convert_alpha()
                elif self.player2.weapon.id == 2:
                    self.player2.img = pygame.image.load('images/stickman_test_armé_right_fusildassaut.png').convert_alpha()
                elif self.player2.weapon.id == 3:
                    self.player2.img = pygame.image.load('images/stickman_test_armé_pompe_right.png').convert_alpha()

        if self.player1.playerIsDead():
            self.player1.img = pygame.image.load('images/stickman_dead.png').convert_alpha()

        if self.player2.playerIsDead():
            self.player2.img = pygame.image.load('images/stickman_dead.png').convert_alpha()

        if self.player1.playerIsDead():
            self.score_player2 += 1

        elif self.player2.playerIsDead():
            self.score_player1 += 1

        if self.player1.playerIsDead() or self.player2.playerIsDead() or self.restart:
            self.createInstanse()
            self.paused = False

    def createWeapons(self):

        weapon_random = random.choice(self.dict_weapons)

        newWeapon = Weapons(weapon_random["id"], weapon_random["img"], weapon_random["damage"], weapon_random["attackSpeed"], weapon_random["ammunition"], weapon_random["width"], weapon_random["height"])
        self.weapon_gun.append(newWeapon)

    def playGame(self):
        self.changePlayer()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runningGame = False

            if event.type != pygame.KEYDOWN:
                self.player2.modifImage(self.image_player_stand)
                self.player1.modifImage(self.image_player_stand)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.windowGame.button_rect_stop.collidepoint(event.pos):
                    self.paused = not self.paused

                elif self.windowGame.button_rect_restart.collidepoint(event.pos):
                    self.restart = True

                elif self.windowGame.button_rect_quit.collidepoint(event.pos):
                    self.windowGame.closeRoot(pygame)
                    self.runningGame = False
                    return


        if not self.paused:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.paused = not self.paused
                pygame.time.wait(175)
            if not self.player1.playerIsDead():
                if keys[pygame.K_e]:
                    if time.time() - self.player1.last_time_used_attack > self.player1.cooldown_attack and self.player1.weapon == 0:
                        self.player1.last_time_used_attack = time.time()
                        if self.player1.direct_player == "Left":
                            self.player1.dashLeft()
                        elif self.player1.direct_player == "Right":
                            self.player1.dashRight()
                        self.player1.attacking = True
                    elif time.time() - self.player1.last_time_used_attack > self.player1.cooldown_attack :
                        self.player1.noAmmunitionInWeapon()
                        self.player1.last_time_used_attack = time.time()
                        self.player1.attacking = True
                    else :
                        self.player1.attacking = False

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
                if keys[pygame.K_s]:
                    self.player1.modifImage(self.image_player_crouch)
            else:
                if self.player1.y != self.info_screen.current_h:
                    self.player1.y += 10

            if not self.player2.playerIsDead():

                if keys[pygame.K_o]:
                    if time.time() - self.player2.last_time_used_attack > self.player2.cooldown_attack and self.player2.weapon == 0:
                        self.player2.last_time_used_attack = time.time()
                        if self.player2.direct_player == "Left":
                            self.player2.dashLeft()
                        elif self.player2.direct_player == "Right":
                            self.player2.dashRight()
                        self.player2.attacking = True
                    elif time.time() - self.player2.last_time_used_attack > self.player2.cooldown_attack :
                        self.player2.noAmmunitionInWeapon()
                        self.player2.last_time_used_attack = time.time()
                        self.player2.attacking = True
                    else:
                        self.player2.attacking = False

                if keys[pygame.K_j]:
                    self.player2.goLeft()
                    self.player2.modifImage(self.image_player_left)
                if keys[pygame.K_l]:
                    self.player2.goRight()
                    self.player2.modifImage(self.image_player_right)
                if keys[pygame.K_k]:
                    self.player2.modifImage(self.image_player_crouch)
                if keys[pygame.K_i]:
                    self.player2.goUp(time.time())
                    self.player2.y += 10
                else :
                    if self.player2.y != self.info_screen.current_h:
                        self.player2.y += 10
            else:
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

        self.clock.tick(200)

    def reloadPage(self):
        if not self.paused:
            self.windowGame.changeBg('images/img_bg_game.png')
            for weapon in self.weapon_gun :
                weapon.draw(self.windowGame.screen)
            self.player1.draw(self.windowGame.screen, self.font)
            self.player2.draw(self.windowGame.screen, self.font)

            for floor in self.floors:

                floor.draw(self.windowGame.screen)

            if self.player1.attacking :
                bullet = self.player1.simple_attack(self.player2)
                if not bullet:
                    self.player1.attacking = False
                else:
                    self.bullets.append(bullet)
                    self.player1.attacking = False
            if self.player2.attacking :
                bullet = self.player2.simple_attack(self.player1)
                if not bullet:
                    self.player2.attacking = False
                else :
                    self.bullets.append(bullet)
                    self.player2.attacking = False

            for bullet in self.bullets:
                bullet.shot()
                bullet.draw(self.windowGame)

            self.windowGame.scores(self.font, self.score_player1, self.score_player2)

        else:
            self.windowGame.stop()

            self.windowGame.scores(self.font, self.score_player1, self.score_player2)

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

        if self.player1.y > self.info_screen.current_h:
            self.player1.hp = 0

        elif self.player2.y > self.info_screen.current_h:
            self.player2.hp = 0

        for floor in self.floors:

            if self.player1.rect.colliderect(floor.rect):
                dx = min(self.player1.rect.right - floor.rect.left,
                         floor.rect.right - self.player1.rect.left)
                dy = min(self.player1.rect.bottom - floor.rect.top,
                         floor.rect.bottom - self.player1.rect.top)

                if dx < dy:

                    if self.player1.rect.centerx < floor.rect.centerx:
                        self.player1.x -= dx
                    else:
                        self.player1.x += dx
                else:

                    if self.player1.rect.centery < floor.rect.centery:
                        self.player1.y -= dy
                    else:
                        self.player1.y += dy

            if self.player2.rect.colliderect(floor.rect):
                dx = min(self.player2.rect.right - floor.rect.left,
                         floor.rect.right - self.player2.rect.left)
                dy = min(self.player2.rect.bottom - floor.rect.top,
                         floor.rect.bottom - self.player2.rect.top)

                if dx < dy:

                    if self.player2.rect.centerx < floor.rect.centerx:
                        self.player2.x -= dx
                    else:
                        self.player2.x += dx
                else:

                    if self.player2.rect.centery < floor.rect.centery:
                        self.player2.y -= dy
                    else:
                        self.player2.y += dy


            for weapon in self.weapon_gun:
                if weapon.rect_weapon.colliderect(floor.rect):
                    weapon.rect_weapon.y -= 10

        for bullet in self.bullets:
            if bullet.rect.colliderect(self.player1.rect):
                if bullet.playerAttackName == self.player1.name:
                    pass
                else:
                    self.player1.tackDammage(self.player2.damage)
                    self.bullets.remove(bullet)


            if bullet.rect.colliderect(self.player2.rect):
                if bullet.playerAttackName == self.player2.name:
                    pass
                else:
                    self.player2.tackDammage(self.player1.damage)
                    self.bullets.remove(bullet)


            if not bullet.rect.colliderect(self.windowGame.rect):
                self.bullets.remove(bullet)


        for weapon in self.weapon_gun:
            if weapon.rect_weapon.colliderect(self.player1.rect):
                self.player1.weapon = weapon
                self.weapon_gun.remove(weapon)

            elif weapon.rect_weapon.colliderect(self.player2.rect):
                self.player2.weapon = weapon
                self.weapon_gun.remove(weapon)
