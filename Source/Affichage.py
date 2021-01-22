from Source.Variable import *
import pygame
import os

#Affichagedes controles quand on lance le jeu (uniquement)
def afficher_controles(fenetre, police):
    controle_echap = police.render(str("ECHAP : Mettre le jeu en pause"), True, BLANC)
    controle_mute = police.render(str("M : Couper le son du jeu"), True, BLANC)
    fleche_vie = police.render(str("Vies ►"), True, BLANC)
    controle_touche = pygame.image.load("Images/fleche.png")
    controle_touche = pygame.transform.scale(controle_touche, (80, 50))
    controle_touche_texte = police.render(str("Controles ►"), True, BLANC)
    controle_espace = pygame.image.load("Images/espace.png")
    controle_espace = pygame.transform.scale(controle_espace, (120, 30))



    fenetre.blit(controle_echap, (0, FENETRE_HAUTEUR*(6.5/8)))
    fenetre.blit(controle_mute, (0, FENETRE_HAUTEUR * (7 / 8)))
    fenetre.blit(fleche_vie, (FENETRE_LARGEUR - 6*VIE_LARGEUR, FENETRE_HAUTEUR - VIE_HAUTEUR + 5))
    fenetre.blit(controle_touche, (FENETRE_LARGEUR-140, FENETRE_HAUTEUR * (6 / 8)))
    fenetre.blit(controle_touche_texte, (FENETRE_LARGEUR -280, FENETRE_HAUTEUR * (6.3 / 8)))
    fenetre.blit(controle_espace, (FENETRE_LARGEUR -170, FENETRE_HAUTEUR * (5 / 8)))

#Menu Pause
def pause(fenetre, POLICE_ECRITURE_BOUTON, BOUTON, MENU_PAUSE):
    for index, text in enumerate(MENU_PAUSE):

        text_afficher = POLICE_ECRITURE_BOUTON.render(text, True, BLANC)
        texte_largeur, texte_hauteur = text_afficher.get_size()

        # affichage des boutons de couleurs différentes selon celui qui est sélectionné

        if BOUTON == index:
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

######### FIN MENU ##########

#Menu de départ
def afficherBoutonMenu(fenetre, POLICE_ECRITURE_BOUTON, BOUTON, MENU):
    for index, text in enumerate(MENU):

        text_afficher = POLICE_ECRITURE_BOUTON.render(text, True, BLANC)
        texte_largeur, texte_hauteur = text_afficher.get_size()

        # détection de la souris qui passe au dessus des boutons et les afficher en couleur clair si elle est au dessus
        if index == BOUTON:


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



###### NOTIFICATION #######
def coinNotif(fenetre, police, COMPTEUR_NOTIF, COMPTEUR_MUTE, FENETRE_LARGEUR):


        if COMPTEUR_NOTIF > 0:
            if COMPTEUR_MUTE % 2 == 1:
                phrase = str("{}".format("Son Activé"))
                notification = police.render(phrase, True, ROUGE)
                longueur_text_x, longueur_text_y =notification.get_size()
                fenetre.blit(notification, (FENETRE_LARGEUR - longueur_text_x, 0))

            else:
                phrase = str("{}".format("Son Désactivé"))
                notification = police.render(phrase, True, ROUGE)
                longueur_text_x, longueur_text_y = notification.get_size()
                fenetre.blit(notification, (FENETRE_LARGEUR - longueur_text_x, 0))

###### FIN NOTIFICATION ######


# Affichage du score et des vies #
def score(fenetre, police, SCORE, FENETRE_HAUTEUR):
    marquoir = police.render(str("Score: {}".format(int(round(SCORE, 0)))), True, VERT_CLAIR)
    fenetre.blit(marquoir, (20, FENETRE_HAUTEUR // 12))


def vie(fenetre, vie_image, NOMBRE_VIE, FENETRE_HAUTEUR, FENETRE_LARGEUR):
    for x in range(0, NOMBRE_VIE + 1):
        image = pygame.transform.scale(vie_image, (VIE_LARGEUR, VIE_HAUTEUR))
        fenetre.blit(image, (FENETRE_LARGEUR - VIE_LARGEUR * x, FENETRE_HAUTEUR - VIE_HAUTEUR))
##################################

#Affichage des munitions restantes en bas à gauche
def afficher_munition(fenetre, police,MUNITIONS, FENETRE_HAUTEUR):
    if MUNITIONS == 0:  # Afficher les munitions en rouges quand il n'y en a plus

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


######### SPAWN, COLLISIONS ET DEPLACEMENT DES OBSTACLES ##########