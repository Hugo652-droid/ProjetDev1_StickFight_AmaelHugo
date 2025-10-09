"""
--
Auteur : Amael Rochat et Hugo Rod
Date de départ : 18.08.2025
Date de fin : 10.10.2025
Projet : Projet Dev 1 (sticKOnion)
--
Nom fichier : Player.py
Description fichier : Creation et gestion des personnages jouable
--
"""
import random
import time

import pygame
from Bullet import Bullet
from Weapons import Weapon
from Data.powers import powers

INFO_SCREEN = pygame.display.Info()


class Player:
    def __init__(self, name, hp, x, y, image, screen, hand, color):
        """
        The playable charter
        :param name: Name of the player
        :param hp: Health points of the player
        :param x: X position of the player
        :param y: Y position of the player
        :param image: Image of the player
        :param screen: The game window
        :param hand: Data of the weapon : hand
        :param color: The color of the player
        """
        self.screen = screen
        self.name = name
        self.hp = hp
        self.hp_before = 0
        self.x = x
        self.y = y
        self.color = color

        # Creation of the image and rectangle
        self.img = pygame.image.load(image).convert_alpha()
        self.img = pygame.transform.scale(self.img, (200, 100))
        self.rect = self.img.get_rect()

        # All time of usage of an attack or other
        self.last_time_used_vertical = 0
        self.last_time_used_attack = 0
        self.last_time_used_push = 0
        self.last_time_used_power = time.time()

        # All the cooldown for movement and attack
        self.cooldown_vertical = 1
        self.cooldown_attack = 1
        self.cooldown_push = 1
        self.cooldown_power = 0

        # The player's state
        self.attacking = False
        self.pushing = False
        self.invincible = False
        self.player_is_stand = True
        self.jumping = 0
        self.direct_player = "Left"

        # The equipment of the player
        self.hands = Weapon(hand, screen)
        self.weapon = self.hands
        self.damage = self.weapon.damage
        self.power = None

    def draw(self):
        """
        Display the player in the window
        :return: The player displayed
        """
        if self.player_is_stand:
            self.img = pygame.transform.scale(self.img, (80, 100))
        else:
            self.img = pygame.transform.scale(self.img, (150, 100))

        self.rect = self.img.get_rect()
        self.rect.center = (self.x, self.y)
        self.rect = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)
        self.screen.blit(self.img, self.rect)

        self.usePower()

    def modifImage(self, image):
        """
        Modify the image of the player
        :param image: The new image
        :return: The player with the modified image
        """
        self.img = pygame.image.load(image).convert_alpha()

    def jump(self, current_time):
        """
        Function for manage the jump
        :param current_time: The current time
        :return: The player jumping
        """
        if current_time - self.last_time_used_vertical > self.cooldown_vertical:
            self.jumping = INFO_SCREEN.current_h/4 + 100
            self.last_time_used_vertical = current_time

    def goLeft(self):
        """
        Function for go left of the player
        :return: The player going left
        """
        self.x -= 10
        self.direct_player = "Left"

    def goRight(self):
        """
        Function for go right of the player
        :return: The player going right
        """
        self.x += 10
        self.direct_player = "Right"

    def goDown(self, current_time):
        """
        Function for manage the falling of the player
        :param current_time: The current time
        :return: The player falling
        """
        if current_time - self.last_time_used_vertical > self.cooldown_vertical:
            self.y += 150
            self.last_time_used_vertical = current_time

    def dashLeft(self):
        """
        Function for the player dashing to the left
        :return: The player dashing to the left
        """
        self.x -= 150
        self.direct_player = "Left"

    def dashRight(self):
        """
        Function for the player dashing to the right
        :return: The player dashing to the right
        """
        self.x += 150
        self.direct_player = "Right"

    def tackDamage(self, damage):
        """
        Function for manage the player tacking damage
        :param damage: The damage to take
        :return: The hp reduce by the damage
        """
        if not self.invincible:
            self.hp -= damage

    def playerIsDead(self):
        """
        Check if the player is dead
        :return: The player is dead
        """
        return self.hp <= 0

    def takePower(self):
        """
        Function for manage the take of a power
        :return: The player with a power
        """
        random_nb = random.randint(1, 100)

        if random_nb <= 50:
            self.power = powers[0]
            self.cooldown_power = self.power['duration']
        elif random_nb > 50:
            self.power = powers[1]
            self.cooldown_power = self.power['duration']

    def usePower(self):
        """
        Function for manage the use of a power
        :return: The using power
        """
        if self.power:
            if self.power.get("id") == 1:
                if time.time() - self.last_time_used_power < self.cooldown_power:
                    self.cooldown_vertical = 0
                    self.last_time_used_power = time.time()

                if time.time() - self.last_time_used_power > self.cooldown_power:
                    self.cooldown_vertical = 1

            elif self.power.get("id") == 2:
                if time.time() - self.last_time_used_power > self.cooldown_power:
                    self.invincible = True
                    self.last_time_used_power = time.time()

                if time.time() - self.last_time_used_power > self.cooldown_power:
                    self.invincible = False

            elif self.power.get("id") == 3:
                if time.time() - self.last_time_used_power < self.cooldown_power:
                    print(self.power.get("name"))

    def simpleAttack(self, player_damaged):
        """
        Function for manage the shoot of the player and the punch with is damaged
        :param player_damaged: the player damaged
        :return: The bullet but if it's not a gun : false
        """
        if self.weapon.id == 0:
            self.cooldown_attack = 1
            if self.rect.colliderect(player_damaged.rect):
                player_damaged.tackDamage(self.damage)
                return False
            return False
        else:
            if not self.weapon.noAmmunition():
                self.damage = self.weapon.damage
                self.cooldown_attack = self.weapon.attackSpeed
                self.weapon.useAmmunition()
                bullet = Bullet(self.rect.center, self.direct_player, self.name, self.weapon.width, self.weapon.height)
                return bullet
            return False

    def checkAttack(self, sound_shot):
        """
        Function for manage the attack
        :param sound_shot: The sound of the shoot
        :return: The player attacking
        """
        if time.time() - self.last_time_used_attack > self.cooldown_attack and self.weapon.id == 0:
            self.last_time_used_attack = time.time()
            if self.direct_player == "Left":
                self.dashLeft()
            elif self.direct_player == "Right":
                self.dashRight()
            self.attacking = True

        elif time.time() - self.last_time_used_attack > self.cooldown_attack:
            pygame.mixer.Channel(1).stop()
            pygame.mixer.Channel(1).play(sound_shot)
            self.noAmmunitionInWeapon()
            self.last_time_used_attack = time.time()
            self.attacking = True

        else:
            self.attacking = False

    def noAmmunitionInWeapon(self):
        """
        Function for manage the no more ammunition
        :return: The player with is hands
        """
        if self.weapon.noAmmunition():
            self.weapon = self.hands
            self.cooldown_attack = 1
