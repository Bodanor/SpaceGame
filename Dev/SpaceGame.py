import pygame
import json
import os
import Affichage
import Sound
import Entite
import Etoiles
import Gameplay
import Menu
import Missiles

# Initialisation des images, sons et variables
print("Initialisation...")
pygame.mixer.init()
pygame.init()
SpaceWindow = Affichage.SpaceWindow('Space Game')
SpaceSound = Sound.SpaceSound()
SpaceGamePlay = Gameplay.SpaceGamePlay()
SpaceMenu = Menu.SpaceMenu(SpaceWindow.fenetre, SpaceWindow.FENETRE_HAUTEUR, SpaceWindow.FENETRE_LARGEUR)


# Creation d'une entite pour le vaisseau et chargement d'une image pour celle-ci
vaisseau = Entite.Entite()
vaisseau.prendsPose(SpaceWindow.images['vaisseau_jaune_sans_flamme'])
vaisseau.place((SpaceWindow.FENETRE_LARGEUR / 2) - SpaceWindow.VAISSEAU_LARGEUR / 2,
               SpaceWindow.FENETRE_HAUTEUR - SpaceWindow.VAISSEAU_HAUTEUR, 0)

# Variables pour la boucle pricipal du jeu
ENINTRO = True
ENJEU = False
temps = pygame.time.Clock()

# Faire jouer la bande son des le début du jeu
SpaceSound.sounds['musique'].play()

# Creation des etoiles pour le jeu
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
                    if not SpaceSound.SON_EN_PAUSE:
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

                # Confirmation du bouton avec la touche Enter

                if event.key == pygame.K_RETURN:
                    if SpaceMenu.BOUTON == 0 or SpaceMenu.BOUTON == 1:
                        ENINTRO = False
                        ENJEU = True

                    if SpaceMenu.BOUTON == 2:
                        ENINTRO = False
                        ENJEU = False

                # Apuyer sur la touche 'm' pour mute le jeu
                if event.key == pygame.K_m:
                    if SpaceSound.SON_EN_PAUSE == False:
                        SpaceSound.sounds['musique'].stop()
                        SpaceSound.SON_EN_PAUSE = True
                    else:
                        SpaceSound.sounds['musique'].play()
                        SpaceSound.SON_EN_PAUSE = False

            # Creation d'evenements similaires au touche du clavier mais pour manette

            # FIN

    except Exception as e:
        pass

    SpaceWindow.fenetre.fill(SpaceWindow.ESPACE)
    SpaceWindow.affichervie(SpaceGamePlay.NOMBRE_VIE)
    SpaceWindow.afficher_etoiles(etoiles, SpaceGamePlay.VITESSE_ETOILE)
    SpaceWindow.afficher_munition(SpaceGamePlay.MUNITIONS)
    SpaceWindow.dessine_missile(SpaceGamePlay)
    SpaceWindow.afficher(vaisseau)
    SpaceMenu.afficherBoutonMenu()

    if SpaceGamePlay.COMPTEUR_BOUCLE % 60 == 0 and SpaceGamePlay.COMPTEUR_BOUCLE < 3600:
        SpaceGamePlay.VITESSE_JEU += 0.10

    if SpaceGamePlay.COMPTEUR_BOUCLE % 150 == 0:
        if SpaceGamePlay.MUNITIONS > 0:
            missile = Missiles.Missile(SpaceGamePlay)
            missile.placeMissile(vaisseau.position[0] + SpaceWindow.VAISSEAU_LARGEUR / 2, vaisseau.position[1])
            SpaceGamePlay.missiles.append(missile)

    pygame.display.flip()
    temps.tick(60)
    SpaceGamePlay.COMPTEUR_BOUCLE += 1

    while ENJEU == True:

        vaisseau.prendsPose(SpaceWindow.images['vaisseau_jaune_sans_flamme'])


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ENJEU = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    if SpaceGamePlay.MUNITIONS == 0:
                        if SpaceSound.SON_EN_PAUSE == False:
                            SpaceSound.sounds['no_bullets'].play()

                    elif SpaceGamePlay.MUNITIONS > 0:
                        if SpaceSound.SON_EN_PAUSE == False:
                            SpaceSound.sounds['piou'].play()
                        missile = Missiles.Missile(SpaceGamePlay)
                        missile.placeMissile(vaisseau.position[0] + SpaceWindow.VAISSEAU_LARGEUR / 2,
                                             vaisseau.position[1])
                        SpaceGamePlay.missiles.append(missile)
                        SpaceGamePlay.MUNITIONS -= 1

                if event.key == pygame.K_m:
                    if SpaceSound.SON_EN_PAUSE == False:
                        SpaceSound.sounds['musique'].stop()
                        SpaceSound.SON_EN_PAUSE = True
                    else:
                        SpaceSound.sounds['musique'].play()
                        SpaceSound.SON_EN_PAUSE = False


        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            if vaisseau.position[0] + SpaceWindow.VAISSEAU_LARGEUR < SpaceWindow.FENETRE_LARGEUR:
                vaisseau.prendsPose(SpaceWindow.images['vaisseau_jaune_sans_flamme'])
                vaisseau.place(vaisseau.position[0] + SpaceGamePlay.DEPLACEMENT_VAISSEAU, vaisseau.position[1], 0)

        if keys[pygame.K_LEFT]:
            if vaisseau.position[0] <= 0:
                vaisseau.prendsPose(SpaceWindow.images['vaisseau_jaune_sans_flamme'])
            else:
                vaisseau.prendsPose(SpaceWindow.images['vaisseau_jaune_sans_flamme'])
                vaisseau.place(vaisseau.position[0]- SpaceGamePlay.DEPLACEMENT_VAISSEAU, vaisseau.position[1], 0)

        # BAS
        if keys[pygame.K_DOWN]:
            if vaisseau.position[1] < SpaceWindow.FENETRE_HAUTEUR - SpaceWindow.VAISSEAU_HAUTEUR:
                vaisseau.prendsPose(SpaceWindow.images['vaisseau_jaune_sans_flamme'])
                vaisseau.place(vaisseau.position[0], vaisseau.position[1]+ SpaceGamePlay.DEPLACEMENT_VAISSEAU, 0)
        # HAUT
        if keys[pygame.K_UP]:
            if vaisseau.position[1] > 0:
                vaisseau.prendsPose(SpaceWindow.images['vaisseau_jaune_avec_flamme'])
                vaisseau.place(vaisseau.position[0], vaisseau.position[1] - SpaceGamePlay.DEPLACEMENT_VAISSEAU, 0)




        SpaceWindow.fenetre.fill(SpaceWindow.ESPACE)
        SpaceWindow.affichervie(SpaceGamePlay.NOMBRE_VIE)
        SpaceWindow.afficher_etoiles(etoiles, SpaceGamePlay.VITESSE_ETOILE)
        SpaceWindow.afficher_munition(SpaceGamePlay.MUNITIONS)
        SpaceWindow.dessine_missile(SpaceGamePlay)
        SpaceWindow.afficher(vaisseau)

        temps.tick(60)
        pygame.display.flip()
