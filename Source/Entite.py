from Source.Variable import *

##### Définition ENTITE #####

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

def affiche(entites, ecran):
    for objet in entites:
        if estVisible(objet):
            dessine(objet, ecran)


##### Fin ENTITE ######

#####DEFINITION MISSILE#####

def nouvelleEntiteMissile():
    return {
        'visible': True,
        'position': [0, 0],
        'vitesse_missile' : VITESSE_MISSILE
    }
def visibleMissile(entite):
    entite['visible'] = True

def invisibleMissile(entite):
    entite['visible'] = False

def estVisibleMissile(entite):
    return entite['visible']

def placeMissile(entite, x, y):
    entite['position'][0] = x
    entite['position'][1] = y

def positionMissile(entite):
    return entite['position']

def dessineMissile(entite, ecran):
    ecran.blit(entite['image'], entite['position'])

def afficheMissile(entites, ecran):
    for missile in entites:
        if estVisible(missile):
            dessine(missile, ecran)

############################