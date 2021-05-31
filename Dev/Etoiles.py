import random

class Etoiles():

    def __init__(self, FENETRE_LARGEUR, FENETRE_HAUTEUR):
        self.NOMBRE_ETOILES = 500
        self.FENETRE_LARGEUR = FENETRE_LARGEUR
        self.FENETRE_HAUTEUR = FENETRE_HAUTEUR
        self.ETOILES = []

    def cree_etoiles(self):
        for x in range(self.NOMBRE_ETOILES):
            self.ETOILES.append([random.randint(0, self.FENETRE_LARGEUR), random.randint(0, self.FENETRE_HAUTEUR)])
