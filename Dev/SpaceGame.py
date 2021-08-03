import pygame
from Dev.Source import Etoiles, Gameplay, Entite, Missiles

# Initialisation des images, sons et variables
print("Initialisation...")
pygame.mixer.init()
pygame.init()
SpaceGamePlay = Gameplay.SpaceGamePlay()


# Creation d'une entite pour le vaisseau et chargement d'une image pour celle-ci
vaisseau = Entite.Entite()
vaisseau.prendsPose(SpaceGamePlay.SpaceWindow.images['vaisseau_jaune_sans_flamme'])
vaisseau.place((SpaceGamePlay.SpaceWindow.FENETRE_LARGEUR / 2) - SpaceGamePlay.SpaceWindow.VAISSEAU_LARGEUR / 2,
               SpaceGamePlay.SpaceWindow.FENETRE_HAUTEUR - SpaceGamePlay.SpaceWindow.VAISSEAU_HAUTEUR, 0)

# Variables pour la boucle principal du jeu
ENINTRO = True
ENJEU = False
temps = pygame.time.Clock()

# Faire jouer la bande son des le début du jeu
SpaceGamePlay.SpaceSound.sounds['musique'].play()

# Creation des etoiles pour le jeu
SpaceStars = Etoiles.Etoiles(SpaceGamePlay.SpaceWindow.FENETRE_LARGEUR, SpaceGamePlay.SpaceWindow.FENETRE_HAUTEUR)
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
                    if not SpaceGamePlay.SpaceSound.SON_EN_PAUSE:
                        SpaceGamePlay.SpaceSound.sounds['choix'].play()

                    if SpaceGamePlay.SpaceMenu.BOUTON < 2:
                        SpaceGamePlay.SpaceMenu.BOUTON += 1
                    else:
                        SpaceGamePlay.SpaceMenu.BOUTON = 0

                if event.key == pygame.K_UP:
                    if SpaceGamePlay.SpaceSound.SON_EN_PAUSE == False:
                        SpaceGamePlay.SpaceSound.sounds['choix'].play()

                    if SpaceGamePlay.SpaceMenu.BOUTON < 1:
                        SpaceGamePlay.SpaceMenu.BOUTON = 2
                    else:
                        SpaceGamePlay.SpaceMenu.BOUTON -= 1

                # Changement de niveau dans le deuxieme bouton du menu

                if event.key == pygame.K_RIGHT:
                    if SpaceGamePlay.SpaceMenu.BOUTON == 1:
                        if SpaceGamePlay.niveau_difficulte < 2:
                            if SpaceGamePlay.SpaceSound.SON_EN_PAUSE == False:
                                SpaceGamePlay.SpaceSound.sounds['choix_gauche_droite'].play()

                            SpaceGamePlay.niveau_difficulte += 1
                            SpaceGamePlay.changer_difficulte(SpaceGamePlay.SpaceMenu)

                if event.key == pygame.K_LEFT:
                    if SpaceGamePlay.SpaceMenu.BOUTON == 1:
                        if SpaceGamePlay.niveau_difficulte > 0:
                            if SpaceGamePlay.SpaceSound.SON_EN_PAUSE == False:
                                SpaceGamePlay.SpaceSound.sounds['choix_droite_gauche'].play()

                            SpaceGamePlay.niveau_difficulte -= 1
                            SpaceGamePlay.changer_difficulte(SpaceGamePlay.SpaceMenu)

                # Confirmation du bouton avec la touche Enter

                if event.key == pygame.K_RETURN:
                    if SpaceGamePlay.SpaceMenu.BOUTON == 0 or SpaceGamePlay.SpaceMenu.BOUTON == 1:
                        ENINTRO = False
                        ENJEU = True

                    if SpaceGamePlay.SpaceMenu.BOUTON == 2:
                        ENINTRO = False
                        ENJEU = False

                # Apuyer sur la touche 'm' pour mute le jeu
                if event.key == pygame.K_m:
                    if SpaceGamePlay.SpaceSound.SON_EN_PAUSE == False:
                        SpaceGamePlay.SpaceSound.sounds['musique'].stop()
                        SpaceGamePlay.SpaceSound.SON_EN_PAUSE = True
                    else:
                        SpaceGamePlay.SpaceSound.sounds['musique'].play()
                        SpaceGamePlay.SpaceSound.SON_EN_PAUSE = False

            # Creation d'evenements similaires au touche du clavier mais pour manette

            # FIN

    except Exception as e:
        pass

    SpaceGamePlay.SpaceWindow.fenetre.fill(SpaceGamePlay.SpaceWindow.ESPACE)
    SpaceGamePlay.SpaceWindow.affichervie(SpaceGamePlay.NOMBRE_VIE)
    SpaceGamePlay.SpaceWindow.afficher_etoiles(etoiles, SpaceGamePlay.VITESSE_ETOILE)
    SpaceGamePlay.SpaceWindow.afficher_munition(SpaceGamePlay.MUNITIONS)
    SpaceGamePlay.SpaceWindow.dessine_missile(SpaceGamePlay)
    SpaceGamePlay.SpaceWindow.afficher(vaisseau)
    SpaceGamePlay.SpaceMenu.afficherBoutonMenu()
    SpaceGamePlay.SpaceMenu.afficher_menu()

    if SpaceGamePlay.COMPTEUR_BOUCLE % 60 == 0 and SpaceGamePlay.COMPTEUR_BOUCLE < 3600:
        SpaceGamePlay.VITESSE_JEU += 0.10

    if SpaceGamePlay.COMPTEUR_BOUCLE % 150 == 0:
        if SpaceGamePlay.MUNITIONS > 0:
            missile = Missiles.Missile(SpaceGamePlay)
            missile.placeMissile(vaisseau.position[0] + SpaceGamePlay.SpaceWindow.VAISSEAU_LARGEUR / 2, vaisseau.position[1])
            SpaceGamePlay.missiles.append(missile)

    pygame.display.flip()
    temps.tick(60)
    SpaceGamePlay.COMPTEUR_BOUCLE += 1

    while ENJEU == True:

        vaisseau.prendsPose(SpaceGamePlay.SpaceWindow.images['vaisseau_jaune_sans_flamme'])


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ENJEU = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    if SpaceGamePlay.MUNITIONS == 0:
                        if SpaceGamePlay.SpaceSound.SON_EN_PAUSE == False:
                            SpaceGamePlay.SpaceSound.sounds['no_bullets'].play()

                    else:
                        if SpaceGamePlay.SpaceSound.SON_EN_PAUSE == False:
                            SpaceGamePlay.SpaceSound.sounds['piou'].play()
                        missile = Missiles.Missile(SpaceGamePlay)
                        missile.placeMissile(vaisseau.position[0] + SpaceGamePlay.SpaceWindow.VAISSEAU_LARGEUR / 2,
                                             vaisseau.position[1])
                        SpaceGamePlay.missiles.append(missile)
                        SpaceGamePlay.MUNITIONS -= 1

                if event.key == pygame.K_m:
                    if SpaceGamePlay.SpaceSound.SON_EN_PAUSE == False:
                        SpaceGamePlay.SpaceSound.sounds['musique'].stop()
                        SpaceGamePlay.SpaceSound.SON_EN_PAUSE = True
                    else:
                        SpaceGamePlay.SpaceSound.sounds['musique'].play()
                        SpaceGamePlay.SpaceSound.SON_EN_PAUSE = False


        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            if vaisseau.position[0] + SpaceGamePlay.SpaceWindow.VAISSEAU_LARGEUR < SpaceGamePlay.SpaceWindow.FENETRE_LARGEUR:
                vaisseau.prendsPose(SpaceGamePlay.SpaceWindow.images['vaisseau_jaune_sans_flamme'])
                vaisseau.place(vaisseau.position[0] + SpaceGamePlay.DEPLACEMENT_VAISSEAU, vaisseau.position[1], 0)

        if keys[pygame.K_LEFT]:
            if vaisseau.position[0] <= 0:
                vaisseau.prendsPose(SpaceGamePlay.SpaceWindow.images['vaisseau_jaune_sans_flamme'])
            else:
                vaisseau.prendsPose(SpaceGamePlay.SpaceWindow.images['vaisseau_jaune_sans_flamme'])
                vaisseau.place(vaisseau.position[0]- SpaceGamePlay.DEPLACEMENT_VAISSEAU, vaisseau.position[1], 0)

        # BAS
        if keys[pygame.K_DOWN]:
            if vaisseau.position[1] < SpaceGamePlay.SpaceWindow.FENETRE_HAUTEUR - SpaceGamePlay.SpaceWindow.VAISSEAU_HAUTEUR:
                vaisseau.prendsPose(SpaceGamePlay.SpaceWindow.images['vaisseau_jaune_sans_flamme'])
                vaisseau.place(vaisseau.position[0], vaisseau.position[1]+ SpaceGamePlay.DEPLACEMENT_VAISSEAU, 0)
        # HAUT
        if keys[pygame.K_UP]:
            if vaisseau.position[1] > 0:
                vaisseau.prendsPose(SpaceGamePlay.SpaceWindow.images['vaisseau_jaune_avec_flamme'])
                vaisseau.place(vaisseau.position[0], vaisseau.position[1] - SpaceGamePlay.DEPLACEMENT_VAISSEAU, 0)

        SpaceGamePlay.SpaceSpawner.spawn_planete()
        SpaceGamePlay.SpaceSpawner.spawn_ufo()

        SpaceGamePlay.SpaceWindow.fenetre.fill(SpaceGamePlay.SpaceWindow.ESPACE)
        SpaceGamePlay.SpaceWindow.afficher_etoiles(etoiles, SpaceGamePlay.VITESSE_ETOILE)
        SpaceGamePlay.SpaceWindow.dessine_missile(SpaceGamePlay)

        SpaceGamePlay.SpaceWindow.afficher(vaisseau)
        SpaceGamePlay.SpaceWindow.afficher_planetes(SpaceGamePlay)
        SpaceGamePlay.SpaceWindow.afficher_ufo(SpaceGamePlay)
        SpaceGamePlay.SpaceWindow.affichervie(SpaceGamePlay.NOMBRE_VIE)
        SpaceGamePlay.SpaceWindow.afficher_munition(SpaceGamePlay.MUNITIONS)
        SpaceGamePlay.SpaceSpawner.tir_random_ufo()
        SpaceGamePlay.SpaceMouvements.deplace_Objets()

        temps.tick(60)
        pygame.display.flip()
        SpaceGamePlay.COMPTEUR_BOUCLE += 1
