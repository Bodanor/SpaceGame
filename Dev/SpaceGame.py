import pygame
import json
import os
import Affichage
import Sound
import Entite
import Etoiles
import Gameplay
import Menu

#Initialisation des images, sons et variables
print("Initialisation...")
pygame.mixer.init()
pygame.init()
SpaceWindow = Affichage.SpaceWindow('Space Game')
SpaceSound = Sound.SpaceSound()
SpaceGamePlay = Gameplay.SpaceGamePlay()
SpaceMenu = Menu.SpaceMenu(SpaceWindow.fenetre, SpaceWindow.FENETRE_HAUTEUR, SpaceWindow.FENETRE_LARGEUR)



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
temps = pygame.time.Clock()

#Faire jouer la bande son des le début du jeu
SpaceSound.sounds['musique'].play()

#Creation des etoiles pour le jeu
SpaceStars = Etoiles.Etoiles(SpaceWindow.FENETRE_LARGEUR, SpaceWindow.FENETRE_HAUTEUR)
SpaceStars.cree_etoiles()
etoiles = SpaceStars.ETOILES

while ENINTRO:

    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ENINTRO = False

            if event.type == pygame.KEYDOWN:

                # Changement du bouton dans le menu

                if event.key == pygame.K_DOWN:
                    if SpaceSound.SON_EN_PAUSE == False:
                        SpaceSound.sounds['choix'].play()

                    if SpaceMenu.BOUTON < 2:
                        SpaceMenu.BOUTON += 1
                    else:
                        SpaceMenu.BOUTON = 0

                if event.key == pygame.K_UP:
                    if SpaceSound.SON_EN_PAUSE == False:
                        SpaceSound.sounds['choix'].play()

                    if SpaceMenu.BOUTON < 1:
                        SpaceMenu.BOUTON = 2
                    else:
                        SpaceMenu.BOUTON -= 1

                # Changement de niveau dans le deuxieme bouton du menu

                if event.key == pygame.K_RIGHT:
                    if SpaceMenu.BOUTON == 1:
                        if SpaceGamePlay.niveau_difficulte < 2:
                            if SpaceSound.SON_EN_PAUSE == False:
                                SpaceSound.sounds['choix_gauche_droite'].play()

                            SpaceGamePlay.niveau_difficulte += 1
                            SpaceGamePlay.changer_difficulte(SpaceMenu)

                if event.key == pygame.K_LEFT:
                    if SpaceMenu.BOUTON == 1:
                        if SpaceGamePlay.niveau_difficulte > 0:
                            if SpaceSound.SON_EN_PAUSE == False:
                                SpaceSound.sounds['choix_droite_gauche'].play()

                            SpaceGamePlay.niveau_difficulte -= 1
                            SpaceGamePlay.changer_difficulte(SpaceMenu)

                #Confirmation du bouton avec la touche Enter

                if event.key == pygame.K_RETURN:
                    if SpaceMenu.BOUTON == 2:
                        ENINTRO = False


                #Apuyer sur la touche 'm' pour mute le jeu
                if event.key == pygame.K_m :
                    if SpaceSound.SON_EN_PAUSE == False:
                        SpaceSound.sounds['musique'].stop()
                        SpaceSound.SON_EN_PAUSE = True
                    else:
                        SpaceSound.sounds['musique'].play()
                        SpaceSound.SON_EN_PAUSE = False

            #Creation d'evenements similaires au touche du clavier mais pour manette

            #FIN





    except Exception as e:
        pass

    SpaceWindow.fenetre.fill(SpaceWindow.ESPACE)
    SpaceWindow.afficher(vaisseau)
    SpaceWindow.afficher_etoiles(etoiles, SpaceGamePlay.VITESSE_ETOILE)
    SpaceWindow.affichervie(SpaceGamePlay.NOMBRE_VIE)
    SpaceWindow.afficher_munition(SpaceGamePlay.MUNITIONS)
    SpaceMenu.afficherBoutonMenu()
    pygame.display.flip()
    temps.tick(60)

