from Source.Entite import *
import random

###DEPLACEMENT###
def deplace_planete(vitesse_jeu, COMPTEUR_PAUSE, PLANETE_EN_LISTE, couloir_utilise, FENETRE_HAUTEUR):
    # Freeze des planete si en pause
    if COMPTEUR_PAUSE % 2 != 0:

        VITESSE_JEU = 0
    else:


        #Déplacment des planètes
        for planete in PLANETE_EN_LISTE:
            x, y = position(planete)
            couloir_planete = afficherCouloir(planete)
            place(planete, x, y + vitesse_jeu, couloir_planete)
            # Respawn la planete si elle est en dessous de l'ecran (donc plus affichée)
            if position(planete)[1] > FENETRE_HAUTEUR:
                PLANETE_EN_LISTE.remove(planete)
                couloir_planete = afficherCouloir(planete)
                couloir_utilise.remove(couloir_planete)


def deplace_ufo(vitesse_jeu, couloir_utilise_ufo, COMPTEUR_PAUSE, UFO_EN_LISTE, FENETRE_HAUTEUR):
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

def deplace_trou_noir(vitesse_jeu, couloir_utilise_trou_noir, COMPTEUR_PAUSE, TROU_NOIR_EN_LISTE, FENETRE_HAUTEUR):
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
###FIN DEPLACEMENT###