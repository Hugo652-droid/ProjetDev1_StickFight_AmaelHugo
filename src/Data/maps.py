"""
--
Auteur : Amael Rochat et Hugo Rod
Date de départ : 18.08.2025
Date de fin : 10.10.2025
Projet : Projet Dev 1 (sticKOnion)
--
Nom fichier : maps.py
Description fichier : Gestion des maps et leurs platformes
--
"""

import pygame

info_screen = pygame.display.Info()

maps = [
        [
            {
                'name': 'floor',
                'x': info_screen.current_w / 2,
                'y': info_screen.current_h - 100,
                'with': info_screen.current_w - 200,
                'height': info_screen.current_h / 5,
                'image': 'images/imgGames/imgFloors/ground1_dirt.png'
            },
            {
                'name': 'platform_centre',
                'x': info_screen.current_w / 2,
                'y': info_screen.current_h - info_screen.current_h / 3,
                'with': info_screen.current_w - info_screen.current_w / 2,
                'height': info_screen.current_h / 20,
                'image': ""
            },
            {
                'name': 'platform_top_left',
                'x': info_screen.current_w / 4,
                'y': info_screen.current_h / 2.5,
                'with': info_screen.current_w - info_screen.current_w / 1.7,
                'height': info_screen.current_h / 20,
                'image': ""
            },
            {
                'name': 'platform_top_right',
                'x': info_screen.current_w - info_screen.current_w / 4,
                'y': info_screen.current_h / 2.5,
                'with': info_screen.current_w - info_screen.current_w / 1.7,
                'height': info_screen.current_h / 20,
                'image': ""
            }
        ],
        [
            {
                'name': 'floor',
                'x': info_screen.current_w / 2,
                'y': info_screen.current_h - 100,
                'with': info_screen.current_w - 200,
                'height': info_screen.current_h / 5,
                'image': 'images/imgGames/imgFloors/ground1_dirt.png'
            },
            {
                'name': 'platform_mid_left',
                'x': info_screen.current_w / 3,
                'y': info_screen.current_h / 1.8,
                'with': info_screen.current_w / 6,
                'height': info_screen.current_h / 25,
                'image': ""
            },
            {
                'name': 'platform_mid_right',
                'x': info_screen.current_w - info_screen.current_w / 3,
                'y': info_screen.current_h / 1.8,
                'with': info_screen.current_w / 6,
                'height': info_screen.current_h / 25,
                'image': ""
            },
            {
                'name': 'platform_top_centre',
                'x': info_screen.current_w / 2,
                'y': info_screen.current_h / 3,
                'with': info_screen.current_w / 8,
                'height': info_screen.current_h / 30,
                'image': ""
            },
            {
                'name': 'platform_top_left',
                'x': info_screen.current_w / 6,
                'y': info_screen.current_h / 4,
                'with': info_screen.current_w / 10,
                'height': info_screen.current_h / 30,
                'image': ""
            },
            {
                'name': 'platform_top_right',
                'x': info_screen.current_w - info_screen.current_w / 6,
                'y': info_screen.current_h / 4,
                'with': info_screen.current_w / 10,
                'height': info_screen.current_h / 30,
                'image': ""
            }
        ],
        [
            {
                'name': 'floor',
                'x': info_screen.current_w / 2,
                'y': info_screen.current_h - 100,
                'with': info_screen.current_w - 200,
                'height': info_screen.current_h / 5,
                'image': 'images/imgGames/imgFloors/ground1_dirt.png'
            },
            {
                'name': 'platform_left',
                'x': info_screen.current_w / 4,
                'y': info_screen.current_h - info_screen.current_h / 2.5,
                'with': info_screen.current_w / 4,
                'height': info_screen.current_h / 20,
                'image': ""
            },
            {
                'name': 'platform_centre',
                'x': info_screen.current_w / 2,
                'y': info_screen.current_h - info_screen.current_h / 3,
                'with': info_screen.current_w / 4,
                'height': info_screen.current_h / 20,
                'image': ""
            },
            {
                'name': 'platform_top_right',
                'x': info_screen.current_w - info_screen.current_w / 4,
                'y': info_screen.current_h - info_screen.current_h / 2.5,
                'with': info_screen.current_w / 4,
                'height': info_screen.current_h / 20,
                'image': ""
            }
        ],
        [
            {
                'name': 'platform_left',
                'x': info_screen.current_w / 5,
                'y': info_screen.current_h / 3,
                'with': info_screen.current_w / 5,
                'height': info_screen.current_h / 25,
                'image': ""
            },
            {
                'name': 'platform_centre',
                'x': info_screen.current_w / 2,
                'y': info_screen.current_h / 2,
                'with': info_screen.current_w / 3,
                'height': info_screen.current_h / 20,
                'image': ""
            },
            {
                'name': 'platform_top_right',
                'x': info_screen.current_w - info_screen.current_w / 5,
                'y': info_screen.current_h / 3,
                'with': info_screen.current_w / 5,
                'height': info_screen.current_h / 25,
                'image': ""
            }
        ],
]
