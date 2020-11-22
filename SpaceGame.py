import pygame
import random

ESPACE = (0, 0, 15)
BLANC = (255,255,255)
NOMBRE_ETOILES = 500
FENETRE_LARGEUR = 1080
FENETRE_HAUTEUR = 720

VAISSEAU_LARGEUR = 70
VAISSEAU_HAUTEUR = 60

VIE_LARGEUR = 30
VIE_HAUTEUR = 25

PLANETE_LARGEUR = 180
PLANETE_HAUTEUR = 180

POSE_PLANETE = ('Planete1', 'Planete2','Planete3', 'Planete4','Planete5', 'Planete6','Planete7', 'Planete8','Planete9', 'Planete10','Planete11', 'Planete12','Planete13', 'Planete14','Planete15', 'Planete16')
POSE_VAISSEAU = ('vaisseau_sans_flamme', 'vaisseau_avec_flamme')

VITESSE_JEU = 3

MUNITIONS = 10
NOMBRE_VIE = 3

SCORE = 0
COMPTEUR_BOUCLE = 0

vitesse_missile = 0.6



etoiles = [
        [random.randint(0, FENETRE_LARGEUR), random.randint(0, FENETRE_HAUTEUR)]
        for x in range(NOMBRE_ETOILES)
    ]



def afficher_etoiles(ecran, vitesse_etoile):
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
    marquoir = police.render(str(int(round(SCORE, 0))), True, BLANC)
    fenetre.blit(marquoir, (20, FENETRE_HAUTEUR // 12))

def afficher_munition():
    munition = police.render(str(int(MUNITIONS)), True, BLANC)
    fenetre.blit(munition, (20, FENETRE_HAUTEUR-35))

def vie():

    for x in range(0,NOMBRE_VIE+1):
        vie_image = pygame.image.load('Images/vaisseau_avec_flamme.png')
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

        pygame.draw.circle(fenetre, BLANC, list(map(int, position)), 5)
    return

def ajouter_missile(missile, position, temps_depart, vitesse):
    missile.append({'position_depart': position,
                   'temps_depart': temps_depart,
                   'vitesse_verticale': vitesse})
    return



game_icon = pygame.image.load("Images/vaisseau_avec_flamme.png")
pygame.display.set_icon(game_icon)

pygame.init()

missile = []

fenetre_taille = (FENETRE_LARGEUR, FENETRE_HAUTEUR)
fenetre = pygame.display.set_mode(fenetre_taille)
pygame.display.set_caption('Space Game️')

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


place(vaisseau, FENETRE_LARGEUR/2, FENETRE_HAUTEUR-VAISSEAU_HAUTEUR)

pose_planete = 0

scene = [vaisseau, planetes]
attente = 0
fini = False
temps = pygame.time.Clock()

police = pygame.font.SysFont('monospace', FENETRE_HAUTEUR//20, True)


while NOMBRE_VIE>0:

    temps_maintenant = pygame.time.get_ticks()

    prendsPose(vaisseau, POSE_VAISSEAU[0])

    evenement = pygame.event.get()
    for event in evenement:
        if event.type == pygame.QUIT:
            fini = True
            NOMBRE_VIE = 0
    #Tir
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if MUNITIONS > 0:
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
        if position(vaisseau)[1] > FENETRE_HAUTEUR - VAISSEAU_HAUTEUR:
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

#Score et compteur
    score()
    afficher_munition()
    vie()
    COMPTEUR_BOUCLE +=1

    if COMPTEUR_BOUCLE % 60 == 0 and SCORE <= 1000 :
        SCORE += 1
        VITESSE_JEU += 0.01

    if COMPTEUR_BOUCLE % 60 == 0 and SCORE > 10 :
        SCORE += 1
        NOMBRE_VIE-=1

    if COMPTEUR_BOUCLE % 6000 == 0:
        MUNITIONS += 10

    dessiner_missile(missile, fenetre)
    afficher_etoiles(fenetre, VITESSE_JEU)

    affiche(scene, fenetre)

    pygame.display.flip()



    temps.tick(60)


pygame.display.quit()
pygame.quit()
exit()