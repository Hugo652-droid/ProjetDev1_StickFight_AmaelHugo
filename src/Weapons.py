import pygame

class Weapons():
    def __init__(self):
        pass

    def simple_attack(self, player_attack, player_damaged):
         if player_attack.direct_player == "Left":
             player_attack.x -= 30
             if player_attack.rect.colliderect(player_damaged.rect):
                 player_damaged.hp -= 10

         elif player_attack.direct_player == "Right":
             player_attack.x += 30
             if player_attack.rect.colliderect(player_damaged.rect):
                 player_damaged.hp -= 10










