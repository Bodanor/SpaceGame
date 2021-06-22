from Source.Entite import *

import math

### COLLISIONS ###

#Fonction permettant de calculer la disatnce entre deux entité
def distance_objets(objet1, HAUTEUR_OBJET1,LARGEUR_OBJET1, objet2, HAUTEUR_OBJET2,LARGEUR_OBJET2):
    centre_objet1_x = position(objet1)[0] + LARGEUR_OBJET1 / 2
    centre_objet1_y = position(objet1)[1] + HAUTEUR_OBJET1 / 2
    centre_objet2_x = position(objet2)[0] + LARGEUR_OBJET2 / 2
    centre_objet2_y = position(objet2)[1] + HAUTEUR_OBJET2 / 2
    distance = math.sqrt((centre_objet1_x - centre_objet2_x) ** 2 + (centre_objet1_y - centre_objet2_y) ** 2)

    return distance

#Collisions entre toutes les entités
def collision_entite(PLANETE_EN_LISTE,  nombre_vie, COMPTEUR_COLLISION, COMPTEUR_BONUS, collision_active, SCORE, vaisseau, VAISSEAU_HAUTEUR, VAISSEAU_LARGEUR, TAILLE_PLANETE, SON_EN_PAUSE, moinsvie, couloir_utilise, missile, MISSILE_UFO_EN_LISTE, UFO_EN_LISTE, explosion_ufo, couloir_utilise_ufo, UFO_TAILLE, TROU_NOIR_EN_LISTE, TROU_NOIR_TAILLE, couloir_utilise_trou_noir, BONUS_TAILLE, BONUS_EN_LISTE,couloir_utilise_bonus, enbonus, sonBonus):


    #Test si les collisions sont activées

    if collision_active == True:

        for bonus in BONUS_EN_LISTE:

            distance_vaisseau_bonus = distance_objets(vaisseau, VAISSEAU_LARGEUR, VAISSEAU_HAUTEUR, bonus, BONUS_TAILLE,
                                                      BONUS_TAILLE)

            # Collisions entre le vaisseau et le bonus

            if distance_vaisseau_bonus < 55:  # SI on a une collision avec le bonus, la musique joue pendnat 10 seconde

                COMPTEUR_BONUS = 600
                BONUS_EN_LISTE.remove(bonus)
                enbonus = True
                couloir_bonus = afficherCouloir(bonus)
                couloir_utilise_bonus.remove(couloir_bonus)
                return nombre_vie, COMPTEUR_COLLISION, collision_active, SCORE, enbonus, COMPTEUR_BONUS

        for ufo in UFO_EN_LISTE:
            # Collision entre l'ufo et les missiles
            for missiles in missile:
                distance_missile_ufo = distance_objets(missiles, 10, 10, ufo, UFO_TAILLE, UFO_TAILLE)

                if distance_missile_ufo < 43:  # Si un de nos missiles touche un UFO, l'UFO disparait, le missile aussi, on joue le son de destructionde l'UFO, et on ajoute 25 points
                    if SON_EN_PAUSE == False:
                        explosion_ufo.play()
                    missile.remove(missiles)
                    UFO_EN_LISTE.remove(ufo)
                    couloir_ufo = afficherCouloir(ufo)
                    couloir_utilise_ufo.remove(couloir_ufo)
                    SCORE += 25
                    return nombre_vie, COMPTEUR_COLLISION, collision_active, SCORE, enbonus, COMPTEUR_BONUS

        #COllISION PLANETE
        for planete in PLANETE_EN_LISTE:

                #Calcul de la distance entre le centre de la planete et du vaisseaux
                distance_vaisseau_planete = distance_objets(vaisseau,VAISSEAU_HAUTEUR,VAISSEAU_LARGEUR,planete,TAILLE_PLANETE,TAILLE_PLANETE)

                if distance_vaisseau_planete < 125: #Si il y a collision avec une planète, on enlève une vie, on joue un son et on désactive les collisions pendant 3 secondes
                    if enbonus == False:
                        nombre_vie = nombre_vie - 1
                        COMPTEUR_COLLISION = 180
                        collision_active = False

                        if SON_EN_PAUSE == False:
                            moinsvie.play()
                    PLANETE_EN_LISTE.remove(planete)
                    couloir_planete = afficherCouloir(planete)
                    couloir_utilise.remove(couloir_planete)

                    return nombre_vie, COMPTEUR_COLLISION, collision_active, SCORE, enbonus, COMPTEUR_BONUS

                for missiles in missile:
                    distance_missile_planete = distance_objets(missiles, 10, 10, planete, TAILLE_PLANETE, TAILLE_PLANETE)

                    if distance_missile_planete < 92: #On test si les missiles rentrent en contact avec une planete. Si c'est le cas, on enlève le missile
                        missile.remove(missiles)

                        return nombre_vie, COMPTEUR_COLLISION, collision_active, SCORE, enbonus, COMPTEUR_BONUS

                for missile_ufo in MISSILE_UFO_EN_LISTE:
                    distance_missileUFO_planete = distance_objets(missile_ufo, 10, 10, planete, TAILLE_PLANETE, TAILLE_PLANETE)

                    if distance_missileUFO_planete < 92:#On test si les missiles UFO rentrent en contact avec une planete. Si c'est le cas, on enlève le missile
                        MISSILE_UFO_EN_LISTE.remove(missile_ufo)

                        return nombre_vie, COMPTEUR_COLLISION, collision_active, SCORE, enbonus, COMPTEUR_BONUS


        #COLLISION UFO
        for ufo in UFO_EN_LISTE:

            distance_vaisseau_UFO = distance_objets(vaisseau,VAISSEAU_LARGEUR,VAISSEAU_HAUTEUR,ufo,UFO_TAILLE,UFO_TAILLE)

            # Collisions entre le vaisseau et l'ufo
            if distance_vaisseau_UFO < 70: #Si on percute un UFO, on enlève une vie, on joue le son de perte de vie et de destruction de l'UFO (et on enlève l'UFO)(et on désactive les collisions pendant 3 secondes)
                if SON_EN_PAUSE == False:
                    explosion_ufo.play()
                if enbonus == False:
                    nombre_vie = nombre_vie - 1
                    COMPTEUR_COLLISION = 180
                    collision_active = False

                    if SON_EN_PAUSE == False:
                        moinsvie.play()

                UFO_EN_LISTE.remove(ufo)

                couloir_ufo = afficherCouloir(ufo)
                couloir_utilise_ufo.remove(couloir_ufo)
                return nombre_vie, COMPTEUR_COLLISION, collision_active, SCORE, enbonus, COMPTEUR_BONUS


        #COLLISIONS TROU NOIR
        for trou_noir in TROU_NOIR_EN_LISTE:

            #Collision entre les trous noirs et le vaisseau. Si c'est le cas le jeu s'arrête instantanèment
            distance_vaisseau_trou_noir = distance_objets(trou_noir,TROU_NOIR_TAILLE,TROU_NOIR_TAILLE, vaisseau, VAISSEAU_LARGEUR, VAISSEAU_HAUTEUR )

            if distance_vaisseau_trou_noir < 70:
                nombre_vie = 0
                COMPTEUR_COLLISION = 180
                collision_active = False
                couloir_trou_noir = afficherCouloir(trou_noir)
                couloir_utilise_trou_noir.remove(couloir_trou_noir)
                return nombre_vie, COMPTEUR_COLLISION, collision_active, SCORE, enbonus, COMPTEUR_BONUS

            # Collisions entre les missiles et les trous noirs
            for missiles in missile:
                distance_missile_trou_noir = distance_objets(missiles, 10, 10, trou_noir, TROU_NOIR_TAILLE,
                                                             TROU_NOIR_TAILLE)
                if distance_missile_trou_noir < 43:#Si collisions avec le missile, on remove le missile
                    missile.remove(missiles)
                    return nombre_vie, COMPTEUR_COLLISION, collision_active, SCORE, enbonus, COMPTEUR_BONUS

            #Collisions entre les missiles de l'ufo et le trou noir
            for missiles_ufo in MISSILE_UFO_EN_LISTE:
                distance_missileUFO_trou_noir = distance_objets(missiles_ufo, 10, 10, trou_noir, TROU_NOIR_TAILLE,
                                                             TROU_NOIR_TAILLE)

                if distance_missileUFO_trou_noir < 43:#Si collisions avec le missile de l'ufo, on remove le missile de l'ufo

                    MISSILE_UFO_EN_LISTE.remove(missiles_ufo)
                    return nombre_vie, COMPTEUR_COLLISION, collision_active, SCORE, enbonus, COMPTEUR_BONUS




        #COLLISIONS ENTRE MISSILES UFO ET VAISSEAU
        for missile_ufo in MISSILE_UFO_EN_LISTE:

                distance_missileUFO_vaisseau = distance_objets(vaisseau,VAISSEAU_HAUTEUR,VAISSEAU_LARGEUR,missile_ufo,10,10)

                if distance_missileUFO_vaisseau < 45: #Si le missile UFO nous touche, on perd une vie, on enlève le missile, on joue le son de perte de vie, et on désactive les collisions pendant 3 secondes
                     if enbonus == False:
                         nombre_vie = nombre_vie - 1
                         COMPTEUR_COLLISION = 180
                         collision_active = False

                         if SON_EN_PAUSE == False:
                             moinsvie.play()

                     MISSILE_UFO_EN_LISTE.remove(missile_ufo)

                return nombre_vie, COMPTEUR_COLLISION, collision_active, SCORE, enbonus, COMPTEUR_BONUS


    else:
        return nombre_vie, COMPTEUR_COLLISION, collision_active, SCORE, enbonus, COMPTEUR_BONUS

    return nombre_vie, COMPTEUR_COLLISION, collision_active, SCORE, enbonus, COMPTEUR_BONUS
###FIN COLLISIONS


######### FIN  SPAWN, COLLISIONS ET DEPLACEMENT DES OBSTACLES ##########