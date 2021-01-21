from Entite import *
import pygame
import random

##### Tir et Munition #####

#Ajouter les missiles
def ajouter_missile(position):

    missiles = nouvelleEntiteMissile()
    placeMissile(missiles, position[0], position[1])
    missile.append(missiles)

    return

# DEPLACEMENT DES MISSILES
def deplace_missile(missile, position_missile, vitesse_missile):
    position_y = position_missile[1] - vitesse_missile
    placeMissile(missile, position_missile[0], position_y)

#AFFICHAGE DES MISSILES
def dessine_missile(fenetre, vitesse_missile):


    for missiles in missile:
        COULEUR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if estVisible(missiles):
            if positionMissile(missiles)[1] < 0:
                missile.remove(missiles)
            deplace_missile(missiles, positionMissile(missiles), vitesse_missile)

            pygame.draw.circle(fenetre, COULEUR, list(map(int,positionMissile(missiles))), 7)
            pygame.draw.circle(fenetre, COULEUR, list(map(int, positionMissile(missiles))), 10, width=1)
            pygame.draw.circle(fenetre, BLANC, list(map(int, positionMissile(missiles))), 5)


## MISSILE POUR L'UFO ##

# Déplacement des missiles de l'alien
def deplace_missile_ufo(missile_ufo, position_missile, vitesse_missile):
    position_y = position_missile[1] + vitesse_missile
    placeMissile(missile_ufo, position_missile[0], position_y)


#Ajouter des missiles pour l'alien
def ajouter_missile_ufo(position, MISSILE_UFO_EN_LISTE):

    missiles_ufo = nouvelleEntiteMissile()
    placeMissile(missiles_ufo, position[0] + UFO_TAILLE/2, position[1]+ UFO_TAILLE/2)
    MISSILE_UFO_EN_LISTE.append(missiles_ufo)
    return

#Dessiner les missiles de l'alien
def dessine_missile_ufo(fenetre, MISSILE_UFO_EN_LISTE, VITESSE_JEU):

        for missiles_ufo in MISSILE_UFO_EN_LISTE:
            if estVisible(missiles_ufo):


                deplace_missile_ufo(missiles_ufo, positionMissile(missiles_ufo) , VITESSE_JEU*2)
                pygame.draw.circle(fenetre, ROUGE, list(map(int, positionMissile(missiles_ufo))), 7)
                pygame.draw.circle(fenetre, ROUGE, list(map(int, positionMissile(missiles_ufo))), 10, width=1)
                pygame.draw.circle(fenetre, BLANC, list(map(int, positionMissile(missiles_ufo))), 5)

            if positionMissile(missiles_ufo)[1] > FENETRE_HAUTEUR:
                MISSILE_UFO_EN_LISTE.remove(missiles_ufo)

#L'UFO tire selon la fréquence (la fréquence varie selon la difficulté)
def tir_random_ufo(MISSILE_UFO_EN_LISTE, UFO_EN_LISTE, COMPTEUR_BOUCLE, FREQUENCE_TIR):
    for ufo in UFO_EN_LISTE:

            if COMPTEUR_BOUCLE % FREQUENCE_TIR == 0:
                ajouter_missile_ufo(position(ufo), MISSILE_UFO_EN_LISTE)

## FIN MISSILE UFO ##

##### FIN Tir et Munition #####