from Source.Missiles import *
import random


###SPAWN###
def creation_couloirs_planete(COULOIRS, FENETRE_LARGEUR):
    for x in range(0, 5):
        COULOIRS.append(((FENETRE_LARGEUR / 5) * x, (FENETRE_LARGEUR / 5) * (x + 1)))


def spawn_planete(couloir_utilise, PLANETE_EN_LISTE, LISTE_PLANETE, COULOIRS):
    # Nombre de chances de spawn une planete
    random_timer = random.randint(1, 16)
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


def spawn_ufo(couloir_utilise_ufo, UFO_EN_LISTE, PLANETE_EN_LISTE, LISTE_UFO, TAILLE_PLANETE, COULOIRS, MISSILE_UFO_EN_LISTE):
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
                            if hauteur_random > position(planete)[1] + TAILLE_PLANETE or hauteur_random < position(planete)[1] - TAILLE_PLANETE:

                                place(LISTE_UFO[ufo_random], COULOIRS[couloir_random][0], hauteur_random,
                                      couloir_random)
                                UFO_EN_LISTE.append(LISTE_UFO[ufo_random])
                                couloir_utilise_ufo.append(couloir_random)
                                ajouter_missile_ufo(position(LISTE_UFO[ufo_random]), MISSILE_UFO_EN_LISTE)

def spawn_trou_noir(niveau_difficulte, couloir_utilise_trou_noir, FREQUENCE_APPARITION_TROU_NOIR, TROU_NOIR_EN_LISTE, LISTE_TROU_NOIR, PLANETE_EN_LISTE, COULOIRS, TAILLE_PLANETE):

    random_timer = random.randint(0, FREQUENCE_APPARITION_TROU_NOIR)
    if random_timer == 2:
        if len(TROU_NOIR_EN_LISTE) < niveau_difficulte +1:

            couloir_random = random.randint(0, 4)
            trou_noir_random = random.randint(0, 4)
            hauteur_random = random.randint(-200, -80)

            # On verifie qu'il n'existe pas deja une planete a l'emplacement du trou noir
            if couloir_random in couloir_utilise_trou_noir:
                pass
            else:
                if LISTE_TROU_NOIR[trou_noir_random] in TROU_NOIR_EN_LISTE:
                    pass
                else:

                    for planete in PLANETE_EN_LISTE:


                        couloir_planete = afficherCouloir(planete)
                        if couloir_planete == couloir_random:

                            if hauteur_random > position(planete)[1] + TAILLE_PLANETE or hauteur_random < position(planete)[1] - TAILLE_PLANETE:
                                place(LISTE_TROU_NOIR[trou_noir_random], COULOIRS[couloir_random][0], hauteur_random,
                                      couloir_random)

                                TROU_NOIR_EN_LISTE.append(LISTE_TROU_NOIR[trou_noir_random])
                                couloir_utilise_trou_noir.append(couloir_random)

def spawn_bonus(niveau_difficulte, couloir_utilise_bonus, FREQUENCE_APPARITION_BONUS, BONUS_EN_LISTE, BONUS_LISTE, PLANETE_EN_LISTE, COULOIRS, TAILLE_PLANETE, enbonus):

    random_timer = random.randint(0, FREQUENCE_APPARITION_BONUS)
    if random_timer == 2:
        if len(BONUS_EN_LISTE) <1 and (enbonus == False):

            couloir_random = random.randint(0, 4)
            bonus_random = random.randint(0, 4)
            hauteur_random = random.randint(-200, -80)

            # On verifie qu'il n'existe pas deja une planete a l'emplacement du trou noir
            if couloir_random in couloir_utilise_bonus:
                pass
            else:
                if BONUS_LISTE[bonus_random] in BONUS_EN_LISTE:
                    pass
                else:

                    for planete in PLANETE_EN_LISTE:


                        couloir_planete = afficherCouloir(planete)
                        if couloir_planete == couloir_random:

                            if hauteur_random > position(planete)[1] + TAILLE_PLANETE or hauteur_random < position(planete)[1] - TAILLE_PLANETE:
                                place(BONUS_LISTE[bonus_random], COULOIRS[couloir_random][0], hauteur_random,
                                      couloir_random)

                                BONUS_EN_LISTE.append(BONUS_LISTE[bonus_random])
                                couloir_utilise_bonus.append(couloir_random)

###FIN SPAWN###

