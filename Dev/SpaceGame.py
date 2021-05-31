import pygame
import Affichage
import Sound
import Entite
import etoiles
import json
import os
import Gameplay

#Initialisation des images, sons et variables
print("Initialisation...")
pygame.mixer.init()
pygame.init()
SpaceWindow = Affichage.SpaceWindow('Space Game')
SpaceSound = Sound.SpaceSound()
SpaceGamePlay = Gameplay.SpaceGamePlay()


#initialisation de la manette ps4
joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))

for joystick in joysticks:
    joystick.init()

with open(os.path.join("controller.json"), 'r+') as file:
    button_keys = json.load(file)

analog_keys = {0:0, 1:0, 2:0, 3:0, 4:-1, 5:-1}


#Creation d'une entite pour le vaisseau et chargement d'une image pour celle-ci
vaisseau = Entite.Entite()
vaisseau.prendsPose(SpaceWindow.images['vaisseau_jaune_avec_flamme'])
vaisseau.place((SpaceWindow.FENETRE_LARGEUR / 2) - SpaceWindow.VAISSEAU_LARGEUR / 2, SpaceWindow.FENETRE_HAUTEUR - SpaceWindow.VAISSEAU_HAUTEUR, 0)

#Variables pour la boucle pricipal du jeu
ENINTRO = True
SON_EN_PAUSE = False
temps = pygame.time.Clock()

#Faire jouer la bande son des le début du jeu
SpaceSound.sounds['musique'].play()

#Creation des etoiles pour le jeu
SpaceStars = etoiles.Etoiles(SpaceWindow.FENETRE_LARGEUR, SpaceWindow.FENETRE_HAUTEUR)
SpaceStars.cree_etoiles()
etoiles = SpaceStars.ETOILES

while ENINTRO:

    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ENINTRO = False

            if event.type == pygame.KEYDOWN :
                print("testing")
                #Apuyer sur la touche 'm' pour mute le jeu
                if event.key == pygame.K_m :
                    if SON_EN_PAUSE == False:
                        SpaceSound.sounds['musique'].stop()
                        SON_EN_PAUSE = True
                    else:
                        SpaceSound.sounds['musique'].play()
                        SON_EN_PAUSE = False


    except Exception as e:
        pass

    SpaceWindow.fenetre.fill(SpaceWindow.ESPACE)
    SpaceWindow.afficher(vaisseau)
    SpaceWindow.afficher_etoiles(etoiles, SpaceGamePlay.VITESSE_ETOILE)
    SpaceWindow.affichervie(SpaceGamePlay.NOMBRE_VIE)

    pygame.display.flip()
    temps.tick(60)

