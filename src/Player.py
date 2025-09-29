"""
--
Auteur : Amael Rochat et Hugo Rod
Date de départ : 18.08.2025
Date de fin : --.--.----
Projet : Projet Dev 1 (sticKOnion)
--
Nom fichier : Player.py
Description fichier : Creation et gestion des personnages jouable
--
"""
import random
import time

import pygame
from src.Bullet import Bullet
from src.Weapons import Weapons
from src.Data.powers import powers

class Player:
    def __init__(self, name, hp, x, y, image, screen, hands, color):
        self.name = name
        self.hp = hp
        self.x = x
        self.y = y
        self.info_screen = pygame.display.Info()
        self.img = pygame.image.load(image).convert_alpha()
        self.img = pygame.transform.scale(self.img, (200, 100))
        self.rect = self.img.get_rect()
        self.last_time_used_vertical = 0
        self.last_time_used_attack = 0
        self.last_time_used_push = 0
        self.cooldown_vertical = 1
        self.cooldown_attack = 1
        self.cooldown_push = 1
        self.direct_player = "Left"
        self.jumping = 0
        self.color = color
        self.attacking = False
        self.pushing = False
        self.hands =  Weapons(hands, screen)
        self.weapon = self.hands
        self.damage = 10
        self.screen = screen
        self.power = None
        self.last_time_used_power = time.time()
        self.cooldown_power = 0
        self.hp_before = 0

    def draw(self):
        self.img = pygame.transform.scale(self.img, (150, 100))
        self.rect = self.img.get_rect()
        self.rect.center = (self.x, self.y)
        self.rect = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)
        self.screen.blit(self.img, self.rect)
        self.usePower()

    def modifImage(self, image):
        self.img = pygame.image.load(image).convert_alpha()

    def jump(self, current_time):
        if current_time - self.last_time_used_vertical > self.cooldown_vertical:
            self.jumping = self.info_screen.current_h/4 + 100
            self.last_time_used_vertical = current_time

    def goLeft(self):
        self.x -= 10
        self.direct_player = "Left"

    def goRight(self):
        self.x += 10
        self.direct_player = "Right"

    def goDown(self, current_time):
        if current_time - self.last_time_used_vertical > self.cooldown_vertical:
            self.y += 150
            self.last_time_used_vertical = current_time

    def dashLeft(self):
        self.x -= 150
        self.direct_player = "Left"

    def dashRight(self):
        self.x += 150
        self.direct_player = "Right"

    def tackDammage(self, damage):
        self.hp -= damage

    def playerIsDead(self):
        return self.hp <= 0

    def takePower(self):
        random_nb = random.randint(1, 100)

        if random_nb <= 33:
            self.power = powers[0]
            self.cooldown_power = self.power['duration']

        elif random_nb <= 66:
            self.power = powers[1]
            self.cooldown_power = self.power['duration']

        elif random_nb > 66:
            self.power = powers[2]
            self.cooldown_power = self.power['duration']

    def usePower(self):
        if self.power:
            if self.power.get("id") == 1:
                if time.time() - self.last_time_used_power < self.cooldown_power:
                    self.cooldown_vertical = 0
                    print(self.power.get("name"))
                    self.last_time_used_power = time.time()

                if time.time() - self.last_time_used_power > self.cooldown_power:
                    self.cooldown_vertical = 1

            elif self.power.get("id") == 2:
                if time.time() - self.last_time_used_power < self.cooldown_power:
                    print(self.power.get("name"))
                    if self.hp <= 100:
                        self.hp_before = self.hp
                    self.hp = 1000
                    self.last_time_used_power = time.time()

                if time.time() - self.last_time_used_power > self.cooldown_power:
                    self.hp = self.hp_before

            elif self.power.get("id") == 3:
                if time.time() - self.last_time_used_power < self.cooldown_power:
                    print(self.power.get("name"))

    def simpleAttack(self, player_damaged):
        if self.weapon.id == 0:
            self.cooldown_attack = 1
            if self.rect.colliderect(player_damaged.rect):
                player_damaged.tackDammage(self.damage)
                return False
            return False
        else :
            if not self.weapon.noAmmunition():
                self.damage = self.weapon.dammage
                self.cooldown_attack = self.weapon.attackSpeed
                self.weapon.useAmmunition()
                bullet = Bullet(self.rect.center, self.direct_player, self.name, self.weapon.width, self.weapon.height)
                return bullet
            return False

    def checkAttack(self, sound_shot):
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
        if self.weapon.noAmmunition():
            self.weapon = self.hands
            self.cooldown_attack = 1