import pygame
import random

ESPACE = (0, 0, 15)
NOMBRE_ETOILES = 500
FENETRE_LARGEUR = 1080
FENETRE_HAUTEUR = 720

VAISSEAU_LARGEUR = 60
VAISSEAU_HAUTEUR = 51

POSE_PLANETE = ('Planete1', 'Planete2','Planete3', 'Planete4','Planete5', 'Planete6','Planete7', 'Planete8','Planete9', 'Planete10','Planete11', 'Planete12','Planete13', 'Planete14','Planete15', 'Planete16')
POSE_VAISSEAU = ('vaisseau_sans_flamme', 'vaisseau_avec_flamme')

etoiles = [
        [random.randint(0, FENETRE_LARGEUR), random.randint(0, FENETRE_HAUTEUR)]
        for x in range(NOMBRE_ETOILES)
    ]

def afficher_etoiles(ecran):
    for etoile in etoiles:
        pygame.draw.line(ecran, (255,255,255), (etoile[0], etoile[1]), (etoile[0], etoile[1]))

        etoile[1] = etoile[1] + 1
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
    place(planetes, random.randint(0, FENETRE_LARGEUR), random.randint(0, FENETRE_HAUTEUR))
    ecran.blit(entite['image'], entite['position'])

##### Fin ENTITE #####


def affiche(entites, ecran):
    for objet in entites:
        if estVisible(objet):
            dessine(objet, ecran)


pygame.init()

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
                               ('Planete16', 'planete16.png')):

    chemin = 'Images/' + nom_fichier
    image = pygame.image.load(chemin).convert_alpha(fenetre)
    image = pygame.transform.scale(image, (VAISSEAU_LARGEUR, VAISSEAU_HAUTEUR))
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
while not fini:

    prendsPose(vaisseau, POSE_VAISSEAU[0])


    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            fini = True

    #Déplacement VAISSEAU ( NE PAS INCLURE DES PRESSAGES DE TOUCHES) :
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

    afficher_etoiles(fenetre)

    pose_planete = random.randint(0, len(POSE_PLANETE) - 1)
    prendsPose(planetes, POSE_PLANETE[pose_planete])

    #SAVOIR SI TOUTES LES PLANETES SONT AFFICHées
    affiche(scene, fenetre)
    pygame.display.flip()


    temps.tick(60)

pygame.display.quit()
pygame.quit()
exit()