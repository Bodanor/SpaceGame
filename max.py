def collision_planete(PLANETE_EN_LISTE, position_vaisseau):

    for planete in PLANETE_EN_LISTE:
        #Test collision dans l'ordre BAS,HAUT,DROITE,GAUCHE
        if position_vaisseau[1] <= position(planete)[1] + TAILLE_PLANETE and position_vaisseau[1]+VAISSEAU_HAUTEUR >= position(planete)[1] and position(planete)[0] <= position_vaisseau[0]+VAISSEAU_LARGEUR and position_vaisseau[0] <= position(planete)[0]+TAILLE_PLANETE:
            if position_vaisseau[1] <= position(planete)[1] + TAILLE_PLANETE*(7/8) and position_vaisseau[1]+VAISSEAU_HAUTEUR >= position(planete)[1]+ TAILLE_PLANETE*(1/8) and position(planete)[0] + TAILLE_PLANETE*(1/8) <= position_vaisseau[0]+VAISSEAU_LARGEUR and position_vaisseau[0] <= position(planete)[0]+TAILLE_PLANETE*(7/8):
