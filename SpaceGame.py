import pygame
import random


#Variables
ESPACE = (0, 0, 15)
BLANC = (255,255,255)
BLEU = (129, 78, 216)
ROUGE = (255,0,0)


BOUTON_COULEUR_CLAIR = (170,170,170)
BOUTON_COULEUR_FONCE = (100,100,100)


NOMBRE_ETOILES = 500

FENETRE_LARGEUR = 1080
FENETRE_HAUTEUR = 720

VAISSEAU_LARGEUR = 70
VAISSEAU_HAUTEUR = 60

VIE_LARGEUR = 30
VIE_HAUTEUR = 25
NOMBRE_VIE = 3

PLANETE_LARGEUR = 180
PLANETE_HAUTEUR = 180

POSE_PLANETE = ('Planete1', 'Planete2','Planete3', 'Planete4','Planete5', 'Planete6','Planete7', 'Planete8','Planete9', 'Planete10','Planete11', 'Planete12','Planete13', 'Planete14','Planete15', 'Planete16')
POSE_VAISSEAU = ('vaisseau_sans_flamme', 'vaisseau_avec_flamme')

VITESSE_JEU = 3

MUNITIONS = 15
vitesse_missile = 0.6


SCORE = 0
COMPTEUR_BOUCLE = 0



vie_image = pygame.image.load('Images/vaisseau_jaune_avec_flamme.png')

#Fonctions

def cree_etoiles():

    etoile = []
    for x in range(NOMBRE_ETOILES):
        etoile.append([random.randint(0,FENETRE_LARGEUR), random.randint(0, FENETRE_HAUTEUR)])

    return etoile


def afficher_etoiles(ecran, vitesse_etoile, etoiles):

    for etoile in etoiles:
        pygame.draw.line(ecran, (255,255,255), (etoile[0], etoile[1]), (etoile[0], etoile[1]))

        etoile[1] = etoile[1] + vitesse_etoile
        if etoile[1] > FENETRE_HAUTEUR:
            etoile[1] = 0
            etoile[0] = random.randint(0, FENETRE_LARGEUR)

##### Définition ENTITE #####

def nouvelleEntite():
    return {
        'visible':False,
        'position': [0, 0],
        'image' : None,
        'listeImage' : {}
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
def ajouteImage(entite,nom ,image):
    entite['listeImage'][nom] = image

def dessine(entite, ecran):
    ecran.blit(entite['image'], entite['position'])

##### Fin ENTITE #####


def affiche(entites, ecran):
    for objet in entites:
        if estVisible(objet):
            dessine(objet, ecran)


#Score et vie
def score():
    marquoir = police.render(str("Score: {}".format(int(round(SCORE, 0)))), True, BLANC)
    fenetre.blit(marquoir, (20, FENETRE_HAUTEUR // 12))

def afficher_munition(nombre_munitions):
    if nombre_munitions == 0:

        munition = police.render(str(": {}".format(int(MUNITIONS))), True, ROUGE)
        fenetre.blit(munition, (35, FENETRE_HAUTEUR - 35))

        pygame.draw.rect(fenetre, BLANC, pygame.Rect(5, FENETRE_HAUTEUR - 40, munition.get_size()[0]+40, 30), width=1)
        pygame.draw.circle(fenetre, BLEU,(17, FENETRE_HAUTEUR - 25), 10, width=1)
        pygame.draw.circle(fenetre, BLANC, (17, FENETRE_HAUTEUR - 25), 5)
    else:
        munition = police.render(str(": {}".format(int(MUNITIONS))), True, BLANC)
        fenetre.blit(munition, (35, FENETRE_HAUTEUR-35))

        pygame.draw.rect(fenetre, BLANC, pygame.Rect(5, FENETRE_HAUTEUR - 40, munition.get_size()[0]+40, 30), width=1)
        pygame.draw.circle(fenetre, BLEU, (17, FENETRE_HAUTEUR - 25), 10, width=1)
        pygame.draw.circle(fenetre, BLANC, (17, FENETRE_HAUTEUR - 25), 5)

def vie():

    for x in range(0,NOMBRE_VIE+1):
        image = pygame.transform.scale(vie_image, (VIE_LARGEUR,VIE_HAUTEUR))
        fenetre.blit(image, (FENETRE_LARGEUR-VIE_LARGEUR*x,FENETRE_HAUTEUR-VIE_HAUTEUR))

#Tir
def mru_1d(depart, temps_depart, vitesse, temps_maintenant):
    mru_1d = depart + (vitesse * (temps_maintenant - temps_depart))
    return (mru_1d)


def dessiner_missile(missile, fenetre):
    for missile in missile:
        position = (missile['position_depart'][0],
                    mru_1d(missile['position_depart'][1],
                           missile['temps_depart'],
                           missile['vitesse_verticale'],
                           pygame.time.get_ticks()))
        pygame.draw.circle(fenetre, BLEU, list(map(int, position)), 10, width=1)
        pygame.draw.circle(fenetre, BLANC, list(map(int, position)), 5)
    return

def ajouter_missile(missile, position, temps_depart, vitesse):
    missile.append({'position_depart': position,
                   'temps_depart': temps_depart,
                   'vitesse_verticale': vitesse})
    return


#Menu
def afficherBoutonMenu(Menu):

    menu_longueur = len(Menu)
    hauteur = FENETRE_HAUTEUR / menu_longueur

    for index, text in enumerate(Menu):

        text_afficher = POLICE_ECRITURE_BOUTON.render(text, True, BLANC)
        texte_largeur, texte_hauteur = text_afficher.get_size()

        if FENETRE_LARGEUR / 2 - texte_largeur//2 <= mouse[0] <= FENETRE_LARGEUR / 2 + texte_largeur//2 and FENETRE_HAUTEUR / menu_longueur - texte_hauteur + (hauteur / 2 * index) <= mouse[1] <= (FENETRE_HAUTEUR / menu_longueur) + (hauteur / 2 * index):
            pygame.draw.rect(fenetre, BOUTON_COULEUR_CLAIR,
                             [(FENETRE_LARGEUR / 2) - texte_largeur//2, ((FENETRE_HAUTEUR / menu_longueur) - texte_hauteur) + (hauteur / 2 * index), texte_largeur, 40])

        else:
            pygame.draw.rect(fenetre, BOUTON_COULEUR_FONCE,
                             [(FENETRE_LARGEUR / 2) - texte_largeur//2, ((FENETRE_HAUTEUR / menu_longueur) - texte_hauteur)+ (hauteur / 2 * index), texte_largeur, 40])


        fenetre.blit(text_afficher, ((FENETRE_LARGEUR / 2) - texte_largeur// 2,(FENETRE_HAUTEUR /menu_longueur) -  texte_hauteur + (hauteur * index) / 2))






    return (True, False, 0, 60, 15)

#Changement de l'icône de jeu
game_icon = pygame.image.load("Images/vaisseau_avec_flamme.png")
pygame.display.set_icon(game_icon)

pygame.init()

#Son
pygame.mixer.init()
piou = pygame.mixer.Sound("Son/piou.wav")
no_bullets = pygame.mixer.Sound("Son/no_bullets.wav")


print("[LOG] BRUITAGES CHARGE !")
missile = []

#Création de la fenêtre

fenetre = pygame.display.set_mode((FENETRE_LARGEUR, FENETRE_HAUTEUR), pygame.RESIZABLE)
pygame.display.set_caption('Space Game')

vaisseau = nouvelleEntite()
planetes = nouvelleEntite()


print("[LOG] CHARGEMENT DES IMAGES")
#CHARGER TOUTES LES IMAGES :
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
                               ('trou_noir','trou_noir.png'),
                               ('ufo','ufo.png')):

    chemin = 'Images/' + nom_fichier
    image = pygame.image.load(chemin).convert_alpha(fenetre)
    image = pygame.transform.scale(image, (PLANETE_LARGEUR, PLANETE_HAUTEUR))
    ajouteImage(planetes,nom_image,image)

    for nom_image, nom_fichier in (('vaisseau_sans_flamme', 'vaisseau_sans_flamme.png'),
                               ('vaisseau_avec_flamme', 'vaisseau_avec_flamme.png')):

        chemin = 'Images/' + nom_fichier
        image = pygame.image.load(chemin).convert_alpha(fenetre)
        image = pygame.transform.scale(image, (VAISSEAU_LARGEUR, VAISSEAU_HAUTEUR))
        ajouteImage(vaisseau,nom_image,image)


# FIN CHARGEMENT IMAGES <--

print("[LOG] TOUTES LES IMAGES SONT CHARGéES")




place(vaisseau, (FENETRE_LARGEUR/2) -VAISSEAU_LARGEUR/2 , FENETRE_HAUTEUR-VAISSEAU_HAUTEUR)

pose_planete = 0

scene = [vaisseau, planetes]
fini = False
enintro = True
enjeu = False
temps = pygame.time.Clock()

police = pygame.font.SysFont('monospace', FENETRE_HAUTEUR//40, True)
POLICE_ECRITURE_BOUTON = pygame.font.SysFont('monospace',36)

etoiles = cree_etoiles()




###CREATION DU MENU###

MENU = ['Jouer','Difficulté','Quitter']
CHOIX_MENU = 1


while enintro:
    temps_maintenant = pygame.time.get_ticks()

    prendsPose(vaisseau, POSE_VAISSEAU[0])

    evenement = pygame.event.get()
    for event in evenement:
        # Changement de taille d'écran
        if event.type == pygame.VIDEORESIZE:
            FENETRE_LARGEUR, FENETRE_HAUTEUR = fenetre.get_size()
            etoiles = cree_etoiles()
            place(vaisseau, (FENETRE_LARGEUR / 2) - VAISSEAU_LARGEUR / 2, FENETRE_HAUTEUR - VAISSEAU_HAUTEUR)
        if event.type == pygame.QUIT:
            enintro = False
            NOMBRE_VIE = 0

            # Lancer le jeu
        if event.type == pygame.MOUSEBUTTONDOWN:
            if FENETRE_LARGEUR / 2 - texte_largeur // 2 <= mouse[
                0] <= FENETRE_LARGEUR / 2 + texte_largeur // 2 and FENETRE_HAUTEUR / menu_longueur - texte_hauteur + (
                    hauteur / 2 * index) <= mouse[1] <= (FENETRE_HAUTEUR / menu_longueur) + (hauteur / 2 * index):
                enintro = False
                enjeu = True
                SCORE = 0
                COMPTEUR_BOUCLE = 0
                MUNITIONS = 15
                return (enintro, enjeu, SCORE, COMPTEUR_BOUCLE, MUNITIONS)

            # Quitter le jeu
            if FENETRE_LARGEUR / 2 - texte_largeur // 2 <= mouse[
                0] <= FENETRE_LARGEUR / 2 + texte_largeur // 2 and FENETRE_HAUTEUR / menu_longueur - texte_hauteur + (
                    hauteur / 2 * index) <= mouse[1] <= (FENETRE_HAUTEUR / menu_longueur) + (hauteur / 2 * index):
                enintro = False
                enjeu = False
                NOMBRE_VIE = 0

                return (False, False, 0, 0, 0)
        # Controle clavier
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                None
            if event.key == pygame.K_UP:
                None


    temps_maintenant = pygame.time.get_ticks()
    prendsPose(vaisseau, POSE_VAISSEAU[0])
    fenetre.fill(ESPACE)
    mouse = pygame.mouse.get_pos()
    COMPTEUR_BOUCLE += 1

#Mécanique du jeu
    if COMPTEUR_BOUCLE % 60 == 0 and SCORE <= 100:
        SCORE += 1
        VITESSE_JEU += 0.10

    if COMPTEUR_BOUCLE % 60 == 0 and SCORE > 100:
        SCORE += 1

    if COMPTEUR_BOUCLE % 6000 == 0:
        MUNITIONS += 10
#Tir auto
    if COMPTEUR_BOUCLE % 120 == 0:
        if MUNITIONS > 0:
            ajouter_missile(missile, (position(vaisseau)[0] + VAISSEAU_LARGEUR / 2, position(vaisseau)[1]),
                            temps_maintenant,
                            -vitesse_missile)
            MUNITIONS -= 1

    dessiner_missile(missile, fenetre)

    afficher_etoiles(fenetre, VITESSE_JEU, etoiles)

    affiche(scene, fenetre)
    score()
    afficher_munition(MUNITIONS)
    vie()
    enintro, enjeu, SCORE, COMPTEUR_BOUCLE, MUNITIONS = afficherBoutonMenu(MENU)
    pygame.display.flip()

    temps.tick(60)
#####FIN DU MENU#####



#####BOUCLE DU JEU#####

    while enjeu:
        if NOMBRE_VIE > 0:

            temps_maintenant = pygame.time.get_ticks()

            prendsPose(vaisseau, POSE_VAISSEAU[0])

            evenement = pygame.event.get()
            for event in evenement:
                #Changement de l'écran
                if event.type == pygame.VIDEORESIZE:
                    FENETRE_LARGEUR, FENETRE_HAUTEUR = fenetre.get_size()
                    etoiles = cree_etoiles()
                    place(vaisseau, FENETRE_LARGEUR / 2, FENETRE_HAUTEUR - VAISSEAU_HAUTEUR)
                if event.type == pygame.QUIT:
                    enjeu = False
                    NOMBRE_VIE = 0

            #Tir
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if MUNITIONS == 0:
                            no_bullets.play()
                        else:
                            piou.play()
                            ajouter_missile(missile, (position(vaisseau)[0]+VAISSEAU_LARGEUR/2 , position(vaisseau)[1]), temps_maintenant,
                                            -vitesse_missile)
                            MUNITIONS -=1



            #Déplacement du vaisseau
            keys = pygame.key.get_pressed()

            if keys[pygame.K_RIGHT]:
                if position(vaisseau)[0] + VAISSEAU_LARGEUR >FENETRE_LARGEUR:
                    None
                else:
                    prendsPose(vaisseau, POSE_VAISSEAU[1])
                    position_vaisseau = position(vaisseau)
                    place(vaisseau, position_vaisseau[0] + 5, position_vaisseau[1])


            if keys[pygame.K_LEFT]:
                if position(vaisseau)[0] == 0:
                    None
                else:
                    prendsPose(vaisseau, POSE_VAISSEAU[1])
                    position_vaisseau = position(vaisseau)
                    place(vaisseau, position_vaisseau[0] - 5, position_vaisseau[1])

            if keys[pygame.K_DOWN]:
                if position(vaisseau)[1] > FENETRE_HAUTEUR - VAISSEAU_HAUTEUR :
                    None
                else:
                    prendsPose(vaisseau, POSE_VAISSEAU[0])
                    position_vaisseau = position(vaisseau)
                    place(vaisseau, position_vaisseau[0], position_vaisseau[1] + 5)


            if keys[pygame.K_UP]:
                if position(vaisseau)[1] < 0:
                    None
                else:
                    prendsPose(vaisseau, POSE_VAISSEAU[1])
                    position_vaisseau = position(vaisseau)
                    place(vaisseau, position_vaisseau[0], position_vaisseau[1] - 5)

            fenetre.fill(ESPACE)

        #Score, compteur, et missiles
            COMPTEUR_BOUCLE +=1

            if COMPTEUR_BOUCLE % 60 == 0 and SCORE <= 1000:
                SCORE += 1
                VITESSE_JEU += 0.01

            if COMPTEUR_BOUCLE % 60 == 0 and SCORE > 1000 :
                SCORE += 1


            if COMPTEUR_BOUCLE % 6000 == 0:
                MUNITIONS += 10

            dessiner_missile(missile, fenetre)

            afficher_etoiles(fenetre, VITESSE_JEU, etoiles)



            affiche(scene, fenetre)
            score()
            afficher_munition(MUNITIONS)
            vie()
            pygame.display.flip()



            temps.tick(60)

pygame.display.quit()
pygame.quit()
exit()