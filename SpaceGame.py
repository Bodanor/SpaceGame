import pygame
import random
import math

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
NOMBRE_UFO = 5
NOMBRE_TROU_NOIR = 5

# Dimension Fenetre
FENETRE_LARGEUR = 1080
FENETRE_HAUTEUR = 720

# Dimension Vaisseau
VAISSEAU_LARGEUR = 70
VAISSEAU_HAUTEUR = 60
DEPLACEMENT_VAISSEAU = 7

# Dimension UFO
UFO_TAILLE = 80

# trou noir
TROU_NOIR_TAILLE = 80
FREQUENCE_APPARITION_TROU_NOIR = 1000

# Apparence vie
VIE_LARGEUR = 30
VIE_HAUTEUR = 25

# dimension planete
TAILLE_PLANETE = 180

# Pose Planete
POSE_PLANETE = (
    'Planete1', 'Planete2', 'Planete3', 'Planete4', 'Planete5', 'Planete6', 'Planete7', 'Planete8', 'Planete9',
    'Planete10',
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
COMPTEUR_COLLISION = 0
NOMBRE_VIE = 3
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

# DEFINITION ENTITE
LISTE_PLANETE = []
PLANETE_EN_LISTE = []
LISTE_UFO = []
UFO_EN_LISTE = []
LISTE_TROU_NOIR = []
TROU_NOIR_EN_LISTE = []
COULOIRS = []

########FIN CONSTANTE#######

# Difficulté
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
        'visible': True,
        'position': [0, 0],
        'image': None,
        'listeImage': {},
        'couloir': 0
    }


def visible(entite):
    entite['visible'] = True


def invisible(entite):
    entite['visible'] = False


def estVisible(entite):
    return entite['visible']


def place(entite, x, y, couloir):
    entite['position'][0] = x
    entite['position'][1] = y
    entite['couloir'] = couloir


def position(entite):
    return entite['position']


def afficherCouloir(entite):
    return entite['couloir']


def prendsPose(entite, nom):
    entite['image'] = entite['listeImage'][nom]


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


# Affichage du score et vies
def score():
    marquoir = police.render(str("Score: {}".format(int(round(SCORE, 0)))), True, BLANC)
    fenetre.blit(marquoir, (20, FENETRE_HAUTEUR // 12))


def vie():
    for x in range(0, NOMBRE_VIE + 1):
        image = pygame.transform.scale(vie_image, (VIE_LARGEUR, VIE_HAUTEUR))
        fenetre.blit(image, (FENETRE_LARGEUR - VIE_LARGEUR * x, FENETRE_HAUTEUR - VIE_HAUTEUR))


# Tir et Munition
def afficher_munition(nombre_munitions):
    if nombre_munitions == 0:  # Afficher les munitions en rouges quand il n'y en a plus

        munition = police.render(str(": {}".format(int(MUNITIONS))), True, ROUGE)
        fenetre.blit(munition, (35, FENETRE_HAUTEUR - 35))
        pygame.draw.rect(fenetre, BLANC, pygame.Rect(5, FENETRE_HAUTEUR - 40, munition.get_size()[0] + 40, 30), width=1)
        pygame.draw.circle(fenetre, BLEU, (17, FENETRE_HAUTEUR - 25), 10, width=1)
        pygame.draw.circle(fenetre, BLANC, (17, FENETRE_HAUTEUR - 25), 5)

    else:  # Afficher les munitions normalement
        munition = police.render(str(": {}".format(int(MUNITIONS))), True, BLANC)
        fenetre.blit(munition, (35, FENETRE_HAUTEUR - 35))
        pygame.draw.rect(fenetre, BLANC, pygame.Rect(5, FENETRE_HAUTEUR - 40, munition.get_size()[0] + 40, 30), width=1)
        pygame.draw.circle(fenetre, BLEU, (17, FENETRE_HAUTEUR - 25), 10, width=1)
        pygame.draw.circle(fenetre, BLANC, (17, FENETRE_HAUTEUR - 25), 5)


# MRU pour les missiles
def mru_1d(depart, temps_depart, vitesse, temps_maintenant, compteur_pause):
    if COMPTEUR_PAUSE % 2 != 0:
        return 0
    mru_1d = depart + (vitesse * (temps_maintenant - temps_depart))
    return (mru_1d)


# Affichage des missiles
def dessiner_missile(missile, fenetre):
    temps_maintenant = pygame.time.get_ticks()

    for missile in missile:
        missile_vitesse = missile['vitesse_verticale']

        if COMPTEUR_PAUSE % 2 != 0:  # stopper missiles pendant menu pause
            temps_maintenant = temps_maintenant - TEMPS_AVANT_PAUSE
            missile_vitesse = 0

        position = (missile['position_depart'][0],
                    mru_1d(missile['position_depart'][1],
                           missile['temps_depart'],
                           missile_vitesse,
                           temps_maintenant, COMPTEUR_PAUSE))

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

        # détection de la souris qui passe au dessus des boutons et les afficher en couleur clair si elle est au dessus
        if FENETRE_LARGEUR / 2 - BOUTON_LARGEUR // 2 <= mouse[
            0] <= FENETRE_LARGEUR / 2 + BOUTON_LARGEUR // 2 and FENETRE_HAUTEUR / MENU_LONGUEUR - BOUTON_HAUTEUR + (
                HAUTEUR / 2 * index) <= mouse[1] <= (FENETRE_HAUTEUR / MENU_LONGUEUR) + (
                HAUTEUR / 2 * index) or index == BOUTON:
            pygame.draw.rect(fenetre, BOUTON_COULEUR_CLAIR,
                             [(FENETRE_LARGEUR / 2) - BOUTON_LARGEUR // 2,
                              ((FENETRE_HAUTEUR / MENU_LONGUEUR) - BOUTON_HAUTEUR) + (HAUTEUR / 2 * index),
                              BOUTON_LARGEUR, 40])

        else:  # Afficher les boutons d'une couleur normale
            pygame.draw.rect(fenetre, BOUTON_COULEUR_FONCE,
                             [(FENETRE_LARGEUR / 2) - BOUTON_LARGEUR // 2,
                              ((FENETRE_HAUTEUR / MENU_LONGUEUR) - BOUTON_HAUTEUR) + (HAUTEUR / 2 * index),
                              BOUTON_LARGEUR, 40])

        fenetre.blit(text_afficher, ((FENETRE_LARGEUR / 2) - texte_largeur // 2,
                                     (FENETRE_HAUTEUR / MENU_LONGUEUR) - texte_hauteur + (HAUTEUR * index) / 2))


# Pause
def pause():
    for index, text in enumerate(MENU_PAUSE):

        text_afficher = POLICE_ECRITURE_BOUTON.render(text, True, BLANC)
        texte_largeur, texte_hauteur = text_afficher.get_size()

        # affichage des boutons de couleurs différentes selon celui qui est sélectionné
        if BOUTON == index or FENETRE_LARGEUR / 2 - BOUTON_LARGEUR // 2 <= mouse[
            0] <= FENETRE_LARGEUR / 2 + BOUTON_LARGEUR // 2 and FENETRE_HAUTEUR / MENU_LONGUEUR - BOUTON_HAUTEUR + (
                HAUTEUR / 2 * index) <= mouse[1] <= (FENETRE_HAUTEUR / MENU_LONGUEUR) + (
                HAUTEUR / 2 * index):
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

    pygame.display.flip()
    temps.tick(60)


def creation_couloirs_planete():
    for x in range(0, 5):
        COULOIRS.append(((FENETRE_LARGEUR / 5) * x, (FENETRE_LARGEUR / 5) * (x + 1)))


# GERER PLANETES
def spawn_planete():
    # Nombre de chances de spawn une planete
    random_timer = random.randint(0, 14)
    if random_timer == 3:
        # Pas plus de 4 planetes a l'ecran
        if len(PLANETE_EN_LISTE) < 4:
            couloir_random = random.randint(0, 4)
            planete_random = random.randint(0, 15)

            # Une seule planete par couloir
            if couloir_random in couloir_utilise:
                pass

            else:
                if LISTE_PLANETE[planete_random] in PLANETE_EN_LISTE:
                    pass
                else:
                    place(LISTE_PLANETE[planete_random], COULOIRS[couloir_random][0], -TAILLE_PLANETE, couloir_random)
                    PLANETE_EN_LISTE.append(LISTE_PLANETE[planete_random])
                    couloir_utilise.append(couloir_random)


def deplace_planete(vitesse_jeu):
    # Freeze des planete si en pause
    if COMPTEUR_PAUSE % 2 != 0:
        vitesse_jeu = 0
    else:

        for planete in PLANETE_EN_LISTE:
            x, y = position(planete)
            couloir_planete = afficherCouloir(planete)
            place(planete, x, y + vitesse_jeu, couloir_planete)
            # Respawn la planete si elle est en dessous de l'ecran (donc plus affichée)
            if position(planete)[1] > FENETRE_HAUTEUR:
                PLANETE_EN_LISTE.remove(planete)
                couloir_planete = afficherCouloir(planete)
                couloir_utilise.remove(couloir_planete)


# Gérer les collisions
def collision_entite(PLANETE_EN_LISTE,  nombre_vie, COMPTEUR_COLLISION, collision_active):
    compteur = COMPTEUR_COLLISION
    vies = nombre_vie
    collision = collision_active

    #Test si on vient de percuter un objet
    if collision:
        vies = nombre_vie
        for planete in PLANETE_EN_LISTE:

                #Calcul de la distance entre le centre des objets et des vaisseaux
                distance_vaisseau_planete = distance_objets(vaisseau,VAISSEAU_HAUTEUR,VAISSEAU_LARGEUR,planete,TAILLE_PLANETE,TAILLE_PLANETE)

                if distance_vaisseau_planete < 125:
                    vies = vies - 1
                    compteur = 180
                    collision = False
                    PLANETE_EN_LISTE.remove(planete)
                    couloir_planete = afficherCouloir(planete)
                    couloir_utilise.remove(couloir_planete)
                    return vies, compteur, collision

        for ufo in UFO_EN_LISTE:
            distance_vaisseau_UFO = distance_objets(vaisseau,VAISSEAU_LARGEUR,VAISSEAU_HAUTEUR,ufo,UFO_TAILLE,UFO_TAILLE)

            if distance_vaisseau_UFO < 70:
                vies = vies -1
                compteur = 180
                collision = False
                UFO_EN_LISTE.remove(ufo)
                couloir_ufo = afficherCouloir(ufo)
                couloir_utilise_ufo.remove(couloir_ufo)
                return vies, compteur, collision

        for trou_noir in TROU_NOIR_EN_LISTE:
            distance_vaisseau_trou_noir = distance_objets(trou_noir,TROU_NOIR_TAILLE,TROU_NOIR_TAILLE, vaisseau, VAISSEAU_LARGEUR, VAISSEAU_HAUTEUR )

            if distance_vaisseau_trou_noir < 70:
                vies = 0
                compteur = 180
                collision = False
                couloir_trou_noir = afficherCouloir(trou_noir)
                couloir_utilise_trou_noir.remove(couloir_trou_noir)
                return vies, compteur, collision
    else:
       return vies, compteur, collision
    return vies, compteur, collision

def distance_objets(objet1, HAUTEUR_OBJET1,LARGEUR_OBJET1, objet2, HAUTEUR_OBJET2,LARGEUR_OBJET2):
    centre_objet1_x = position(objet1)[0] + LARGEUR_OBJET1 / 2
    centre_objet1_y = position(objet1)[1] + HAUTEUR_OBJET1 / 2
    centre_objet2_x = position(objet2)[0] + LARGEUR_OBJET2 / 2
    centre_objet2_y = position(objet2)[1] + HAUTEUR_OBJET2 / 2
    distance = math.sqrt((centre_objet1_x - centre_objet2_x) ** 2 + (centre_objet1_y - centre_objet2_y) ** 2)

    return distance


# GERER UFO
def spawn_ufo():
    random_timer = random.randint(0, 14)
    if random_timer == 2:
        if len(UFO_EN_LISTE) < 1:
            couloir_random = random.randint(0, 4)
            ufo_random = random.randint(0, 4)
            hauteur_random = random.randint(-200, -80)
            if couloir_random in couloir_utilise_ufo:
                pass
            else:
                if LISTE_UFO[ufo_random] in UFO_EN_LISTE:
                    pass
                else:
                    # On verifie qu'il n'existe pas deja une planete a l'emplacement de l'UFO
                    for planete in PLANETE_EN_LISTE:

                        couloir_planete = afficherCouloir(planete)
                        if couloir_planete == couloir_random:
                            if hauteur_random > position(planete)[1] + TAILLE_PLANETE or hauteur_random + UFO_TAILLE < \
                                    position(planete)[1]:
                                place(LISTE_UFO[ufo_random], COULOIRS[couloir_random][0], hauteur_random,
                                      couloir_random)
                                UFO_EN_LISTE.append(LISTE_UFO[ufo_random])
                                couloir_utilise_ufo.append(couloir_random)


def deplace_ufo(vitesse_jeu):
    # Si en pause alors on freeze l'UFO
    if COMPTEUR_PAUSE % 2 != 0:
        vitesse_jeu = 0
    else:

        for ufo in UFO_EN_LISTE:
            x, y = position(ufo)
            couloir_ufo = afficherCouloir(ufo)
            place(ufo, x, y + vitesse_jeu, couloir_ufo)
            # Si l'UFO sort de la fenetre alors on met un nombre random de pixel avant une nouvelle apparition
            if position(ufo)[1] > FENETRE_HAUTEUR + random.randint(100, 9000):
                UFO_EN_LISTE.remove(ufo)
                couloir_ufo = afficherCouloir(ufo)
                couloir_utilise_ufo.remove(couloir_ufo)


###TROU NOIR#######
def spawn_trou_noir():
    random_timer = random.randint(0, FREQUENCE_APPARITION_TROU_NOIR)
    if random_timer == 2:
        if len(TROU_NOIR_EN_LISTE) < 1:
            couloir_random = random.randint(0, 4)
            trou_noir_random = random.randint(0, 4)
            hauteur_random = random.randint(-200, -80)
            if couloir_random in couloir_utilise_trou_noir:
                pass
            else:
                if LISTE_TROU_NOIR[trou_noir_random] in TROU_NOIR_EN_LISTE:
                    pass
                else:
                    # On verifie qu'il n'existe pas deja une planete a l'emplacement du trou noir
                    for planete in PLANETE_EN_LISTE:

                        couloir_planete = afficherCouloir(planete)
                        if couloir_planete == couloir_random:
                            if hauteur_random > position(planete)[
                                1] + TAILLE_PLANETE or hauteur_random + TROU_NOIR_TAILLE < position(planete)[1]:
                                place(LISTE_TROU_NOIR[trou_noir_random], COULOIRS[couloir_random][0], hauteur_random,
                                      couloir_random)
                                TROU_NOIR_EN_LISTE.append(LISTE_TROU_NOIR[trou_noir_random])
                                couloir_utilise_trou_noir.append(couloir_random)


def deplace_trou_noir(vitesse_jeu):
    # Si en pause alors on freeze le trou noir
    if COMPTEUR_PAUSE % 2 != 0:
        vitesse_jeu = 0
    else:

        for trou_noir in TROU_NOIR_EN_LISTE:
            x, y = position(trou_noir)
            couloir_trou_noir = afficherCouloir(trou_noir)
            place(trou_noir, x, y + vitesse_jeu, couloir_trou_noir)
            # Si l'UFO sort de la fenetre alors on met un nombre random de pixel avant une nouvelle apparition
            if position(trou_noir)[1] > FENETRE_HAUTEUR + random.randint(100, 9000):
                TROU_NOIR_EN_LISTE.remove(trou_noir)
                couloir_trou_noir = afficherCouloir(trou_noir)
                couloir_utilise_trou_noir.remove(couloir_trou_noir)


# Difficulté
def difficulte(niveau_difficulte):
    # Les valeures du jeu changent en fonction de la difficulté choisie
    if niveau_difficulte == 0:
        MENU = ['Jouer', 'Facile>', 'Quitter']
        AJOUT_MUNITION = 20
        MUNITIONS = 20
        VITESSE_JEU = 3
        VITESSE_MISSILE = 1
        NOMBRE_VIE = 3
        DEPLACEMENT_VAISSEAU = 7
        FREQUENCE_APPARITION_TROU_NOIR = 1000

    elif niveau_difficulte == 1:
        MENU = ['Jouer', '<Moyen>', 'Quitter']
        AJOUT_MUNITION = 15
        MUNITIONS = 15
        VITESSE_JEU = 3.5
        VITESSE_MISSILE = 0.8
        NOMBRE_VIE = 2
        DEPLACEMENT_VAISSEAU = 6
        FREQUENCE_APPARITION_TROU_NOIR = 500
    elif niveau_difficulte == 2:
        MENU = ['Jouer', '<Difficile', 'Quitter']
        AJOUT_MUNITION = 10
        MUNITIONS = 10
        VITESSE_JEU = 4
        VITESSE_MISSILE = 0.6
        NOMBRE_VIE = 1
        DEPLACEMENT_VAISSEAU = 5
        FREQUENCE_APPARITION_TROU_NOIR = 250

    return MENU, AJOUT_MUNITION, MUNITIONS, VITESSE_JEU, VITESSE_MISSILE, NOMBRE_VIE, DEPLACEMENT_VAISSEAU, FREQUENCE_APPARITION_TROU_NOIR


def bestscore(bestscore):
    try:
        with open('scoreboard.txt', 'r+') as fichier:
            meilleurscore = fichier.readline()
            meilleurscore = int(meilleurscore)
            if meilleurscore != bestscore:
                if meilleurscore < bestscore:
                    fichier.close()
                    fichier = open('scoreboard.txt', 'w+')
                    fichier.write("{}".format(bestscore))
                    fichier.close()
            if meilleurscore == "":
                fichier.write("0")
            marquoir = police.render(str("Meilleur score: {}".format(int(round(meilleurscore, 0)))), True, BLANC)
            fenetre.blit(marquoir, (20, FENETRE_HAUTEUR // 24))

    except FileNotFoundError:
        fichier = open('scoreboard.txt', 'w')
        fichier.write("0")
        fichier.close()

    except ValueError:
        pass


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

# CHARGER TOUTES LES IMAGES #
print("[LOG] CHARGEMENT DES IMAGES")
print("[LOG] CHARGEMENT DES PLANETES")
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

print("[LOG] TOUTES LES PLANETES SONT CHARGéES")
print("[LOG] CHARGEMENT DES VAISSEAUX")
for nom_image, nom_fichier in (('vaisseau_jaune_sans_flamme', 'vaisseau_jaune_sans_flamme.png'),
                               ('vaisseau_jaune_avec_flamme', 'vaisseau_jaune_avec_flamme.png')):
    chemin = 'Images/' + nom_fichier
    image = pygame.image.load(chemin).convert_alpha(fenetre)
    image = pygame.transform.scale(image, (VAISSEAU_LARGEUR, VAISSEAU_HAUTEUR))
    ajouteImage(vaisseau, nom_image, image)

print("[LOG] TOUT LES VAISSEAUX SONT CHARGéES")
print("[LOG] CHARGEMENT DE L'UFO")

for i in range(NOMBRE_UFO):
    chemin = 'Images/ufo.png'
    image = pygame.image.load(chemin).convert_alpha(fenetre)
    image = pygame.transform.scale(image, (UFO_TAILLE, UFO_TAILLE))
    ufo = nouvelleEntite()
    ajouteImage(ufo, 'ufo{}'.format(i), image)
    prendsPose(ufo, 'ufo{}'.format(i))
    LISTE_UFO.append(ufo)
print("[LOG] TOUT LES UFO SONT CHARGéES")

print("[LOG] CHARGEMENT DU TROU NOIR")

for i in range(NOMBRE_TROU_NOIR):
    chemin = 'Images/trou_noir.png'
    image = pygame.image.load(chemin).convert_alpha(fenetre)
    image = pygame.transform.scale(image, (TROU_NOIR_TAILLE, TROU_NOIR_TAILLE))
    trou_noir = nouvelleEntite()
    ajouteImage(trou_noir, 'trou_noir{}'.format(i), image)
    prendsPose(trou_noir, 'trou_noir{}'.format(i))
    LISTE_TROU_NOIR.append(trou_noir)
print("[LOG]  LES TROUS NOIR SONT CHARGéES")

print("[LOG] TOUTES LES IMAGES SONT CHARGéES")
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
etoiles = cree_etoiles()

creation_couloirs_planete()
couloir_utilise = []
couloir_utilise_ufo = []
couloir_utilise_trou_noir = []
collision_active = True
######CREATION DU MENU######
while enintro:
    visible(vaisseau)
    temps_maintenant = pygame.time.get_ticks()
    prendsPose(vaisseau, POSE_VAISSEAU[0])
    place(vaisseau, (FENETRE_LARGEUR / 2) - VAISSEAU_LARGEUR / 2,
          FENETRE_HAUTEUR - VAISSEAU_HAUTEUR, 0)
    evenement = pygame.event.get()
    for event in evenement:

        # Changement de taille d'écran
        if event.type == pygame.VIDEORESIZE:
            FENETRE_LARGEUR, FENETRE_HAUTEUR = fenetre.get_size()

            etoiles = cree_etoiles()
            place(vaisseau, (FENETRE_LARGEUR / 2) - VAISSEAU_LARGEUR / 2, FENETRE_HAUTEUR - VAISSEAU_HAUTEUR, 0)

        # Quitter avec la croix
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Lancer le jeu
        if event.type == pygame.MOUSEBUTTONDOWN:
            if FENETRE_LARGEUR / 2 - BOUTON_LARGEUR // 2 <= mouse[
                0] <= FENETRE_LARGEUR / 2 + BOUTON_LARGEUR // 2 and FENETRE_HAUTEUR / MENU_LONGUEUR - BOUTON_HAUTEUR + (
                    HAUTEUR / 2 * 0) <= mouse[1] <= (FENETRE_HAUTEUR / MENU_LONGUEUR) + (HAUTEUR / 2 * 0):

                if niveau_difficulte == 0:
                    VITESSE_JEU = 3
                elif niveau_difficulte == 1:
                    VITESSE_JEU = 3.5

                elif niveau_difficulte == 2:
                    VITESSE_JEU = 4

                enintro = False
                enjeu = True
                SCORE = 0
                COMPTEUR_BOUCLE = 1
                BOUTON = 0

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
                        MENU, AJOUT_MUNITION, MUNITIONS, VITESSE_JEU, VITESSE_MISSILE, NOMBRE_VIE, DEPLACEMENT_VAISSEAU, FREQUENCE_APPARITION_TROU_NOIR = difficulte(
                            niveau_difficulte)
                    else:
                        None
            # Décrémentation de la difficulté
            if event.key == pygame.K_LEFT:
                if BOUTON == 1:
                    if niveau_difficulte > 0:
                        niveau_difficulte -= 1
                        MENU, AJOUT_MUNITION, MUNITIONS, VITESSE_JEU, VITESSE_MISSILE, NOMBRE_VIE, DEPLACEMENT_VAISSEAU, FREQUENCE_APPARITION_TROU_NOIR = difficulte(
                            niveau_difficulte)
                    else:
                        None
            # déplacement dans le menu
            if event.key == pygame.K_DOWN:
                if BOUTON < 2:
                    BOUTON += 1
                else:
                    BOUTON = 0

            # déplacement dans le menu
            if event.key == pygame.K_UP:
                if BOUTON < 1:
                    BOUTON = 2
                else:
                    BOUTON -= 1

            # lancer/quitter le jeu
            if event.key == pygame.K_RETURN:

                # Jouer
                if BOUTON == 0 or BOUTON == 1:
                    if niveau_difficulte == 0:
                        VITESSE_JEU = 3
                    elif niveau_difficulte == 1:
                        VITESSE_JEU = 3.5

                    elif niveau_difficulte == 2:
                        VITESSE_JEU = 4

                    enintro = False
                    enjeu = True
                    SCORE = 0
                    COMPTEUR_BOUCLE = 1
                    BOUTON = 0

                # Quitter le programme
                if BOUTON == 2:
                    enjeu = False
                    enintro = False
                    NOMBRE_VIE = 0

    # Mécanique du jeu
    # Incrémentation de la vitesse du jeu dans le menu
    if COMPTEUR_BOUCLE % 60 == 0 and COMPTEUR_BOUCLE < 3600:
        VITESSE_JEU += 0.10

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
    mouse = pygame.mouse.get_pos()
    fenetre.fill(ESPACE)
    afficher_etoiles(fenetre, VITESSE_JEU, etoiles)
    dessiner_missile(missile, fenetre)

    # Affichage général
    affiche(scene, fenetre)

    score()
    bestscore(0)
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
    while enjeu:

        # Arrêter le jeu si plus de vie
        if NOMBRE_VIE == 0:
            bestscore(SCORE)
            SCORE = 0
            enintro = True
            enjeu = False
            couloir_utilise = []
            PLANETE_EN_LISTE = []
            UFO_EN_LISTE = []
            TROU_NOIR_EN_LISTE = []
            spawn_planete()
            deplace_planete(VITESSE_JEU)
            visible(vaisseau)
            COMPTEUR_COLLISION = 0

            # Reprise des paramètres de la difficulté choisie dans le menu
            MENU, AJOUT_MUNITION, MUNITIONS, VITESSE_JEU, VITESSE_MISSILE, NOMBRE_VIE, DEPLACEMENT_VAISSEAU, FREQUENCE_APPARITION_TROU_NOIR = difficulte(
                niveau_difficulte)

            fenetre.fill(ESPACE)

        # Spawn des entités ennemies
        spawn_planete()
        deplace_planete(VITESSE_JEU)
        spawn_ufo()
        spawn_trou_noir()
        deplace_ufo(VITESSE_JEU)
        deplace_trou_noir(VITESSE_JEU)
        temps_maintenant = pygame.time.get_ticks()
        prendsPose(vaisseau, POSE_VAISSEAU[0])

        evenement = pygame.event.get()
        mouse = pygame.mouse.get_pos()

        for event in evenement:
            # Changement de l'écran
            if event.type == pygame.VIDEORESIZE:

                position_x, position_y = position(vaisseau)
                place(vaisseau, (position_x / FENETRE_LARGEUR) * fenetre.get_size()[0],
                      (position_y / FENETRE_HAUTEUR) * fenetre.get_size()[1], 0)

                FENETRE_LARGEUR, FENETRE_HAUTEUR = fenetre.get_size()
                COULOIRS = []
                creation_couloirs_planete()
                for planete in PLANETE_EN_LISTE:
                    couloir = afficherCouloir(planete)
                    position_x, position_y = position(planete)

                    place(planete, COULOIRS[couloir][0], position_y, couloir)

                for ufo in UFO_EN_LISTE:
                    couloir = afficherCouloir(ufo)
                    position_x, position_y = position(ufo)

                    place(ufo, COULOIRS[couloir][0], position_y, couloir)

                for trou_noir in TROU_NOIR_EN_LISTE:
                    couloir = afficherCouloir(trou_noir)
                    position_x, position_y = position(trou_noir)

                    place(trou_noir, COULOIRS[couloir][0], position_y, couloir)

                etoiles = cree_etoiles()

            # Quitter avec la croix
            if event.type == pygame.QUIT:
                bestscore(SCORE)
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if FENETRE_LARGEUR / 2 - BOUTON_LARGEUR // 2 <= mouse[
                    0] <= FENETRE_LARGEUR / 2 + BOUTON_LARGEUR // 2 and FENETRE_HAUTEUR / MENU_LONGUEUR - BOUTON_HAUTEUR + (
                        HAUTEUR / 2 * 0) <= mouse[1] <= (FENETRE_HAUTEUR / MENU_LONGUEUR) + (HAUTEUR / 2 * 0):
                    COMPTEUR_PAUSE += 1

                if FENETRE_LARGEUR / 2 - BOUTON_LARGEUR // 2 <= mouse[
                    0] <= FENETRE_LARGEUR / 2 + BOUTON_LARGEUR // 2 and FENETRE_HAUTEUR / MENU_LONGUEUR - BOUTON_HAUTEUR + (
                        HAUTEUR / 2 * 1) <= mouse[1] <= (FENETRE_HAUTEUR / MENU_LONGUEUR) + (HAUTEUR / 2 * 1):
                    bestscore(SCORE)
                    COMPTEUR_PAUSE += 1
                    SCORE = 0
                    enintro = True
                    enjeu = False
                    couloir_utilise = []
                    PLANETE_EN_LISTE = []
                    spawn_planete()
                    deplace_planete(VITESSE_JEU)
                    visible(vaisseau)
                    COMPTEUR_COLLISION = 0
                    BOUTON = 0

            # Tir
            if event.type == pygame.KEYDOWN:
                # Vérification qu'on est pas en pause
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

                ######## Touche dans le menu Pause########
                # Quitter le menu pause avec echap
                if event.key == pygame.K_ESCAPE:
                    TEMPS_AVANT_PAUSE = pygame.time.get_ticks()
                    COMPTEUR_PAUSE += 1

                if COMPTEUR_PAUSE % 2 != 0:
                    # Bas
                    if event.key == pygame.K_DOWN:
                        if BOUTON < 1:
                            BOUTON += 1
                        else:
                            BOUTON = 0

                    # Haut
                    if event.key == pygame.K_UP:
                        if BOUTON == 1:
                            BOUTON = 0
                        elif BOUTON == 0:
                            BOUTON = 1

                ####Enter#####
                if event.key == pygame.K_RETURN:  # continuer le jeu
                    if BOUTON == 0:
                        COMPTEUR_PAUSE += 1

                    # Revenir au menu principal
                    if BOUTON == 1:
                        bestscore(SCORE)
                        COMPTEUR_PAUSE += 1
                        SCORE = 0
                        enintro = True
                        enjeu = False
                        couloir_utilise = []
                        PLANETE_EN_LISTE = []
                        spawn_planete()
                        deplace_planete(VITESSE_JEU)
                        visible(vaisseau)
                        COMPTEUR_COLLISION = 0
                        BOUTON = 0

                        # Reprise des paramètres de la difficulté choisie dans le menu
                        MENU, AJOUT_MUNITION, MUNITIONS, VITESSE_JEU, VITESSE_MISSILE, NOMBRE_VIE, DEPLACEMENT_VAISSEAU, FREQUENCE_APPARITION_TROU_NOIR = difficulte(
                            niveau_difficulte)
            ########FIN BOUTON PAUSE########

        ########Déplacement du vaisseau########
        if COMPTEUR_PAUSE % 2 != 0:  # Vérification si on est en pause
            pause()
            pygame.display.flip()
        else:
            keys = pygame.key.get_pressed()
            # DROITE
            if keys[pygame.K_RIGHT]:
                if position(vaisseau)[0] + VAISSEAU_LARGEUR > FENETRE_LARGEUR:
                    None
                else:
                    prendsPose(vaisseau, POSE_VAISSEAU[1])
                    position_vaisseau = position(vaisseau)
                    place(vaisseau, position_vaisseau[0] + DEPLACEMENT_VAISSEAU, position_vaisseau[1], 0)

            # GAUCHE
            if keys[pygame.K_LEFT]:
                if position(vaisseau)[0] <= 0:
                    prendsPose(vaisseau, POSE_VAISSEAU[1])
                    position_vaisseau = position(vaisseau)
                else:
                    prendsPose(vaisseau, POSE_VAISSEAU[1])
                    position_vaisseau = position(vaisseau)
                    place(vaisseau, position_vaisseau[0] - DEPLACEMENT_VAISSEAU, position_vaisseau[1], 0)

            # BAS
            if keys[pygame.K_DOWN]:
                if position(vaisseau)[1] > FENETRE_HAUTEUR - VAISSEAU_HAUTEUR:
                    None
                else:
                    prendsPose(vaisseau, POSE_VAISSEAU[0])
                    position_vaisseau = position(vaisseau)
                    place(vaisseau, position_vaisseau[0], position_vaisseau[1] + DEPLACEMENT_VAISSEAU, 0)

            # HAUT
            if keys[pygame.K_UP]:
                if position(vaisseau)[1] < 0:
                    None
                else:
                    prendsPose(vaisseau, POSE_VAISSEAU[1])
                    position_vaisseau = position(vaisseau)
                    place(vaisseau, position_vaisseau[0], position_vaisseau[1] - DEPLACEMENT_VAISSEAU, 0)
            ########FIN CONTROLE DU VAISSEAU#######

            # incrémentation du Score, compteur, et missiles
            if COMPTEUR_BOUCLE % 60 == 0 and SCORE <= 1000:
                SCORE += 1
                VITESSE_JEU += 0.05

            if COMPTEUR_BOUCLE % 60 == 0 and SCORE > 1000:
                SCORE += 1

            if COMPTEUR_BOUCLE % 6000 == 0:
                MUNITIONS += AJOUT_MUNITION

            if niveau_difficulte == 2:  # On regagne une vie tous les 200 scores si on est en difficile
                if COMPTEUR_BOUCLE % 12000 == 0:
                    NOMBRE_VIE += 1

            # Faire clignoter le vaisseau si collision
            if collision_active == False:

                if COMPTEUR_COLLISION == 180 or COMPTEUR_COLLISION == 150 or COMPTEUR_COLLISION == 120 or COMPTEUR_COLLISION == 90 or COMPTEUR_COLLISION == 60 or COMPTEUR_COLLISION == 30:
                    invisible(vaisseau)
                    print("invisible")
                if COMPTEUR_COLLISION == 165 or COMPTEUR_COLLISION == 135 or COMPTEUR_COLLISION == 105 or COMPTEUR_COLLISION == 75 or COMPTEUR_COLLISION == 45 or COMPTEUR_COLLISION == 15:
                    visible(vaisseau)
                    print("visible")
                if COMPTEUR_COLLISION == 0:
                    collision_active = True
                    visible(vaisseau)
                COMPTEUR_COLLISION -= 1

            # Affichage
            fenetre.fill(ESPACE)
            dessiner_missile(missile, fenetre)
            afficher_etoiles(fenetre, VITESSE_JEU, etoiles)
            affiche(scene, fenetre)
            affiche(PLANETE_EN_LISTE, fenetre)
            affiche(UFO_EN_LISTE, fenetre)
            affiche(TROU_NOIR_EN_LISTE, fenetre)
            score()
            afficher_munition(MUNITIONS)
            NOMBRE_VIE, COMPTEUR_COLLISION, collision_active = collision_entite(PLANETE_EN_LISTE, NOMBRE_VIE,
                                                                                COMPTEUR_COLLISION, collision_active)
            vie()
            pygame.display.flip()
            # Temps
            temps.tick(60)
            COMPTEUR_BOUCLE += 1

pygame.display.quit()
pygame.quit()
exit()