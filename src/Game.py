"""
--
Auteur : Amael Rochat et Hugo Rod
Date de départ : 18.08.2025
Date de fin : --.--.----
Projet : Projet Dev 1 (sticKOnion)
--
Nom fichier : Game.py
Description fichier : Creation et gestion des parties et du jeu
--
"""

from src.Player import Player
from src.Root import Root
from src.Map import Map
from src.Weapons import Weapons
from src.Data.weapon import dict_weapons
import time
import pygame
import random

class Game:
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 25)
        self.window_game = Root(self.font)
        self.info_screen = pygame.display.Info()
        self.clock = pygame.time.Clock()

        self.image_player1_left = "images/imgCharacters/imgPlayer1/runPlayer1/stickman_go_left_player1.png"
        self.image_player1_right = "images/imgCharacters/imgPlayer1/runPlayer1/stickman_go_right_player1.png"
        self.image_player1_stand = "images/imgCharacters/imgPlayer1/stickman_stand_player1.png"

        self.image_player2_left = "images/imgCharacters/imgPlayer2/runPlayer2/stickman_go_left_player2.png"
        self.image_player2_right = "images/imgCharacters/imgPlayer2/runPlayer2/stickman_go_right_player2.png"
        self.image_player2_stand = "images/imgCharacters/imgPlayer2/stickman_stand_player2.png"

        self.image_player2_crouch = "images/imgCharacters/imgPlayer2/crouchPlayer2/Player2_crouch.png"
        self.image_player1_crouch = "images/imgCharacters/imgPlayer1/crouchPlayer1/Player1_crouch.png"

        self.font = pygame.font.Font("assets/Shooting Star.ttf", 100)
        self.running_game = True
        self.paused = False
        self.cooldown_drop_weapon = 5
        self.heal_points_start = 100
        self.weapons = dict_weapons
        self.score_player1 = 0
        self.score_player2 = 0
        self.last_drop = time.time()
        self.weapon_gun = []
        self.bullets = []
        self.restart = False
        self.floors = []

        self.sound_shot = pygame.mixer.Sound("./sounds/gun-shot.mp3")
        self.sound_falling = pygame.mixer.Sound("./sounds/falling-character.mp3")
        self.sound_background = pygame.mixer.Sound("./sounds/fighting-battle-warrior-drums.mp3")
        self.sounds = [self.sound_shot, self.sound_falling, self.sound_background]

        pygame.mixer.Channel(0).play(self.sound_background, -1)

        self.createInstanse()


    def createInstanse(self):
        margin = self.info_screen.current_w / 10  # 10% d’espace sur les côtés

        self.player1 = Player(
            "Player 1",
            self.heal_points_start,
            margin,  # distance depuis la gauche
            self.info_screen.current_h / 2,
            "images/imgCharacters/imgPlayer1/runPlayer1/stickman_go_right_player1.png",
            self.window_game.screen,
            "images/imgCharacters/imgPlayer1/stickman_stand_player1.png",
            (252, 186, 3),
        )

        self.player2 = Player(
            "Player 2",
            self.heal_points_start,
            self.info_screen.current_w - margin - self.player1.rect.width,  # distance depuis la droite
            self.info_screen.current_h / 2,
            "images/imgCharacters/imgPlayer2/runPlayer2/stickman_go_right_player2.png",
            self.window_game.screen,
            "images/imgCharacters/imgPlayer2/stickman_stand_player2.png",
            (160, 7, 237),
        )

        floor = Map(self.window_game,
                    (self.info_screen.current_w / 2), (self.info_screen.current_h - 100),
                         (self.info_screen.current_w - 200), (self.info_screen.current_h / 5))

        mid_platform = Map(self.window_game, (self.info_screen.current_w / 2), (self.info_screen.current_h - self.info_screen.current_h / 3),
                          (self.info_screen.current_w - self.info_screen.current_w / 2), (self.info_screen.current_h / 20))

        top_left_platform = Map(self.window_game, (self.info_screen.current_w / 4), (self.info_screen.current_h  / 2.5),
                          self.info_screen.current_w - self.info_screen.current_w/ 1.7 ,(self.info_screen.current_h / 20))

        top_right_platform = Map(self.window_game, (self.info_screen.current_w - self.info_screen.current_w / 4), (self.info_screen.current_h / 2.5),
                          self.info_screen.current_w - self.info_screen.current_w / 1.7,
                          (self.info_screen.current_h / 20))

        self.map1 = [floor, mid_platform, top_left_platform, top_right_platform]


        floor2 = Map(self.window_game,
                     self.info_screen.current_w / 2,
                     self.info_screen.current_h - 100,
                     self.info_screen.current_w - 200,
                     self.info_screen.current_h / 5)

        left_platform2 = Map(self.window_game,
                             self.info_screen.current_w / 4,
                             self.info_screen.current_h - self.info_screen.current_h / 2.5,
                             self.info_screen.current_w / 4,
                             self.info_screen.current_h / 20)

        middle_platform2 = Map(self.window_game,
                               self.info_screen.current_w / 2,
                               self.info_screen.current_h - self.info_screen.current_h / 3,
                               self.info_screen.current_w / 4,
                               self.info_screen.current_h / 20)

        right_platform2 = Map(self.window_game,
                              self.info_screen.current_w - self.info_screen.current_w / 4,
                              self.info_screen.current_h - self.info_screen.current_h / 2.5,
                              self.info_screen.current_w / 4,
                              self.info_screen.current_h / 20)

        self.map2 = [floor2, left_platform2, middle_platform2, right_platform2]

        center_platform2 = Map(
            self.window_game,
            self.info_screen.current_w / 2,
            self.info_screen.current_h / 2,
            self.info_screen.current_w / 3,
            self.info_screen.current_h / 20
        )

        side_left_platform2 = Map(
            self.window_game,
            self.info_screen.current_w / 5,
            self.info_screen.current_h / 3,
            self.info_screen.current_w / 5,
            self.info_screen.current_h / 25
        )

        side_right_platform2 = Map(
            self.window_game,
            self.info_screen.current_w - self.info_screen.current_w / 5,
            self.info_screen.current_h / 3,
            self.info_screen.current_w / 5,
            self.info_screen.current_h / 25
        )

        self.map3 = [center_platform2, side_left_platform2, side_right_platform2]

        floor3 = Map(
            self.window_game,
            self.info_screen.current_w / 2,
            self.info_screen.current_h - 100,
            self.info_screen.current_w - 200,
            self.info_screen.current_h / 6
        )

        left_step3 = Map(
            self.window_game,
            self.info_screen.current_w / 4,
            self.info_screen.current_h - self.info_screen.current_h / 3,
            self.info_screen.current_w / 5,
            self.info_screen.current_h / 20
        )

        middle_step3 = Map(
            self.window_game,
            self.info_screen.current_w / 2,
            self.info_screen.current_h - self.info_screen.current_h / 2.5,
            self.info_screen.current_w / 5,
            self.info_screen.current_h / 20
        )

        right_step3 = Map(
            self.window_game,
            self.info_screen.current_w - self.info_screen.current_w / 4,
            self.info_screen.current_h - self.info_screen.current_h / 3,
            self.info_screen.current_w / 5,
            self.info_screen.current_h / 20
        )

        self.map4 = [floor3, left_step3, middle_step3, right_step3]

        maps = [self.map1, self.map2, self.map3, self.map4 ]

        self.floors = random.choice(maps)

        self.last_drop = time.time()
        self.weapon_gun = []
        self.bullets = []
        self.restart = False

    def launchGame(self):
        while self.running_game:
            self.playGame()

    def changePlayer(self):
        if self.player1.weapon:
            if self.player1.direct_player == "Left":
                if self.player1.weapon.id == 1:
                    self.player1.img = pygame.image.load(
                        'images/imgCharacters/imgPlayer1/armedPlayer1/armedGunPlayer1/stickman_armed_left_gun_player1.png').convert_alpha()
                elif self.player1.weapon.id == 2:
                    self.player1.img = pygame.image.load(
                        'images/imgCharacters/imgPlayer1/armedPlayer1/armedRiflePlayer1/stickman_armed_left_rifle_player1.png').convert_alpha()
                elif self.player1.weapon.id == 3:
                    self.player1.img = pygame.image.load(
                        'images/imgCharacters/imgPlayer1/armedPlayer1/armedShotgunPlayer1/stickman_armed_pompe_left_player1.png').convert_alpha()
                elif self.player1.weapon.id == 4:
                    self.player1.img = pygame.image.load(
                        'images/imgCharacters/imgPlayer1/armedPlayer1/armedSniperPlayer1/stickman_armed_left_sniper_player1.png').convert_alpha()

        if self.player2.weapon:
            if self.player2.direct_player == "Left":
                if self.player2.weapon.id == 1:
                    self.player2.img = pygame.image.load(
                        'images/imgCharacters/imgPlayer2/armedPlayer2/armedGunPlayer2/stickman_armed_left_gun_player2.png').convert_alpha()
                elif self.player2.weapon.id == 2:
                    self.player2.img = pygame.image.load(
                        'images/imgCharacters/imgPlayer2/armedPlayer2/armedRiflePlayer2/stickman_armed_left_rifle_player2.png').convert_alpha()
                elif self.player2.weapon.id == 3:
                    self.player2.img = pygame.image.load(
                        'images/imgCharacters/imgPlayer2/armedPlayer2/armedShotgunPlayer2/stickman_armed_pompe_left_player2.png').convert_alpha()
                elif self.player2.weapon.id == 4:
                    self.player2.img = pygame.image.load(
                        'images/imgCharacters/imgPlayer2/armedPlayer2/armedSniperPlayer2/stickman_armed_left_sniper_player2.png').convert_alpha()

        if self.player1.weapon:
            if self.player1.direct_player == "Right":
                if self.player1.weapon.id == 1:
                    self.player1.img = pygame.image.load(
                        'images/imgCharacters/imgPlayer1/armedPlayer1/armedGunPlayer1/stickman_armed_right_gun_player1.png').convert_alpha()
                elif self.player1.weapon.id == 2:
                    self.player1.img = pygame.image.load(
                        'images/imgCharacters/imgPlayer1/armedPlayer1/armedRiflePlayer1/stickman_armed_right_rifle_player1.png').convert_alpha()
                elif self.player1.weapon.id == 3:
                    self.player1.img = pygame.image.load(
                        'images/imgCharacters/imgPlayer1/armedPlayer1/armedShotgunPlayer1/stickman_armed_pompe_right_player1.png').convert_alpha()
                elif self.player1.weapon.id == 4:
                    self.player1.img = pygame.image.load(
                        'images/imgCharacters/imgPlayer1/armedPlayer1/armedSniperPlayer1/stickman_armed_right_sniper_player1.png').convert_alpha()

        if self.player2.weapon:
            if self.player2.direct_player == "Right":
                if self.player2.weapon.id == 1:
                    self.player2.img = pygame.image.load(
                        'images/imgCharacters/imgPlayer2/armedPlayer2/armedGunPlayer2/stickman_armed_right_gun_player2.png').convert_alpha()
                elif self.player2.weapon.id == 2:
                    self.player2.img = pygame.image.load(
                        'images/imgCharacters/imgPlayer2/armedPlayer2/armedRiflePlayer2/stickman_armed_right_rifle_player2.png').convert_alpha()
                elif self.player2.weapon.id == 3:
                    self.player2.img = pygame.image.load(
                        'images/imgCharacters/imgPlayer2/armedPlayer2/armedShotgunPlayer2/stickman_armed_pompe_right_player2.png').convert_alpha()
                elif self.player2.weapon.id == 4:
                    self.player2.img = pygame.image.load(
                        'images/imgCharacters/imgPlayer2/armedPlayer2/armedSniperPlayer2/stickman_armed_right_sniper_player2.png').convert_alpha()

        if self.player1.playerIsDead():
            self.score_player2 += 1

        elif self.player2.playerIsDead():
            self.score_player1 += 1

        if self.player1.playerIsDead():
            self.player1.img = pygame.image.load(
                'images/imgCharacters/imgPlayer1/deadPlayer1/stickman_dead_player1.png').convert_alpha()
            self.reloadPage()
            pygame.time.wait(2000)
        elif self.player2.playerIsDead():
            self.player2.img = pygame.image.load(
                'images/imgCharacters/imgPlayer2/deadPlayer2/stickman_dead_player2.png').convert_alpha()
            self.reloadPage()
            pygame.time.wait(2000)

        if self.player1.playerIsDead() or self.player2.playerIsDead() or self.restart:
            self.createInstanse()
            self.paused = False

    def createWeapons(self):

        random_nb = random.randint(1, 100)

        if random_nb <= 13:
            weapon = self.weapons[3]
            new_weapon = Weapons(weapon["id"], weapon["img"], weapon["damage"],
                                weapon["attackSpeed"], weapon["ammunition"], weapon["width"],
                                weapon["height"], self.window_game.screen)
            self.weapon_gun.append(new_weapon)

        elif random_nb <= 36:
            weapon = self.weapons[2]
            new_weapon = Weapons(weapon["id"], weapon["img"], weapon["damage"],
                                weapon["attackSpeed"], weapon["ammunition"], weapon["width"],
                                weapon["height"], self.window_game.screen)
            self.weapon_gun.append(new_weapon)

        elif random_nb <= 68:
            weapon = self.weapons[1]
            new_weapon = Weapons(weapon["id"], weapon["img"], weapon["damage"],
                                weapon["attackSpeed"], weapon["ammunition"], weapon["width"],
                                weapon["height"], self.window_game.screen)
            self.weapon_gun.append(new_weapon)

        elif random_nb <= 100:
            weapon = self.weapons[0]
            new_weapon = Weapons(weapon["id"], weapon["img"], weapon["damage"],
                                weapon["attackSpeed"], weapon["ammunition"], weapon["width"],
                                weapon["height"], self.window_game.screen)
            self.weapon_gun.append(new_weapon)

    def playGame(self):
        self.changePlayer()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running_game = False

            if event.type != pygame.KEYDOWN:
                self.player2.modifImage(self.image_player2_stand)
                self.player1.modifImage(self.image_player1_stand)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.paused:
                    if self.window_game.button_rect_restart.collidepoint(event.pos):
                        self.restart = True

                    elif self.window_game.button_rect_quit.collidepoint(event.pos):
                        self.window_game.closeRoot()
                        self.running_game = False
                        return

        if not self.paused:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.paused = not self.paused
                pygame.time.wait(175)
            if not self.player1.playerIsDead():
                if keys[pygame.K_e]:
                    if time.time() - self.player1.last_time_used_attack > self.player1.cooldown_attack and self.player1.weapon.id == 0:
                        self.player1.last_time_used_attack = time.time()
                        if self.player1.direct_player == "Left":
                            self.player1.dashLeft()
                        elif self.player1.direct_player == "Right":
                            self.player1.dashRight()
                        self.player1.attacking = True
                    elif time.time() - self.player1.last_time_used_attack > self.player1.cooldown_attack :
                        pygame.mixer.Channel(1).stop()
                        pygame.mixer.Channel(1).play(self.sound_shot)
                        self.player1.noAmmunitionInWeapon(self.player1)
                        self.player1.last_time_used_attack = time.time()
                        self.player1.attacking = True
                    else :
                        self.player1.attacking = False
                if keys[pygame.K_q]:
                    if time.time() - self.player1.last_time_used_push > self.player1.cooldown_push:
                        self.player1.last_time_used_push = time.time()
                        self.player1.pushing = True
                if keys[pygame.K_a]:
                    self.player1.goLeft()
                    self.player1.modifImage(self.image_player1_left)
                if keys[pygame.K_d]:
                    self.player1.goRight()
                    self.player1.modifImage(self.image_player1_right)
                if keys[pygame.K_w]:
                    self.player1.jump(time.time())
                if keys[pygame.K_s]:
                    if self.player1.rect.bottom > self.floors[0].rect.top:
                        self.player1.modifImage(self.image_player1_crouch)
                    else:
                        self.player1.modifImage(self.image_player1_crouch)
                        self.player1.goDown(time.time())
            else:
                if self.player1.y != self.info_screen.current_h:
                    self.player1.y += 10

            if not self.player2.playerIsDead():

                if keys[pygame.K_o]:
                    if time.time() - self.player2.last_time_used_attack > self.player2.cooldown_attack and self.player2.weapon.id == 0:
                        self.player2.last_time_used_attack = time.time()
                        if self.player2.direct_player == "Left":
                            self.player2.dashLeft()
                        elif self.player2.direct_player == "Right":
                            self.player2.dashRight()
                        self.player2.attacking = True
                    elif time.time() - self.player2.last_time_used_attack > self.player2.cooldown_attack :
                        pygame.mixer.Channel(1).stop()
                        pygame.mixer.Channel(1).play(self.sound_shot)
                        self.player2.noAmmunitionInWeapon(self.player2)
                        self.player2.last_time_used_attack = time.time()
                        self.player2.attacking = True
                    else:
                        self.player2.attacking = False
                if keys[pygame.K_u]:
                    if time.time() - self.player2.last_time_used_push > self.player2.cooldown_push:
                        self.player2.last_time_used_push = time.time()
                        self.player2.pushing = True
                if keys[pygame.K_j]:
                    self.player2.goLeft()
                    self.player2.modifImage(self.image_player2_left)
                if keys[pygame.K_l]:
                    self.player2.goRight()
                    self.player2.modifImage(self.image_player2_right)
                if keys[pygame.K_k]:
                    if self.player2.rect.bottom > self.floors[0].rect.top:
                        self.player2.modifImage(self.image_player2_crouch)
                    else:
                        self.player2.modifImage(self.image_player2_crouch)
                        self.player2.goDown(time.time())
                if keys[pygame.K_i]:
                    self.player2.jump(time.time())
            else:
                if self.player2.y != self.info_screen.current_h:
                    self.player2.y += 10

            if time.time() - self.last_drop > self.cooldown_drop_weapon:
                self.last_drop = time.time()
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
            pygame.mouse.set_visible(False)
            self.window_game.changeBg('images/imgBackgrounds/gamePageBgs/gameBgs/test_blue_bg.jpg')

            for weapon in self.weapon_gun :
                weapon.draw(self.floors, self.player1, self.player2)

            if self.player1.jumping > 0 :
                self.player1.y -= 20
                if self.player1.jumping <= 0 :
                    self.player1.jumping = 0
                else :
                    self.player1.jumping -= 20
            elif self.player1.jumping <= 0:
                if self.player1.y != self.info_screen.current_h:
                    self.player1.y += 10

            if self.player2.jumping > 0:
                self.player2.y -= 20
                if self.player2.jumping <= 0:
                    self.player2.jumping = 0
                else:
                    self.player2.jumping -= 20
            elif self.player2.jumping <= 0:
                if self.player2.y != self.info_screen.current_h:
                    self.player2.y += 10


            self.player1.draw(self.font)
            self.player2.draw(self.font)

            for floor in self.floors:

                floor.draw(self.window_game.screen)

            if self.player1.attacking :
                bullet = self.player1.simpleAttack(self.player2)
                if not bullet:
                    self.player1.attacking = False

                else:
                    self.bullets.append(bullet)
                    self.player1.attacking = False

            if self.player2.attacking :
                bullet = self.player2.simpleAttack(self.player1)
                if not bullet:
                    self.player2.attacking = False

                else :
                    self.bullets.append(bullet)
                    self.player2.attacking = False




            for bullet in self.bullets:
                bullet.shot()
                bullet.draw(self.window_game)

            self.window_game.scores_player1(self.font, self.score_player1, self.player1)
            self.window_game.scores_player2(self.font, self.score_player2, self.player2)

            if self.player1.playerIsDead():
                self.window_game.win(self.player2)
            elif self.player2.playerIsDead():
                self.window_game.win(self.player1)

        else:

            pygame.mouse.set_visible(True)
            self.window_game.stop()


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
                if bullet.player_attack_name == self.player1.name:
                    pass
                else:
                    self.player1.tackDammage(self.player2.damage)
                    self.bullets.remove(bullet)


            if bullet.rect.colliderect(self.player2.rect):
                if bullet.player_attack_name == self.player2.name:
                    pass
                else:
                    self.player2.tackDammage(self.player1.damage)
                    self.bullets.remove(bullet)


            if not bullet.rect.colliderect(self.window_game.rect):
                self.bullets.remove(bullet)


        for weapon in self.weapon_gun:
            if weapon.rect_weapon.colliderect(self.player1.rect):
                self.player1.weapon = weapon
                self.weapon_gun.remove(weapon)

            elif weapon.rect_weapon.colliderect(self.player2.rect):
                self.player2.weapon = weapon
                self.weapon_gun.remove(weapon)

        if self.player1.pushing and self.player1.rect.colliderect(self.player2.rect):
            self.player1.pushing = False
            if self.player1.direct_player == "Left":
                self.player2.dashLeft()
            elif self.player1.direct_player == "Right":
                self.player2.dashRight()
        else:
            self.player1.pushing = False
        if self.player2.pushing and self.player2.rect.colliderect(self.player1.rect):
            self.player2.pushing = False
            if self.player2.direct_player == "Left":
                self.player1.dashLeft()
            elif self.player2.direct_player == "Right":
                self.player1.dashRight()
        else:
            self.player2.pushing = False
