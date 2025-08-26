import pygame

class Weapons():
    def __init__(self):
        self.cooldown = 1
        self.lastused = 0

    def simple_attack(self, player_attack, player_damaged, current_time):
         if current_time - self.lastused > self.cooldown:
            self.lastused = current_time
            if player_attack.direct_player == "Left":
                player_attack.x -= 100
                if player_attack.rect.colliderect(player_damaged.rect):
                    player_damaged.hp -= 50

            elif player_attack.direct_player == "Right":
                player_attack.x += 100
                if player_attack.rect.colliderect(player_damaged.rect):
                    player_damaged.hp -= 50










