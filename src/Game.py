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
from src.Powers import Powers
from src.Root import Root
from src.Map import Map
from src.Weapons import Weapons
from src.Data.weapon import weapons
from src.Data.powers import powers
from src.Data.imagesPlayer import imagesPlayer
from src.Data.maps import maps
import time
import pygame
import random

class Game:
    def __init__(self, game_mod):
        # Variable for the window and the game
        self.game_mod = game_mod
        self.font = pygame.font.Font("assets/Shooting Star.ttf", 100)
        self.window_game = Root(self.font)

        # Variable for information (Screen and time)
        self.info_screen = pygame.display.Info()
        self.clock = pygame.time.Clock()

        # Variable for datas
        self.image_player = imagesPlayer
        self.power = powers
        self.weapons = weapons
        self.maps = maps

        # Variable for the status of the game
        self.running_game = True
        self.paused = False
        self.restart = False

        # Variable for the player
        self.heal_points_start = 100
        self.score_player1 = 0
        self.score_player2 = 0

        # Variable for array of entities in the game
        self.weapon_gun = []
        self.bullets = []
        self.floors = []
        self.players = []
        self.power_list = []

        # Variable of cooldown for dropping items
        self.cooldown_drop_weapon = 5
        self.cooldown_drop_power = 7

        # Variable for the last drop of the item
        self.last_drop_weapon = time.time()
        self.last_drop_power = time.time()

        # Variable of sounds
        self.sound_shot = pygame.mixer.Sound("./sounds/gun-shot.mp3")
        self.sound_falling = pygame.mixer.Sound("./sounds/falling-character.mp3")
        self.sound_background = pygame.mixer.Sound("./sounds/fighting-battle-warrior-drums.mp3")
        self.sounds = [self.sound_shot, self.sound_falling, self.sound_background]

        # Player for the background sound
        pygame.mixer.Channel(0).play(self.sound_background, -1)

        self.createInstanse()

    def createInstanse(self):
        """
        Create all entities for a game
        :return: All entities initiate
        """
        margin = self.info_screen.current_w / 10  # 10% d’espace sur les côtés

        self.player1 = Player(
            "Player 1",
            self.heal_points_start,
            margin,  # distance depuis la gauche
            self.info_screen.current_h / 2,
            self.image_player.get("player1_left"),
            self.window_game.screen,
            self.weapons[0],
            (252, 186, 3),
        )

        self.player2 = Player(
            "Player 2",
            self.heal_points_start,
            self.info_screen.current_w - margin - self.player1.rect.width,  # distance depuis la droite
            self.info_screen.current_h / 2,
            "images/imgCharacters/imgPlayer2/runPlayer2/stickman_go_right_player2.png",
            self.window_game.screen,
            self.weapons[0],
            (160, 7, 237),
        )

        self.players = [self.player1, self.player2]

        self.createFloors()

        self.last_drop_weapon = time.time()
        self.weapon_gun = []
        self.power_list = []
        self.bullets = []
        self.restart = False

    def launchGame(self):
        """
        Function to launch a game
        :return: The launched game
        """
        while self.running_game:
            self.playGame()

        pygame.mixer.Channel(0).stop()

    def changeImgPlayer(self):
        """
        Function for controlling the player image
        :return: The player image
        """
        if self.player1.weapon:
            if self.player1.direct_player == "Left":
                if self.player1.weapon.id == 1:
                    self.player1.img = pygame.image.load(
                        self.image_player.get("player1_left_gun")).convert_alpha()
                elif self.player1.weapon.id == 2:
                    self.player1.img = pygame.image.load(
                        self.image_player.get("player1_left_rifle")).convert_alpha()
                elif self.player1.weapon.id == 3:
                    self.player1.img = pygame.image.load(
                        self.image_player.get("player1_left_shotgun")).convert_alpha()
                elif self.player1.weapon.id == 4:
                    self.player1.img = pygame.image.load(
                        self.image_player.get("player1_left_sniper")).convert_alpha()
            elif self.player1.direct_player == "Right":
                if self.player1.weapon.id == 1:
                    self.player1.img = pygame.image.load(
                        self.image_player.get("player1_right_gun")).convert_alpha()
                elif self.player1.weapon.id == 2:
                    self.player1.img = pygame.image.load(
                        self.image_player.get("player1_right_rifle")).convert_alpha()
                elif self.player1.weapon.id == 3:
                    self.player1.img = pygame.image.load(
                        self.image_player.get("player1_right_shotgun")).convert_alpha()
                elif self.player1.weapon.id == 4:
                    self.player1.img = pygame.image.load(
                        self.image_player.get("player1_right_sniper")).convert_alpha()

        if self.player2.weapon:
            if self.player2.direct_player == "Left":
                if self.player2.weapon.id == 1:
                    self.player2.img = pygame.image.load(
                        self.image_player.get("player2_left_gun")).convert_alpha()
                elif self.player2.weapon.id == 2:
                    self.player2.img = pygame.image.load(
                        self.image_player.get("player2_left_rifle")).convert_alpha()
                elif self.player2.weapon.id == 3:
                    self.player2.img = pygame.image.load(
                        self.image_player.get("player2_left_shotgun")).convert_alpha()
                elif self.player2.weapon.id == 4:
                    self.player2.img = pygame.image.load(
                        self.image_player.get("player2_left_sniper")).convert_alpha()
            elif self.player2.direct_player == "Right":
                if self.player2.weapon.id == 1:
                    self.player2.img = pygame.image.load(
                        self.image_player.get("player2_right_gun")).convert_alpha()
                elif self.player2.weapon.id == 2:
                    self.player2.img = pygame.image.load(
                        self.image_player.get("player2_right_rifle")).convert_alpha()
                elif self.player2.weapon.id == 3:
                    self.player2.img = pygame.image.load(
                        self.image_player.get("player2_right_shotgun")).convert_alpha()
                elif self.player2.weapon.id == 4:
                    self.player2.img = pygame.image.load(
                        self.image_player.get("player2_right_sniper")).convert_alpha()

        self.playersDead()

    def playersDead(self):
        """
        Function for controlling if a player is dead
        :return: If a player is dead -> Victory screen
        """
        if self.player1.playerIsDead():
            self.score_player2 += 1
            self.player1.img = pygame.image.load(
                self.image_player.get("player1_dead")).convert_alpha()
            self.reloadPage()
            pygame.time.wait(2000)
        elif self.player2.playerIsDead():
            self.score_player1 += 1
            self.player2.img = pygame.image.load(
                self.image_player.get("player2_dead")).convert_alpha()
            self.reloadPage()
            pygame.time.wait(2000)

        if self.player1.playerIsDead() or self.player2.playerIsDead() or self.restart:
            self.createInstanse()
            self.paused = False

    def createWeapons(self):
        """
        Function for creating a random weapon in the battlefield
        :return: The weapon in the battlefield
        """
        random_nb = random.randint(1, 100)

        if random_nb <= 13:
            weapon = self.weapons[4]
            new_weapon = Weapons(weapon, self.window_game.screen)
            self.weapon_gun.append(new_weapon)

        elif random_nb <= 36:
            weapon = self.weapons[3]
            new_weapon = Weapons(weapon, self.window_game.screen)
            self.weapon_gun.append(new_weapon)

        elif random_nb <= 68:
            weapon = self.weapons[2]
            new_weapon = Weapons(weapon, self.window_game.screen)
            self.weapon_gun.append(new_weapon)

        elif random_nb <= 100:
            weapon = self.weapons[1]
            new_weapon = Weapons(weapon, self.window_game.screen)
            self.weapon_gun.append(new_weapon)

    def createPowers(self):
        """
        Function for creating a random power in the battlefield
        :return: The power in the battlefield
        """
        random_nb = random.randint(1, 100)

        if random_nb <= 50:
            power = self.power[0]
            new_power = Powers(power, self.window_game.screen)

            self.power_list.append(new_power)

        elif random_nb > 50:
            power = self.power[1]
            new_power = Powers(power, self.window_game.screen)

            self.power_list.append(new_power)

    def createFloors(self):
        """
        Function for creating a random battlefield
        :return: The battlefield random
        """
        current_maps = []
        for map in self.maps :
            current_map = []

            for floor in map:
                print(floor)
                current_floor = Map(self.window_game, floor)
                current_map.append(current_floor)

            current_maps.append(current_map)

        self.floors = random.choice(current_maps)

    def playGame(self):
        """
        Function for controlling all the game event
        :return: The gestion of the game
        """
        self.changeImgPlayer()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running_game = False
            if event.type != pygame.KEYDOWN:
                self.player2.modifImage(self.image_player.get("player2_stand"))
                self.player1.modifImage(self.image_player.get("player1_stand"))
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Gestion of the paused menu
                if self.paused:
                    if self.window_game.button_rect_restart.collidepoint(event.pos):
                        self.restart = True
                    elif self.window_game.button_rect_quit.collidepoint(event.pos):
                        self.window_game.closeRoot()
                        self.running_game = False
                        return

        # Gestion of the gameplay
        if not self.paused:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.paused = not self.paused
                pygame.time.wait(175)
            if not self.player1.playerIsDead():
                if keys[pygame.K_e]:
                    self.player1.checkAttack(self.sound_shot)
                if keys[pygame.K_q]:
                    if time.time() - self.player1.last_time_used_push > self.player1.cooldown_push:
                        self.player1.last_time_used_push = time.time()
                        self.player1.pushing = True
                if keys[pygame.K_a]:
                    self.player1.goLeft()
                    self.player1.modifImage(self.image_player.get("player1_left"))
                if keys[pygame.K_d]:
                    self.player1.goRight()
                    self.player1.modifImage(self.image_player.get("player1_right"))
                if keys[pygame.K_w]:
                    self.player1.jump(time.time())
                if keys[pygame.K_s]:
                    if self.player1.rect.bottom > self.floors[0].rect.top:
                        self.player1.modifImage(self.image_player.get("player1_crouch"))
                    else:
                        self.player1.modifImage(self.image_player.get("player1_crouch"))
                        self.player1.goDown(time.time())
            else:
                if self.player1.y != self.info_screen.current_h:
                    self.player1.y += 10

            if not self.player2.playerIsDead():

                if keys[pygame.K_o]:
                    self.player2.checkAttack(self.sound_shot)
                if keys[pygame.K_u]:
                    if time.time() - self.player2.last_time_used_push > self.player2.cooldown_push:
                        self.player2.last_time_used_push = time.time()
                        self.player2.pushing = True
                if keys[pygame.K_j]:
                    self.player2.goLeft()
                    self.player2.modifImage(self.image_player.get("player2_left"))
                if keys[pygame.K_l]:
                    self.player2.goRight()
                    self.player2.modifImage(self.image_player.get("player2_right"))
                if keys[pygame.K_k]:
                    if self.player2.rect.bottom > self.floors[0].rect.top:
                        self.player2.modifImage(self.image_player.get("player2_crouch"))
                    else:
                        self.player2.modifImage(self.image_player.get("player2_crouch"))
                        self.player2.goDown(time.time())
                if keys[pygame.K_i]:
                    self.player2.jump(time.time())
            else:
                if self.player2.y != self.info_screen.current_h:
                    self.player2.y += 10

            if time.time() - self.last_drop_weapon > self.cooldown_drop_weapon and (self.game_mod == 1 or self.game_mod == 3):
                self.last_drop_weapon = time.time()
                self.createWeapons()

            if time.time() - self.last_drop_power > self.cooldown_drop_power and self.game_mod == 1:
                self.last_drop_power = time.time()
                self.createPowers()

            for weapon in self.weapon_gun:
                if weapon.rect_weapon.y != self.info_screen.current_h:
                    weapon.rect_weapon.y += 10

            for power in self.power_list:
                if power.rect_power.y != self.info_screen.current_h:
                    power.rect_power.y += 10

            self.collision()

        else :

            # Gestion of the paused menu
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.paused = not self.paused
                pygame.time.wait(175)

        self.reloadPage()

        self.clock.tick(200)

    def reloadPage(self):
        """
        Function for reloading the page
        :return: The window and all the entities in the page
        """

        # Creating the window for the game
        if not self.paused:
            pygame.mouse.set_visible(False)
            self.window_game.changeBg('images/imgBackgrounds/gamePageBgs/gameBgs/test_blue_bg.jpg')

            for floor in self.floors:
                floor.draw(self.window_game.screen)

            for weapon in self.weapon_gun :
                weapon.draw(self.floors, self.player1, self.player2)

            for power in self.power_list :
                power.draw(self.floors, self.player1, self.player2)

            if self.player1.jumping > 0 :
                self.player1.y -= 20
                if self.player1.jumping <= 0 :
                    self.player1.jumping = 0
                else :
                    self.player1.jumping -= 20
            elif self.player1.jumping <= 0:
                if self.player1.y <= self.info_screen.current_h:
                    self.player1.y += 10

            if self.player2.jumping > 0:
                self.player2.y -= 20
                if self.player2.jumping <= 0:
                    self.player2.jumping = 0
                else:
                    self.player2.jumping -= 20
            elif self.player2.jumping <= 0:
                if self.player2.y <= self.info_screen.current_h:
                    self.player2.y += 10

            self.player1.draw()
            self.player2.draw()

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
        """
        Function for the gestion of collisions
        :return: The collision management
        """
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

            for power in self.power_list:
                if power.rect_power.colliderect(floor.rect):
                    power.rect_power.y -= 10

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

        for power in self.power_list:
            if power.rect_power.colliderect(self.player1.rect):
                self.player1.power = power
                self.power_list.remove(power)
                self.player1.takePower()

            elif power.rect_power.colliderect(self.player2.rect):
                self.player2.power = power
                self.power_list.remove(power)
                self.player2.takePower()

        if self.player1.pushing and self.player1.rect.colliderect(self.player2.rect):
            self.player1.pushing = False
            if self.player1.direct_player == "Left":
                self.player2.dashLeft()
            elif self.player1.direct_player == "Right":
                self.player2.dashRight()

        if self.player2.pushing and self.player2.rect.colliderect(self.player1.rect):
            self.player2.pushing = False
            if self.player2.direct_player == "Left":
                self.player1.dashLeft()
            elif self.player2.direct_player == "Right":
                self.player1.dashRight()

