import pygame
import random

######CONSTANTES#######
# Couleur
ESPACE = (0, 0, 15)
BLANC = (255, 255, 255)
BLEU = (129, 78, 216)
ROUGE = (255, 0, 0)

BOUTON_COULEUR_CLAIR = (170, 170, 170)
BOUTON_COULEUR_FONCE = (100, 100, 100)

# Etoile
NOMBRE_ETOILES = 500

# Dimension Fenetre
FENETRE_LARGEUR = 1080
FENETRE_HAUTEUR = 720

# Dimension Vaisseau
VAISSEAU_LARGEUR = 70
VAISSEAU_HAUTEUR = 60
DEPLACEMENT_VAISSEAU = 7

# Vie
VIE_LARGEUR = 30
VIE_HAUTEUR = 25
NOMBRE_VIE = 3

# dimension planete
PLANETE_LARGEUR = 180
PLANETE_HAUTEUR = 180

# Pose Planete
POSE_PLANETE = (
'Planete1', 'Planete2', 'Planete3', 'Planete4', 'Planete5', 'Planete6', 'Planete7', 'Planete8', 'Planete9', 'Planete10',
'Planete11', 'Planete12', 'Planete13', 'Planete14', 'Planete15', 'Planete16')
POSE_VAISSEAU = ('vaisseau_jaune_sans_flamme', 'vaisseau_jaune_avec_flamme')

# Vitesse du Jeu
VITESSE_JEU = 3

# Info tir
MUNITIONS = 20
VITESSE_MISSILE = 1
AJOUT_MUNITION = 20

# Score et compteur
SCORE = 0
COMPTEUR_BOUCLE = 0
COMPTEUR_PAUSE = 0

TEMPS_AVANT_PAUSE = 0

# CONSTANTE POUR LE MENU
MENU = ['Jouer', 'Facile>', 'Quitter']
MENU_PAUSE = ['REPRENDRE', 'QUITTER']
CHOIX_MENU = 1
MENU_LONGUEUR = len(MENU)
MENU_PAUSE_LONGUEUR = len(MENU_PAUSE)
HAUTEUR = FENETRE_HAUTEUR / MENU_LONGUEUR
HAUTEUR_PAUSE = FENETRE_HAUTEUR / MENU_PAUSE_LONGUEUR
BOUTON_LARGEUR = 220
BOUTON_HAUTEUR = 41
BOUTON = 0

# DEFINITION PLANETE
LISTE_PLANETE = []


########FIN CONSTANTE#######

#Difficulté
niveau_difficulte = 0

#######FONCTIONS########

# Etoile
def cree_etoiles():
    etoile = []
    for x in range(NOMBRE_ETOILES):
        etoile.append([random.randint(0, FENETRE_LARGEUR), random.randint(0, FENETRE_HAUTEUR)])

    return etoile


def afficher_etoiles(ecran, vitesse_etoile, etoiles):
    for etoile in etoiles:
        pygame.draw.line(ecran, (255, 255, 255), (etoile[0], etoile[1]), (etoile[0], etoile[1]))

        etoile[1] = etoile[1] + vitesse_etoile
        if etoile[1] > FENETRE_HAUTEUR:
            etoile[1] = 0
            etoile[0] = random.randint(0, FENETRE_LARGEUR)


# Définition ENTITE #

def nouvelleEntite():
    return {
        'visible': False,
        'position': [0, 0],
        'image': None,
        'listeImage': {}
    }


def visible(entite):
    entite['visible'] = True


def invisible(entite):
    entite['visible'] = False


def estVisible(entite):
    return entite['visible']


def place(entite, x, y):
    entite['position'][0] = x
    entite['position'][1] = y


def position(entite):
    return entite['position']


def prendsPose(entite, nom):
    entite['image'] = entite['listeImage'][nom]
    visible(entite)


def ajouteImage(entite, nom, image):
    entite['listeImage'][nom] = image


def dessine(entite, ecran):
    ecran.blit(entite['image'], entite['position'])


# Fin ENTITE #

# AFFICHAGE
def affiche(entites, ecran):
    for objet in entites:
        if estVisible(objet):
            dessine(objet, ecran)


# Score et vie
def score():
    marquoir = police.render(str("Score: {}".format(int(round(SCORE, 0)))), True, BLANC)
    fenetre.blit(marquoir, (20, FENETRE_HAUTEUR // 12))


def vie():
    for x in range(0, NOMBRE_VIE + 1):
        image = pygame.transform.scale(vie_image, (VIE_LARGEUR, VIE_HAUTEUR))
        fenetre.blit(image, (FENETRE_LARGEUR - VIE_LARGEUR * x, FENETRE_HAUTEUR - VIE_HAUTEUR))


# Tir et Munition
def afficher_munition(nombre_munitions):
    if nombre_munitions == 0:

        munition = police.render(str(": {}".format(int(MUNITIONS))), True, ROUGE)
        fenetre.blit(munition, (35, FENETRE_HAUTEUR - 35))
        pygame.draw.rect(fenetre, BLANC, pygame.Rect(5, FENETRE_HAUTEUR - 40, munition.get_size()[0] + 40, 30), width=1)
        pygame.draw.circle(fenetre, BLEU, (17, FENETRE_HAUTEUR - 25), 10, width=1)
        pygame.draw.circle(fenetre, BLANC, (17, FENETRE_HAUTEUR - 25), 5)
    else:
        munition = police.render(str(": {}".format(int(MUNITIONS))), True, BLANC)
        fenetre.blit(munition, (35, FENETRE_HAUTEUR - 35))
        pygame.draw.rect(fenetre, BLANC, pygame.Rect(5, FENETRE_HAUTEUR - 40, munition.get_size()[0] + 40, 30), width=1)
        pygame.draw.circle(fenetre, BLEU, (17, FENETRE_HAUTEUR - 25), 10, width=1)
        pygame.draw.circle(fenetre, BLANC, (17, FENETRE_HAUTEUR - 25), 5)


def mru_1d(depart, temps_depart, vitesse, temps_maintenant):
    mru_1d = depart + (vitesse * (temps_maintenant - temps_depart))
    return (mru_1d)


# TODO A MODIFIER LES BALLES QUI DISPARESSENT

def dessiner_missile(missile, fenetre):

    temps_maintenant = pygame.time.get_ticks()

    for missile in missile:
        missile_vitesse = missile['vitesse_verticale']
        if COMPTEUR_PAUSE % 2 != 0:
            temps_maintenant = temps_maintenant - TEMPS_AVANT_PAUSE
            missile_vitesse = 0

        position = (missile['position_depart'][0],
                    mru_1d(missile['position_depart'][1],
                           missile['temps_depart'],
                           missile_vitesse,
                           temps_maintenant))

        pygame.draw.circle(fenetre, BLEU, list(map(int, position)), 10, width=1)
        pygame.draw.circle(fenetre, BLANC, list(map(int, position)), 5)
    return


def ajouter_missile(missile, position, temps_depart, vitesse):
    missile.append({'position_depart': position,
                    'temps_depart': temps_depart,
                    'vitesse_verticale': vitesse})
    return


# MENU#
def afficherBoutonMenu(Menu):
    for index, text in enumerate(Menu):

        text_afficher = POLICE_ECRITURE_BOUTON.render(text, True, BLANC)
        texte_largeur, texte_hauteur = text_afficher.get_size()

        if FENETRE_LARGEUR / 2 - BOUTON_LARGEUR // 2 <= mouse[
            0] <= FENETRE_LARGEUR / 2 + BOUTON_LARGEUR // 2 and FENETRE_HAUTEUR / MENU_LONGUEUR - BOUTON_HAUTEUR + (
                HAUTEUR / 2 * index) <= mouse[1] <= (FENETRE_HAUTEUR / MENU_LONGUEUR) + (
                HAUTEUR / 2 * index) or index == BOUTON:
            pygame.draw.rect(fenetre, BOUTON_COULEUR_CLAIR,
                             [(FENETRE_LARGEUR / 2) - BOUTON_LARGEUR // 2,
                              ((FENETRE_HAUTEUR / MENU_LONGUEUR) - BOUTON_HAUTEUR) + (HAUTEUR / 2 * index),
                              BOUTON_LARGEUR, 40])

        else:
            pygame.draw.rect(fenetre, BOUTON_COULEUR_FONCE,
                             [(FENETRE_LARGEUR / 2) - BOUTON_LARGEUR // 2,
                              ((FENETRE_HAUTEUR / MENU_LONGUEUR) - BOUTON_HAUTEUR) + (HAUTEUR / 2 * index),
                              BOUTON_LARGEUR, 40])

        fenetre.blit(text_afficher, ((FENETRE_LARGEUR / 2) - texte_largeur // 2,
                                     (FENETRE_HAUTEUR / MENU_LONGUEUR) - texte_hauteur + (HAUTEUR * index) / 2))


# Pause

def pause():
    afficherBoutonMenu(MENU_PAUSE)
    pygame.display.flip()
    temps.tick(60)

def difficulte (niveau_difficulte):
    if niveau_difficulte == 0:
        MENU = ['Jouer', 'Facile>', 'Quitter']
        AJOUT_MUNITION = 20
        MUNITIONS = 20
        VITESSE_JEU = 3
        VITESSE_MISSILE = 1
        NOMBRE_VIE = 3
        DEPLACEMENT_VAISSEAU = 7

    elif niveau_difficulte == 1:
        MENU = ['Jouer', '<Moyen>', 'Quitter']
        AJOUT_MUNITION = 15
        MUNITIONS = 15
        VITESSE_JEU = 3.5
        VITESSE_MISSILE = 0.8
        NOMBRE_VIE = 2
        DEPLACEMENT_VAISSEAU = 6
    elif niveau_difficulte == 2:
        MENU = ['Jouer', '<Difficile', 'Quitter']
        AJOUT_MUNITION = 10
        MUNITIONS = 10
        VITESSE_JEU = 4
        VITESSE_MISSILE = 0.6
        NOMBRE_VIE = 1
        DEPLACEMENT_VAISSEAU = 5

    return MENU,AJOUT_MUNITION, MUNITIONS,VITESSE_JEU,VITESSE_MISSILE,NOMBRE_VIE,DEPLACEMENT_VAISSEAU


#####FIN FONCTIONS######


# Changement de l'icône de jeu
game_icon = pygame.image.load("Images/vaisseau_jaune_avec_flamme.png")
pygame.display.set_icon(game_icon)

# Icone vie
vie_image = pygame.image.load('Images/vaisseau_rouge_avec_flamme.png')

# Initiamisation de pygame
pygame.init()

# Son
pygame.mixer.init()
piou = pygame.mixer.Sound("Son/piou.wav")
no_bullets = pygame.mixer.Sound("Son/no_bullets.wav")
print("[LOG] BRUITAGES CHARGE !")

# Missile
missile = []

# Création de la fenêtre
fenetre = pygame.display.set_mode((FENETRE_LARGEUR, FENETRE_HAUTEUR), pygame.RESIZABLE)
pygame.display.set_caption('Space Game')

# Création des entités
vaisseau = nouvelleEntite()

# CREATION PLANETE

# def spawn_planete()


# CHARGER TOUTES LES IMAGES #
print("[LOG] CHARGEMENT DES IMAGES")

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
                               ('trou_noir', 'trou_noir.png'),
                               ('ufo', 'ufo.png')):

    chemin = 'Images/' + nom_fichier
    image = pygame.image.load(chemin).convert_alpha(fenetre)
    image = pygame.transform.scale(image, (PLANETE_LARGEUR, PLANETE_HAUTEUR))

    for nom_image, nom_fichier in (('vaisseau_jaune_sans_flamme', 'vaisseau_jaune_sans_flamme.png'),
                                   ('vaisseau_jaune_avec_flamme', 'vaisseau_jaune_avec_flamme.png')):
        chemin = 'Images/' + nom_fichier
        image = pygame.image.load(chemin).convert_alpha(fenetre)
        image = pygame.transform.scale(image, (VAISSEAU_LARGEUR, VAISSEAU_HAUTEUR))
        ajouteImage(vaisseau, nom_image, image)

print("[LOG] TOUTES LES IMAGES SONT CHARGéES")
# FIN CHARGEMENT IMAGES #


# Postionement du vaisseau
place(vaisseau, (FENETRE_LARGEUR / 2) - VAISSEAU_LARGEUR / 2, FENETRE_HAUTEUR - VAISSEAU_HAUTEUR)

# Scene et planete
pose_planete = 0
scene = [vaisseau]

# Variable de jeu et Temps
fini = False
enintro = True
enjeu = False
temps = pygame.time.Clock()



# Police d'écriture#
police = pygame.font.SysFont('monospace', FENETRE_HAUTEUR // 40, True)
POLICE_ECRITURE_BOUTON = pygame.font.SysFont('monospace', 36)

# Création des étoiles
etoiles = cree_etoiles()

######CREATION DU MENU######
while enintro:
    temps_maintenant = pygame.time.get_ticks()
    prendsPose(vaisseau, POSE_VAISSEAU[0])
    place(vaisseau, (FENETRE_LARGEUR / 2) - VAISSEAU_LARGEUR / 2,
          FENETRE_HAUTEUR - VAISSEAU_HAUTEUR)
    evenement = pygame.event.get()
    for event in evenement:

        # Changement de taille d'écran
        if event.type == pygame.VIDEORESIZE:
            FENETRE_LARGEUR, FENETRE_HAUTEUR = fenetre.get_size()
            etoiles = cree_etoiles()
            place(vaisseau, (FENETRE_LARGEUR / 2) - VAISSEAU_LARGEUR / 2, FENETRE_HAUTEUR - VAISSEAU_HAUTEUR)

        # Quitter avec la croix
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Lancer le jeu
        if event.type == pygame.MOUSEBUTTONDOWN:
            if FENETRE_LARGEUR / 2 - BOUTON_LARGEUR // 2 <= mouse[
                0] <= FENETRE_LARGEUR / 2 + BOUTON_LARGEUR // 2 and FENETRE_HAUTEUR / MENU_LONGUEUR - BOUTON_HAUTEUR + (
                    HAUTEUR / 2 * 0) <= mouse[1] <= (FENETRE_HAUTEUR / MENU_LONGUEUR) + (HAUTEUR / 2 * 0):
                enintro = False
                enjeu = True
                SCORE = 0
                COMPTEUR_BOUCLE = 1



            # Quitter le jeu avec le bouton quitter
            if FENETRE_LARGEUR / 2 - BOUTON_LARGEUR // 2 <= mouse[
                0] <= FENETRE_LARGEUR / 2 + BOUTON_LARGEUR // 2 and FENETRE_HAUTEUR / MENU_LONGUEUR - BOUTON_HAUTEUR + (
                    HAUTEUR / 2 * 2) <= mouse[1] <= (FENETRE_HAUTEUR / MENU_LONGUEUR) + (HAUTEUR / 2 * 2):
                enjeu = False
                enintro = False
                NOMBRE_VIE = 0

        # Controle clavier
        if event.type == pygame.KEYDOWN:
            # incrémentation de la difficulté
            if event.key == pygame.K_RIGHT:
                if BOUTON == 1:
                    if niveau_difficulte < 2:
                        niveau_difficulte += 1
                        MENU, AJOUT_MUNITION, MUNITIONS, VITESSE_JEU, VITESSE_MISSILE,NOMBRE_VIE,DEPLACEMENT_VAISSEAU = difficulte(niveau_difficulte)
                    else:
                        None
            # Décrémentation de la difficulté
            if event.key == pygame.K_LEFT:
                if BOUTON == 1:
                    if niveau_difficulte > 0:
                        niveau_difficulte -= 1
                        MENU, AJOUT_MUNITION, MUNITIONS, VITESSE_JEU, VITESSE_MISSILE,NOMBRE_VIE,DEPLACEMENT_VAISSEAU = difficulte(niveau_difficulte)
                    else:
                        None
            if event.key == pygame.K_DOWN: #déplacement dans le menu
                if BOUTON < 2:
                    BOUTON += 1
                else:
                    BOUTON = 0

            if event.key == pygame.K_UP:#déplacement dans le menu
                if BOUTON < 1:
                    BOUTON = 2
                else:
                    BOUTON -= 1

            if event.key == pygame.K_RETURN: #lancer/quitter le jeu

                if BOUTON == 0 or BOUTON == 1:
                    enintro = False
                    enjeu = True
                    SCORE = 0
                    COMPTEUR_BOUCLE = 1

                if BOUTON == 2:
                    enjeu = False
                    enintro = False
                    NOMBRE_VIE = 0

    # Mécanique du jeu
    # Incrémentation du score et de la vitesse dans le menu
    if COMPTEUR_BOUCLE % 60 == 0 and COMPTEUR_BOUCLE < 3600:
        VITESSE_JEU += 0.10

    if COMPTEUR_BOUCLE % 60 == 0 and COMPTEUR_BOUCLE > 3600:
        None


    # Tir auto
    if COMPTEUR_BOUCLE % 150 == 0:
        if MUNITIONS > 0:
            ajouter_missile(missile, (position(vaisseau)[0] + VAISSEAU_LARGEUR / 2, position(vaisseau)[1]),
                            temps_maintenant,
                            -VITESSE_MISSILE)


    # Contrôle souris
    mouse = pygame.mouse.get_pos()

    # Affichage Vaisseau, etoile, vie, score
    prendsPose(vaisseau, POSE_VAISSEAU[0])
    fenetre.fill(ESPACE)
    afficher_etoiles(fenetre, VITESSE_JEU, etoiles)

    dessiner_missile(missile, fenetre)

    affiche(scene, fenetre)

    score()
    vie()
    afficher_munition(MUNITIONS)
    afficherBoutonMenu(MENU)
    pygame.display.flip()

    # Temps
    temps_maintenant = pygame.time.get_ticks()
    temps.tick(60)
    COMPTEUR_BOUCLE += 1

    #####FIN DU MENU#####


    #####BOUCLE DU JEU#####

    while NOMBRE_VIE > 0 and enjeu:

        temps_maintenant = pygame.time.get_ticks()
        prendsPose(vaisseau, POSE_VAISSEAU[0])

        evenement = pygame.event.get()
        for event in evenement:
            # Changement de l'écran
            if event.type == pygame.VIDEORESIZE:
                FENETRE_LARGEUR, FENETRE_HAUTEUR = fenetre.get_size()
                print(FENETRE_LARGEUR, FENETRE_HAUTEUR)
                etoiles = cree_etoiles()
                place(vaisseau, FENETRE_LARGEUR / 2, FENETRE_HAUTEUR - VAISSEAU_HAUTEUR)

            # Quitter avec la croix
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Tir
            if event.type == pygame.KEYDOWN:
                #Vérification qu'on est pas en pause
                if event.key == pygame.K_SPACE:
                    if COMPTEUR_PAUSE % 2 != 0:
                        None
                    else:
                        # Pas de munition
                        if MUNITIONS == 0:
                            no_bullets.play()
                        else:
                            # Tir de munitions
                            piou.play()
                            ajouter_missile(missile,
                                            (position(vaisseau)[0] + VAISSEAU_LARGEUR / 2, position(vaisseau)[1]),
                                            temps_maintenant,
                                            -VITESSE_MISSILE)
                            MUNITIONS -= 1

                # Touche dans le menu Pause
                if event.key == pygame.K_ESCAPE: #Quitter le menu
                    TEMPS_AVANT_PAUSE = pygame.time.get_ticks()
                    COMPTEUR_PAUSE += 1
                if event.key == pygame.K_DOWN: #Bas
                    if BOUTON < 1:
                        BOUTON += 1
                    else:
                        BOUTON = 0
                if event.key == pygame.K_UP:#Haut
                    if BOUTON > 1:
                        BOUTON -= 1
                    else:
                        BOUTON = 1
                if event.key == pygame.K_RETURN:#Enter
                    if BOUTON == 0:
                        COMPTEUR_PAUSE += 1
                    if BOUTON == 1: #Revenir au menu principal
                        COMPTEUR_PAUSE+=1
                        enintro = True
                        enjeu = False
                        #Reprise des paramètres de la difficulté choisie
                        MENU, AJOUT_MUNITION, MUNITIONS, VITESSE_JEU, VITESSE_MISSILE,NOMBRE_VIE,DEPLACEMENT_VAISSEAU = difficulte(niveau_difficulte)

        #Pause
        if COMPTEUR_PAUSE % 2 != 0:
            pause()
            pygame.display.flip()
        else:
            # Déplacement du vaisseau
            keys = pygame.key.get_pressed()

            # DROITE
            if keys[pygame.K_RIGHT]:
                if position(vaisseau)[0] + VAISSEAU_LARGEUR > FENETRE_LARGEUR:
                    None
                else:
                    prendsPose(vaisseau, POSE_VAISSEAU[1])
                    position_vaisseau = position(vaisseau)
                    place(vaisseau, position_vaisseau[0] + DEPLACEMENT_VAISSEAU, position_vaisseau[1])


            # GAUCHE
            if keys[pygame.K_LEFT]:
                if position(vaisseau)[0] <= 0:
                    prendsPose(vaisseau, POSE_VAISSEAU[1])
                    position_vaisseau = position(vaisseau)
                else:
                    prendsPose(vaisseau, POSE_VAISSEAU[1])
                    position_vaisseau = position(vaisseau)
                    place(vaisseau, position_vaisseau[0] - DEPLACEMENT_VAISSEAU, position_vaisseau[1])

            # BAS
            if keys[pygame.K_DOWN]:
                if position(vaisseau)[1] > FENETRE_HAUTEUR - VAISSEAU_HAUTEUR:
                    None
                else:
                    prendsPose(vaisseau, POSE_VAISSEAU[0])
                    position_vaisseau = position(vaisseau)
                    place(vaisseau, position_vaisseau[0], position_vaisseau[1] + DEPLACEMENT_VAISSEAU)

            # HAUT
            if keys[pygame.K_UP]:
                if position(vaisseau)[1] < 0:
                    None
                else:
                    prendsPose(vaisseau, POSE_VAISSEAU[1])
                    position_vaisseau = position(vaisseau)
                    place(vaisseau, position_vaisseau[0], position_vaisseau[1] - DEPLACEMENT_VAISSEAU)

            fenetre.fill(ESPACE)

            # Score, compteur, et missiles
            if COMPTEUR_BOUCLE % 60 == 0 and SCORE <= 1000:
                SCORE += 1
                VITESSE_JEU += 0.01

            if COMPTEUR_BOUCLE % 60 == 0 and SCORE > 1000:
                SCORE += 1

            if COMPTEUR_BOUCLE % 6000 == 0:
                MUNITIONS += AJOUT_MUNITION

            if NOMBRE_VIE == 0:
                enjeu = False
                enintro = True

            # Affichage
            dessiner_missile(missile, fenetre)
            afficher_etoiles(fenetre, VITESSE_JEU, etoiles)
            affiche(scene, fenetre)
            score()
            afficher_munition(MUNITIONS)
            vie()
            pygame.display.flip()

            # Temps
            temps.tick(60)
            COMPTEUR_BOUCLE += 1

pygame.display.quit()
pygame.quit()
exit()