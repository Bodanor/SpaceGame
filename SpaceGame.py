import time
from Source.Etoile import *
from Source.Affichage import *
from Source.Spawn import *
from Source.Deplacement import *
from Source.Collisions import *

#Calcul du temps de chargement du jeu
temps_debut_complet = time.time()

###### Difficulté ######
def difficulte(niveau_difficulte):
    # Les valeures du jeu changent en fonction de la difficulté choisie
    if niveau_difficulte == 0:
        MENU = ['Jouer', 'Facile>', 'Quitter']
        AJOUT_MUNITION = 20
        MUNITIONS = 20
        VITESSE_JEU = 3
        VITESSE_MISSILE = 15
        NOMBRE_VIE = 3
        DEPLACEMENT_VAISSEAU = 7
        FREQUENCE_APPARITION_TROU_NOIR = 500
        FREQUENCE_TIR = 180

    elif niveau_difficulte == 1:
        MENU = ['Jouer', '<Moyen>', 'Quitter']
        AJOUT_MUNITION = 15
        MUNITIONS = 15
        VITESSE_JEU = 5
        VITESSE_MISSILE = 10
        NOMBRE_VIE = 2
        DEPLACEMENT_VAISSEAU = 6
        FREQUENCE_APPARITION_TROU_NOIR = 250
        FREQUENCE_TIR = 120
    elif niveau_difficulte == 2:
        MENU = ['Jouer', '<Difficile', 'Quitter']
        AJOUT_MUNITION = 10
        MUNITIONS = 10
        VITESSE_JEU = 7
        VITESSE_MISSILE = 7
        NOMBRE_VIE = 1
        DEPLACEMENT_VAISSEAU = 5
        FREQUENCE_APPARITION_TROU_NOIR = 100
        FREQUENCE_TIR = 60

    return MENU, AJOUT_MUNITION, MUNITIONS, VITESSE_JEU, VITESSE_MISSILE, NOMBRE_VIE, DEPLACEMENT_VAISSEAU, FREQUENCE_APPARITION_TROU_NOIR
###### FIN DIFFICULTE #####

###### MEILLEUR SCORE ######
def bestscore(bestscore, niveau_difficulte):

    #Garde en mémoire le meilleur score
    try:
        with open('scoreboard.txt', 'r+') as fichier: #Ouverture du fichier Scoreboard et lecture de celui-ci

            meilleurs_scores = fichier.readlines()

            if niveau_difficulte == 0:
                meilleur_score = int(meilleurs_scores[0])
                if meilleur_score != bestscore:  # Check si le score en jeu est different du score dans le fichier
                    if meilleur_score < bestscore:
                        meilleurs_scores[0] = str(bestscore) + '\n'
                        fichier.close()
                        fichier = open('scoreboard.txt', 'w+')
                        fichier.writelines(meilleurs_scores)
                        fichier.close()

            if niveau_difficulte == 1:
                meilleur_score = int(meilleurs_scores[1])
                if meilleur_score != bestscore:  # Check si le score en jeu est different du score dans le fichier
                    if meilleur_score < bestscore:
                        meilleurs_scores[1] = str(bestscore) + '\n'
                        fichier.close()
                        fichier = open('scoreboard.txt', 'w+')
                        fichier.writelines(meilleurs_scores)
                        fichier.close()

            if niveau_difficulte == 2:
                meilleur_score = int(meilleurs_scores[2])
                if meilleur_score != bestscore:  # Check si le score en jeu est different du score dans le fichier
                    if meilleur_score < bestscore:
                        meilleurs_scores[2] = str(bestscore) + '\n'
                        fichier.close()
                        fichier = open('scoreboard.txt', 'w+')
                        fichier.writelines(meilleurs_scores)
                        fichier.close()

            if meilleur_score == "":  # Si le fichier est vide alors on ecrit 0
                fichier.write("0")
                fichier.close()

            with open('scoreboard.txt', 'r+') as fichier:  # Ouverture du fichier Scoreboard et lecture de celui-ci
                meilleurs_scores = fichier.readlines()
                if niveau_difficulte == 0:
                    meilleur_score = int(meilleurs_scores[0])
                    phrase = str("Meilleur score: {}".format(int(round(meilleur_score, 0)))) #Affichage du mielleur score actuel qui se trouve dans le fichier
                    marquoir = police.render(phrase, True, JAUNE)
                    longueur_text_x, longueur_text_y = marquoir.get_size()
                    fenetre.blit(marquoir, (FENETRE_LARGEUR//2 - longueur_text_x//2, FENETRE_HAUTEUR // 24))

                if niveau_difficulte == 1:
                    meilleur_score = int(meilleurs_scores[1])
                    phrase = str("Meilleur score: {}".format(int(round(meilleur_score,
                                                                       0))))  # Affichage du mielleur score actuel qui se trouve dans le fichier
                    marquoir = police.render(phrase, True, JAUNE)
                    longueur_text_x, longueur_text_y = marquoir.get_size()
                    fenetre.blit(marquoir, (FENETRE_LARGEUR // 2 - longueur_text_x // 2, FENETRE_HAUTEUR // 24))

                if niveau_difficulte == 2:
                    meilleur_score = int(meilleurs_scores[2])
                    phrase = str("Meilleur score: {}".format(int(round(meilleur_score,
                                                                       0))))  # Affichage du mielleur score actuel qui se trouve dans le fichier
                    marquoir = police.render(phrase, True, JAUNE)
                    longueur_text_x, longueur_text_y = marquoir.get_size()
                    fenetre.blit(marquoir, (FENETRE_LARGEUR // 2 - longueur_text_x // 2, FENETRE_HAUTEUR // 24))

    except FileNotFoundError: #Si le fichier n'existe pas alors on créer un nouveau fichier et on ecrit 0
        fichier = open('scoreboard.txt', 'w')
        fichier.write("0\n0\n0")
        fichier.close()

    except IndexError: #Si le fichier n'existe pas alors on créer un nouveau fichier et on ecrit 0
        fichier = open('scoreboard.txt', 'w')
        fichier.write("0\n0\n0")
        fichier.close()

    except ValueError:  #Si la ligne lue n'est pas un nombre alors le fichier est corrompu et on affiche qu'il est corrompu
        phrase = str("Meilleur score : Probleme avec le fichier Scoreboard. Veuillez le supprimer")
        marquoir = police.render(phrase, True, ROUGE)
        longueur_text_x, longueur_text_y = marquoir.get_size()

        fenetre.blit(marquoir, (FENETRE_LARGEUR // 2 - longueur_text_x // 2, FENETRE_HAUTEUR // 24))
###### FIN MEILLEUR SCORE ######


################### FIN FONCTIONS ###################


# Changement de l'icône de jeu
game_icon = pygame.image.load("Images/vaisseau_jaune_avec_flamme.png")
pygame.display.set_icon(game_icon)

# Icone vie
vie_image = pygame.image.load('Images/vaisseau_rouge_avec_flamme.png')

# Initiamisation de pygame
pygame.init()


# Son
print("[LOG] CHARGEMENTS DES BRUITAGES... ")
pygame.mixer.init()
explosion_ufo = pygame.mixer.Sound("Son/explosion_ufo.wav")
explosion_ufo.set_volume(0.2)
choix = pygame.mixer.Sound("Son/choix_menu.wav")
choix_doite_gauche = pygame.mixer.Sound("Son/droite_gauche.wav")
choix_gauche_droite = pygame.mixer.Sound("Son/gauche_droite.wav")
piou = pygame.mixer.Sound("Son/piou.wav")
no_bullets = pygame.mixer.Sound("Son/no_bullets.wav")
no_bullets.set_volume(0.15)


moinsvie = pygame.mixer.Sound("Son/moinsvie.wav")
moinsvie.set_volume(0.2)

sonBonus = pygame.mixer.Sound("Son/bonus.wav")
sonBonus.set_volume(0.4)


start = pygame.mixer.Sound("Son/start.wav")
start.set_volume(0.2)
back = pygame.mixer.Sound("Son/back.wav")
print("[LOG] BRUITAGES CHARGE !")

print("[LOG] CHARGEMENT BANDE SON...")
musique = pygame.mixer.Sound("Bande Son/musiquePrincipal.wav")
musique.set_volume(0.3)

print("[LOG] BANDE SON CHARGEE!")
#FIN DES SONS#




# Création de la fenêtre
fenetre = pygame.display.set_mode((FENETRE_LARGEUR, FENETRE_HAUTEUR), pygame.RESIZABLE)
pygame.display.set_caption('Space Game')

# Création des entités
vaisseau = nouvelleEntite()

# CHARGER TOUTES LES IMAGES #
print("[LOG] CHARGEMENT DES IMAGES...")
print("[LOG] CHARGEMENT DES PLANETES...")
for nom_image, nom_fichier in (('Planete1', 'planete1.png'),
                               ('Planete2', 'planete2.png'),
                               ('Planete3', 'planete3.png'),
                               ('Planete4', 'planete4.png'),
                               ('Planete5', 'planete5.png'),
                               ('Planete6', 'planete6.png'),
                               ('Planete7', 'planete7.png'),
                               ('Planete8', 'planete8.png'),
                               ('Planete9', 'planete9.png'),
                               ('Planete10', 'planete10.png'),
                               ('Planete11', 'planete11.png'),
                               ('Planete12', 'planete12.png'),
                               ('Planete13', 'planete13.png'),
                               ('Planete14', 'planete14.png'),
                               ('Planete15', 'planete15.png'),
                               ('Planete16', 'planete16.png'),
                               ('trou_noir', 'trou_noir.png')):
    chemin = 'Images/' + nom_fichier
    image = pygame.image.load(chemin).convert_alpha(fenetre)
    image = pygame.transform.scale(image, (TAILLE_PLANETE, TAILLE_PLANETE))
    planete = nouvelleEntite()

    ajouteImage(planete, nom_image, image)
    prendsPose(planete, nom_image)
    LISTE_PLANETE.append(planete)

print("[LOG] TOUTES LES PLANETES SONT CHARGEES")
print("[LOG] CHARGEMENT DES VAISSEAUX....")
for nom_image, nom_fichier in (('vaisseau_jaune_sans_flamme', 'vaisseau_jaune_sans_flamme.png'),
                               ('vaisseau_jaune_avec_flamme', 'vaisseau_jaune_avec_flamme.png'),
                               ('vaisseau_rouge_avec_flamme', 'vaisseau_rouge_avec_flamme.png'),
                               ('vaisseau_rouge_sans_flamme', 'vaisseau_rouge_sans_flamme.png'),
                               ('vaisseau_blanc_avec_flamme', 'vaisseau_blanc_avec_flamme.png'),
                               ('vaisseau_blanc_sans_flamme', 'vaisseau_blanc_sans_flamme.png'),
                               ('vaisseau_bleu_avec_flamme', 'vaisseau_bleu_avec_flamme.png'),
                               ('vaisseau_bleu_sans_flamme', 'vaisseau_bleu_sans_flamme.png'),
                               ('vaisseau_rose_avec_flamme', 'vaisseau_rose_avec_flamme.png'),
                               ('vaisseau_rose_sans_flamme', 'vaisseau_rose_sans_flamme.png'),
                               ('vaisseau_vert_avec_flamme', 'vaisseau_vert_avec_flamme.png'),
                               ('vaisseau_vert_sans_flamme', 'vaisseau_vert_sans_flamme.png')):
    chemin = 'Images/' + nom_fichier
    image = pygame.image.load(chemin).convert_alpha(fenetre)
    image = pygame.transform.scale(image, (VAISSEAU_LARGEUR, VAISSEAU_HAUTEUR))
    ajouteImage(vaisseau, nom_image, image)

print("[LOG] TOUS LES VAISSEAUX SONT CHARGES")
print("[LOG] CHARGEMENT DE L'UFO...")

for i in range(NOMBRE_UFO):
    chemin = 'Images/ufo.png'
    image = pygame.image.load(chemin).convert_alpha(fenetre)
    image = pygame.transform.scale(image, (UFO_TAILLE, UFO_TAILLE))
    ufo = nouvelleEntite()
    ajouteImage(ufo, 'ufo{}'.format(i), image)
    prendsPose(ufo, 'ufo{}'.format(i))
    LISTE_UFO.append(ufo)
print("[LOG] L'UFO EST CHARGE")

print("[LOG] CHARGEMENT DES BONUS")

for i in range(NOMBRE_BONUS):
    chemin = 'Images/bonus.png'
    image = pygame.image.load(chemin).convert_alpha(fenetre)
    image = pygame.transform.scale(image, (BONUS_TAILLE, BONUS_TAILLE))
    bonus = nouvelleEntite()
    ajouteImage(bonus, 'bonus{}'.format(i), image)
    prendsPose(bonus, 'bonus{}'.format(i))
    BONUS_LISTE.append(bonus)

print("[LOG] BONUS CHARGE")
print("[LOG] CHARGEMENT DU TROU NOIR")

for i in range(NOMBRE_TROU_NOIR):
    chemin = 'Images/trou_noir.png'
    image = pygame.image.load(chemin).convert_alpha(fenetre)
    image = pygame.transform.scale(image, (TROU_NOIR_TAILLE, TROU_NOIR_TAILLE))
    trou_noir = nouvelleEntite()
    ajouteImage(trou_noir, 'trou_noir{}'.format(i), image)
    prendsPose(trou_noir, 'trou_noir{}'.format(i))
    LISTE_TROU_NOIR.append(trou_noir)
print("[LOG]  LE TROU NOIR EST CHARGE")

print("[LOG] TOUTES LES IMAGES SONT CHARGEES ! ")
# FIN CHARGEMENT IMAGES #


# Postionement du vaisseau
place(vaisseau, (FENETRE_LARGEUR / 2) - VAISSEAU_LARGEUR / 2, FENETRE_HAUTEUR - VAISSEAU_HAUTEUR, 0)

# Scene et planete
scene = []
scene.append(vaisseau)

# Variable de jeu et Temps
fini = False
enintro = True
enjeu = False
temps = pygame.time.Clock()

# Police d'écriture#
police = pygame.font.SysFont('monospace', FENETRE_HAUTEUR // 40, True)
POLICE_ECRITURE_BOUTON = pygame.font.SysFont('monospace', 36)

# Création des étoiles
etoiles = cree_etoiles(NOMBRE_ETOILES, FENETRE_LARGEUR, FENETRE_HAUTEUR)

#Création des couloirs
creation_couloirs_planete(COULOIRS, FENETRE_LARGEUR)
couloir_utilise = []
couloir_utilise_ufo = []
couloir_utilise_trou_noir = []
couloir_utilise_bonus = []

#Activation des collisions
collision_active = True
enbonus = False

#Premiere fois
Premiere_fois = True

# Difficulté
niveau_difficulte = 0
print("[LOG] LE CHARGEMENT COMPLET A PRIS {} secondes".format(round(time.time() - temps_debut_complet, 2)))

######CREATION DU MENU######
while enintro:

    #Lancement de la bande son
    if SON_EN_PAUSE == False:
        if SON_EN_COURS == True:
            musique.play(-1)
            SON_EN_COURS = False
            SON_EN_PAUSE = False
    else:
        musique.stop()

    #Positionnement du vaisseau
    visible(vaisseau)
    prendsPose(vaisseau, POSE_VAISSEAU_FLAMME[0])
    place(vaisseau, (FENETRE_LARGEUR / 2) - VAISSEAU_LARGEUR / 2,
          FENETRE_HAUTEUR - VAISSEAU_HAUTEUR, 0)

    evenement = pygame.event.get()
    for event in evenement:

        # Changement de taille d'écran
        if event.type == pygame.VIDEORESIZE:

            #Changement de la taille des couloirs, des etoiles, et repositionnement du vaisseau
            FENETRE_LARGEUR, FENETRE_HAUTEUR = fenetre.get_size()
            COULOIRS =[]

            creation_couloirs_planete(COULOIRS, FENETRE_LARGEUR)
            etoiles = cree_etoiles(NOMBRE_ETOILES, FENETRE_LARGEUR, FENETRE_HAUTEUR)
            place(vaisseau, (FENETRE_LARGEUR / 2) - VAISSEAU_LARGEUR / 2, FENETRE_HAUTEUR - VAISSEAU_HAUTEUR, 0)

        # Quitter avec la croix
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


        ### Controle clavier ###
        if event.type == pygame.KEYDOWN:
            # incrémentation de la difficulté
            if event.key == pygame.K_RIGHT:
                if BOUTON == 1:
                    if niveau_difficulte < 2:
                        if SON_EN_PAUSE == False:
                            choix_gauche_droite.play()
                        niveau_difficulte += 1
                        MENU, AJOUT_MUNITION, MUNITIONS, VITESSE_JEU, VITESSE_MISSILE, NOMBRE_VIE, DEPLACEMENT_VAISSEAU, FREQUENCE_APPARITION_TROU_NOIR = difficulte(
                            niveau_difficulte)
                    else:
                        None
            # Décrémentation de la difficulté
            if event.key == pygame.K_LEFT:
                if BOUTON == 1:
                    if niveau_difficulte > 0:
                        if SON_EN_PAUSE == False:
                            choix_doite_gauche.play()
                        niveau_difficulte -= 1
                        MENU, AJOUT_MUNITION, MUNITIONS, VITESSE_JEU, VITESSE_MISSILE, NOMBRE_VIE, DEPLACEMENT_VAISSEAU, FREQUENCE_APPARITION_TROU_NOIR = difficulte(
                            niveau_difficulte)
                    else:
                        None
            # déplacement dans le menu
            if event.key == pygame.K_DOWN:
                if SON_EN_PAUSE == False:
                    choix.play()
                if BOUTON < 2:
                    BOUTON += 1
                else:
                    BOUTON = 0

            # déplacement dans le menu
            if event.key == pygame.K_UP:
                if SON_EN_PAUSE == False:
                    choix.play()
                if BOUTON < 1:
                    BOUTON = 2
                else:
                    BOUTON -= 1

            # lancer/quitter le jeu
            if event.key == pygame.K_RETURN:
                if SON_EN_PAUSE == False:
                    start.play()
                # Jouer
                if BOUTON == 0 or BOUTON == 1:
                    enintro = False
                    enjeu = True
                    SCORE = 0
                    COMPTEUR_BOUCLE = 1
                    BOUTON = 0

                # Quitter le programme
                if BOUTON == 2:
                    enjeu = False
                    enintro = False


            #Supprimer le son du jeu
            if event.key == pygame.K_m:
                if SON_EN_PAUSE == True:

                    COMPTEUR_NOTIF = 180 #Affiche en message pendant trois secondes
                    COMPTEUR_MUTE += 1 #Incremente notre compteur qui permet de voir si on a désactivé le son

                    SON_EN_PAUSE = False
                    SON_EN_COURS = True
                else:

                    COMPTEUR_NOTIF = 180
                    COMPTEUR_MUTE +=1

                    SON_EN_PAUSE = True
                    SON_EN_COURS = False
        ### FIN DES CONTROLES AU CLAVIER ###


    # Mécanique du jeu automatique
    # Incrémentation de la vitesse du jeu dans le menu
    if COMPTEUR_BOUCLE % 60 == 0 and COMPTEUR_BOUCLE < 3600:
        VITESSE_JEU += 0.10

    # Tir auto
    if COMPTEUR_BOUCLE % 150 == 0:
        if MUNITIONS > 0:
            ajouter_missile((position(vaisseau)[0] + VAISSEAU_LARGEUR / 2, position(vaisseau)[1]))


    # Affichage Vaisseau, etoile, vie, score

    fenetre.fill(ESPACE)
    afficher_etoiles(fenetre, VITESSE_JEU, etoiles, FENETRE_HAUTEUR, FENETRE_LARGEUR)
    dessine_missile(fenetre, VITESSE_MISSILE)

    # Affichage général
    affiche(scene, fenetre)

    score(fenetre, police, SCORE, FENETRE_HAUTEUR)
    bestscore(0, niveau_difficulte)
    vie(fenetre, vie_image, NOMBRE_VIE, FENETRE_HAUTEUR, FENETRE_LARGEUR)
    afficher_munition(fenetre, police,MUNITIONS, FENETRE_HAUTEUR)
    afficherBoutonMenu(fenetre, POLICE_ECRITURE_BOUTON, BOUTON, MENU)
    if Premiere_fois: #Affichage des controles quand on lance le jeu
        afficher_controles(fenetre, police)
    if COMPTEUR_NOTIF > 0: #Affichage des notifications et décrémentations du compteur
        coinNotif(fenetre, police, COMPTEUR_NOTIF, COMPTEUR_MUTE, FENETRE_LARGEUR)
        COMPTEUR_NOTIF -=1
    pygame.display.flip()

    # Temps

    temps.tick(60)
    COMPTEUR_BOUCLE += 1

    #####FIN DU MENU#####

    #####BOUCLE DU JEU#####
    while enjeu:

        Premiere_fois = False

        if SON_EN_PAUSE == False: #Joue la bande son
            if SON_EN_COURS == True:
                musique.play(-1)
                SON_EN_COURS = False
                SON_EN_PAUSE = False

        else:
            musique.stop()

        # Arrêter le jeu si plus de vie
        if NOMBRE_VIE == 0:
            # Réinitialisation des variables, sauvegarde du meilleur score
            bestscore(SCORE, niveau_difficulte)
            SCORE = 0
            enintro = True
            enjeu = False
            couloir_utilise = []
            PLANETE_EN_LISTE = []
            UFO_EN_LISTE = []
            spawn_planete(couloir_utilise, PLANETE_EN_LISTE, LISTE_PLANETE, COULOIRS, TAILLE_PLANETE)
            deplace_planete(VITESSE_JEU, COMPTEUR_PAUSE, PLANETE_EN_LISTE, couloir_utilise, FENETRE_HAUTEUR)
            visible(vaisseau)
            COMPTEUR_COLLISION = 0
            BOUTON = 0
            MISSILE_UFO_EN_LISTE = []
            TROU_NOIR_EN_LISTE = []
            BONUS_EN_LISTE = []
            missiles = []
            etoiles.clear()
            etoiles = cree_etoiles(NOMBRE_ETOILES, FENETRE_LARGEUR, FENETRE_HAUTEUR)
            afficher_etoiles(fenetre, VITESSE_JEU, etoiles, FENETRE_HAUTEUR, FENETRE_LARGEUR)
            sonBonus.stop()
            COMPTEUR_BONUS = 0
            enbonus = False

            # Reprise des paramètres de la difficulté choisie dans le menu
            MENU, AJOUT_MUNITION, MUNITIONS, VITESSE_JEU, VITESSE_MISSILE, NOMBRE_VIE, DEPLACEMENT_VAISSEAU, FREQUENCE_APPARITION_TROU_NOIR = difficulte(
                niveau_difficulte)

        # Spawn des entités ennemies
        spawn_planete(couloir_utilise, PLANETE_EN_LISTE, LISTE_PLANETE, COULOIRS, TAILLE_PLANETE)
        deplace_planete(VITESSE_JEU, COMPTEUR_PAUSE, PLANETE_EN_LISTE, couloir_utilise, FENETRE_HAUTEUR)
        spawn_ufo(couloir_utilise_ufo, UFO_EN_LISTE, PLANETE_EN_LISTE, LISTE_UFO, TAILLE_PLANETE, COULOIRS, MISSILE_UFO_EN_LISTE)
        spawn_trou_noir(niveau_difficulte, couloir_utilise_trou_noir, FREQUENCE_APPARITION_TROU_NOIR, TROU_NOIR_EN_LISTE, LISTE_TROU_NOIR, PLANETE_EN_LISTE, COULOIRS, TAILLE_PLANETE)
        deplace_ufo(VITESSE_JEU, couloir_utilise_ufo, COMPTEUR_PAUSE, UFO_EN_LISTE, FENETRE_HAUTEUR)
        deplace_trou_noir(VITESSE_JEU, couloir_utilise_trou_noir, COMPTEUR_PAUSE, TROU_NOIR_EN_LISTE, FENETRE_HAUTEUR)
        spawn_bonus(niveau_difficulte, couloir_utilise_bonus, FREQUENCE_APPARITION_BONUS, BONUS_EN_LISTE, BONUS_LISTE, PLANETE_EN_LISTE, COULOIRS, TAILLE_PLANETE)
        deplace_bonus(VITESSE_JEU, couloir_utilise_bonus, COMPTEUR_PAUSE, BONUS_EN_LISTE, FENETRE_HAUTEUR)

        #pose du vaisseau
        prendsPose(vaisseau, POSE_VAISSEAU_SANS_FLAMME[0])
        evenement = pygame.event.get()

        for event in evenement:
            # Changement de l'écran
            if event.type == pygame.VIDEORESIZE:


                #Garder les mêmes positions pour les objets
                position_x_vaisseau, position_y_vaisseau = position(vaisseau)

                ancienne_largeur, ancienne_hauteur = FENETRE_LARGEUR, FENETRE_HAUTEUR

                FENETRE_LARGEUR, FENETRE_HAUTEUR = fenetre.get_size()
                fenetre.fill(ESPACE)
                etoiles.clear()
                etoiles = cree_etoiles(NOMBRE_ETOILES, FENETRE_LARGEUR, FENETRE_HAUTEUR)
                COULOIRS = []
                creation_couloirs_planete(COULOIRS, FENETRE_LARGEUR)
                for planete in PLANETE_EN_LISTE:
                    couloir = afficherCouloir(planete)
                    position_x_planete, position_y_planete = position(planete)

                    place(planete, COULOIRS[couloir][0], position_y_planete, couloir)


                for ufo in UFO_EN_LISTE:
                    couloir = afficherCouloir(ufo)
                    position_x_ufo, position_y_ufo = position(ufo)

                    place(ufo, COULOIRS[couloir][0], position_y_ufo, couloir)

                for trou_noir in TROU_NOIR_EN_LISTE:
                    couloir = afficherCouloir(trou_noir)
                    position_x_trou_nooir, position_y_trou_noir = position(trou_noir)

                    place(trou_noir, COULOIRS[couloir][0], position_y_trou_noir, couloir)


                for missiles in missile:
                    position_x_missile, position_y_missile = positionMissile(missiles)[0], positionMissile(missiles)[1]

                    placeMissile(missiles, (position_x_missile / ancienne_largeur) * fenetre.get_size()[0],
                          (position_y_missile / ancienne_hauteur) * fenetre.get_size()[1])

                place(vaisseau, (position_x_vaisseau / ancienne_largeur) * fenetre.get_size()[0],
                      (position_y_vaisseau / ancienne_hauteur) * fenetre.get_size()[1], 0)

                dessine_missile(fenetre, VITESSE_MISSILE)
                dessine_missile_ufo(fenetre, MISSILE_UFO_EN_LISTE, VITESSE_JEU)
                afficher_etoiles(fenetre, VITESSE_JEU, etoiles, FENETRE_HAUTEUR, FENETRE_LARGEUR)
                affiche(scene, fenetre)
                affiche(PLANETE_EN_LISTE, fenetre)
                affiche(UFO_EN_LISTE, fenetre)
                affiche(TROU_NOIR_EN_LISTE, fenetre)
                affiche(BONUS_EN_LISTE, fenetre)
                score(fenetre, police, SCORE, FENETRE_HAUTEUR)
                afficher_munition(fenetre, police,MUNITIONS, FENETRE_HAUTEUR)
                vie(fenetre, vie_image, NOMBRE_VIE, FENETRE_HAUTEUR, FENETRE_LARGEUR)
            # Quitter avec la croix

            if event.type == pygame.QUIT:
                (SCORE, niveau_difficulte)
                pygame.quit()
                quit()


            # Tir
            if event.type == pygame.KEYDOWN:
                # Vérification qu'on est pas en pause
                if event.key == pygame.K_SPACE:
                    if COMPTEUR_PAUSE % 2 != 0:
                        None
                    else:
                        # Pas de munition
                        if MUNITIONS == 0:
                            if SON_EN_PAUSE == False:
                                no_bullets.play()
                        else:
                            # Tir de munitions
                            if SON_EN_PAUSE == False:
                                piou.play()
                            ajouter_missile((position(vaisseau)[0] + VAISSEAU_LARGEUR / 2, position(vaisseau)[1]))
                            MUNITIONS -= 1

                #Désactivation du son
                if event.key == pygame.K_m:

                    if SON_EN_PAUSE == True:

                        COMPTEUR_NOTIF = 180
                        COMPTEUR_MUTE += 1

                        SON_EN_PAUSE = False
                        SON_EN_COURS = True

                        if enbonus == True:
                            sonBonus.play()
                    else:

                        COMPTEUR_NOTIF = 180
                        COMPTEUR_MUTE += 1

                        SON_EN_PAUSE = True
                        SON_EN_COURS = False



                ######## Touche dans le menu Pause########
                # Entrer ou sortir du menu pause
                if event.key == pygame.K_ESCAPE:
                    COMPTEUR_PAUSE += 1

                #Controle dans le menu pause
                if COMPTEUR_PAUSE % 2 != 0:
                    # Bas
                    if event.key == pygame.K_DOWN:
                        if SON_EN_PAUSE == False:
                            choix.play()
                        if BOUTON < 1:
                            BOUTON += 1
                        else:
                            BOUTON = 0

                    # Haut
                    if event.key == pygame.K_UP:
                        if SON_EN_PAUSE == False:
                            choix.play()
                        if BOUTON == 1:
                            BOUTON = 0
                        elif BOUTON == 0:
                            BOUTON = 1

                ####Enter#####
                if COMPTEUR_PAUSE % 2 != 0:
                    if event.key == pygame.K_RETURN:
                        # continuer le jeu
                        if BOUTON == 0:
                            COMPTEUR_PAUSE += 1

                        # Revenir au menu principal
                        if BOUTON == 1:
                            if SON_EN_PAUSE == False:
                                sonBonus.stop()
                                back.play()

                            #Réinitialisation des variables, sauvegarde du meilleur score
                            bestscore(SCORE, niveau_difficulte)
                            COMPTEUR_PAUSE += 1
                            SCORE = 0
                            enintro = True
                            enjeu = False
                            couloir_utilise = []
                            PLANETE_EN_LISTE = []
                            UFO_EN_LISTE = []
                            spawn_planete(couloir_utilise, PLANETE_EN_LISTE, LISTE_PLANETE, COULOIRS, TAILLE_PLANETE)
                            deplace_planete(VITESSE_JEU, COMPTEUR_PAUSE, PLANETE_EN_LISTE, couloir_utilise, FENETRE_HAUTEUR)
                            visible(vaisseau)
                            COMPTEUR_COLLISION = 0
                            BOUTON = 0
                            MISSILE_UFO_EN_LISTE = []
                            TROU_NOIR_EN_LISTE = []
                            BONUS_EN_LISTE = []
                            missiles = []
                            etoiles.clear()
                            etoiles = cree_etoiles(NOMBRE_ETOILES, FENETRE_LARGEUR, FENETRE_HAUTEUR)
                            afficher_etoiles(fenetre, VITESSE_JEU, etoiles, FENETRE_HAUTEUR, FENETRE_LARGEUR)
                            COMPTEUR_BONUS = 0
                            sonBonus.stop()
                            enbonus = False

                            # Reprise des paramètres de la difficulté choisie dans le menu
                            MENU, AJOUT_MUNITION, MUNITIONS, VITESSE_JEU, VITESSE_MISSILE, NOMBRE_VIE, DEPLACEMENT_VAISSEAU, FREQUENCE_APPARITION_TROU_NOIR = difficulte(
                                niveau_difficulte)
                ########FIN BOUTON PAUSE########

        ########Déplacement du vaisseau########


        if COMPTEUR_PAUSE % 2 != 0: #freez le jeu
            pause(fenetre, POLICE_ECRITURE_BOUTON, BOUTON, MENU_PAUSE)
            pygame.display.flip()

        else:

            keys = pygame.key.get_pressed()


            #CONTROLE DU VAISSEAU
            # DROITE
            if keys[pygame.K_RIGHT]:
                if position(vaisseau)[0] + VAISSEAU_LARGEUR > FENETRE_LARGEUR:
                    None
                else:
                    prendsPose(vaisseau, POSE_VAISSEAU_FLAMME[0])
                    position_vaisseau = position(vaisseau)
                    place(vaisseau, position_vaisseau[0] + DEPLACEMENT_VAISSEAU, position_vaisseau[1], 0)

            # GAUCHE
            if keys[pygame.K_LEFT]:
                if position(vaisseau)[0] <= 0:
                    prendsPose(vaisseau, POSE_VAISSEAU_SANS_FLAMME[0])
                    position_vaisseau = position(vaisseau)
                else:
                    prendsPose(vaisseau, POSE_VAISSEAU_SANS_FLAMME[0])
                    position_vaisseau = position(vaisseau)
                    place(vaisseau, position_vaisseau[0] - DEPLACEMENT_VAISSEAU, position_vaisseau[1], 0)

            # BAS
            if keys[pygame.K_DOWN]:
                if position(vaisseau)[1] > FENETRE_HAUTEUR - VAISSEAU_HAUTEUR:
                    None
                else:
                    prendsPose(vaisseau, POSE_VAISSEAU_SANS_FLAMME[0])
                    position_vaisseau = position(vaisseau)
                    place(vaisseau, position_vaisseau[0], position_vaisseau[1] + DEPLACEMENT_VAISSEAU, 0)

            # HAUT
            if keys[pygame.K_UP]:
                if position(vaisseau)[1] < 0:
                    None
                else:
                    prendsPose(vaisseau, POSE_VAISSEAU_FLAMME[0])
                    position_vaisseau = position(vaisseau)
                    place(vaisseau, position_vaisseau[0], position_vaisseau[1] - DEPLACEMENT_VAISSEAU, 0)
            ########FIN CONTROLE DU VAISSEAU#######

            # incrémentation du Score, compteur, et missiles
            if COMPTEUR_BOUCLE % 60 == 0 and SCORE <= 1000:
                SCORE += 1
                VITESSE_JEU += 0.05

            if COMPTEUR_BOUCLE % 60 == 0 and SCORE > 750:
                SCORE += 1

            if COMPTEUR_BOUCLE % 6000 == 0:
                MUNITIONS += AJOUT_MUNITION

            if niveau_difficulte == 2:  # On regagne une vie tous les 200 scores si on est en difficile
                if COMPTEUR_BOUCLE % 12000 == 0:
                    NOMBRE_VIE += 1



            if enbonus == True:
                if COMPTEUR_BONUS == 600:
                    sonBonus.play()
                if SON_EN_PAUSE == True:
                    sonBonus.stop()

                if COMPTEUR_BONUS % 10 == 0:
                    vaisseau_random = random.randint(0,len(POSE_VAISSEAU_SANS_FLAMME)-1)
                prendsPose(vaisseau, POSE_VAISSEAU_SANS_FLAMME[vaisseau_random])

                COMPTEUR_BONUS -= 1


                if COMPTEUR_BONUS == 0:
                    collision_active = True
                    enbonus = False
                    visible(vaisseau)
                    sonBonus.stop()



            # Faire clignoter le vaisseau si collision
            if collision_active == False:

                if COMPTEUR_COLLISION == 180 or COMPTEUR_COLLISION == 150 or COMPTEUR_COLLISION == 120 or COMPTEUR_COLLISION == 90 or COMPTEUR_COLLISION == 60 or COMPTEUR_COLLISION == 30:
                    invisible(vaisseau)

                if COMPTEUR_COLLISION == 165 or COMPTEUR_COLLISION == 135 or COMPTEUR_COLLISION == 105 or COMPTEUR_COLLISION == 75 or COMPTEUR_COLLISION == 45 or COMPTEUR_COLLISION == 15:
                    visible(vaisseau)


                if COMPTEUR_COLLISION == 0: #Rendre le vaisseau visible quand les trois secondes sont passées
                    collision_active = True
                    visible(vaisseau)

                COMPTEUR_COLLISION -= 1

            # Affichage
            fenetre.fill(ESPACE)
            dessine_missile(fenetre, VITESSE_MISSILE)
            dessine_missile_ufo(fenetre, MISSILE_UFO_EN_LISTE, VITESSE_JEU)
            afficher_etoiles(fenetre, VITESSE_JEU, etoiles, FENETRE_HAUTEUR, FENETRE_LARGEUR)
            affiche(scene, fenetre)
            affiche(PLANETE_EN_LISTE, fenetre)
            affiche(UFO_EN_LISTE, fenetre)
            affiche(TROU_NOIR_EN_LISTE, fenetre)
            affiche(BONUS_EN_LISTE, fenetre)
            score(fenetre, police, SCORE, FENETRE_HAUTEUR)
            afficher_munition(fenetre, police,MUNITIONS, FENETRE_HAUTEUR)
            NOMBRE_VIE, COMPTEUR_COLLISION, collision_active, SCORE, enbonus, COMPTEUR_BONUS = collision_entite(PLANETE_EN_LISTE,  NOMBRE_VIE, COMPTEUR_COLLISION,COMPTEUR_BONUS, collision_active, SCORE, vaisseau, VAISSEAU_HAUTEUR, VAISSEAU_LARGEUR, TAILLE_PLANETE, SON_EN_PAUSE, moinsvie, couloir_utilise, missile, MISSILE_UFO_EN_LISTE, UFO_EN_LISTE, explosion_ufo, couloir_utilise_ufo, UFO_TAILLE, TROU_NOIR_EN_LISTE, TROU_NOIR_TAILLE, couloir_utilise_trou_noir,BONUS_TAILLE, BONUS_EN_LISTE,couloir_utilise_bonus, enbonus, sonBonus)
            vie(fenetre, vie_image, NOMBRE_VIE, FENETRE_HAUTEUR, FENETRE_LARGEUR)

            #Afficher les notifications
            if COMPTEUR_NOTIF>0:
                coinNotif(fenetre, police, COMPTEUR_NOTIF, COMPTEUR_MUTE, FENETRE_LARGEUR)
                COMPTEUR_NOTIF -= 1
            pygame.display.flip()
            tir_random_ufo(MISSILE_UFO_EN_LISTE, UFO_EN_LISTE, COMPTEUR_BOUCLE, FREQUENCE_TIR)
            # Temps
            temps.tick(60)
            COMPTEUR_BOUCLE += 1





pygame.display.quit()
pygame.quit()
exit()