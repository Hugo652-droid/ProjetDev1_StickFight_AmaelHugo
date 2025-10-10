# ProjetDev1_StickFight_AmaelHugo

## Groupe Dev
Amael Rochat et Hugo Rod

## Projet
Notre projet consiste à recréer le jeu [StickFight](https://store.steampowered.com/app/674940/Stick_Fight_The_Game/) grace a pygame.
Nom du projet : ***sticKOnion***

## Techno
Python et pygame

## Architecture du projet

```
ProjetDev1_StickFight_AmaelHugo 
│   .gitignore                           
│   README.md 
│   
├───Conception
│       StickFight.mmap                               // Mindmap de la conception dans mindmanager
│       StickFight.png                                // Mindmap de la conception
│       UML_class.drawio                              // Diagram UML des classe sur draw.io
│       UML_class.drawio.png                          // Diagram UML des classe
│       UML_class_final.drawio                        // Diagram UML des classe à la fin du projet sur draw.io
│       UML_class_final.png                           // Diagram UML des classe à la fin du projet
│       UML_flux.drawio                               // Diagram UML de flux sur draw.io
│       UML_flux.png                                  // Diagram UML de flux
│
└───src     
    │      Bullet.py                                  // Creation et gestion des balles
    │      Credits.py                                 // Creation et gestion de l'affichage de la page des credits
    │      Game.py                                    // Creation et gestion des parties et du jeu
    │      Home.py                                    // Creation et gestion de l'affichage de la page d'accueil
    │      Main.py                                    // Lancement de l'application et affichage de la page d'accueil
    │      Map.py                                     // Creation et gestion des platforms physique
    │      Player.py                                  // Creation et gestion des personnages jouable
    │      Power.py                                   // Creation et gestion des pouvoirs
    │      Root.py                                    // Creation et gestion des fenêtres de l'application
    │      Settings.py                                // Creation et gestion de la fenêtre d'option
    │      Weapons.py                                 // Creation et gestion des armes         
    │              
    ├───assets
    │      Button.py                                  // Creation et gestion des buttons
    │      Shooting Star.ttf                          // Style de text
    │              
    ├───Data
    │      imagePlayer.py                             // Toutes les images pour les joueur
    │      maps.py                                    // Toutes les données pour la création des platforms physique
    │      powers.py                                  // Toutes les données pour la création des pouvrois
    │      imagePlayer.py                             // Toutes les données pour la création des armes
    │              
    ├───images                                        // Toutes les images pour le jeu
    │              
    └───sounds
           falling-character.mp3                      // Son de chute dans le vide
           fighting-battle-warrior-drums.mp3          // La musique de fond du jeu
           gun-shot.mp3                               // La musique de fond du jeu    
```

### Son
https://pixabay.com/sound-effects
