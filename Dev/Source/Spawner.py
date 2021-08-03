import random
from Dev.Source import Entite, Missiles


class Spawner():
    def __init__(self,SpaceGameplay):
        self.COULOIRS = []
        self.SpaceGameplay = SpaceGameplay

    def creation_couloirs_planete(self):
        for x in range(0, 5):
            self.COULOIRS.append(((self.SpaceGameplay.SpaceWindow.FENETRE_LARGEUR / 5) * x, (self.SpaceGameplay.SpaceWindow.FENETRE_LARGEUR / 5) * (x + 1)))

    def spawn_planete(self):
        # Nombre de chances de spawn une planete
        random_timer = random.randint(0, 14)
        if random_timer == 3:
            # Pas plus de 4 planetes a l'ecran
            if len(self.SpaceGameplay.PLANETE_EN_LISTE) < 4:
                couloir_random = random.randint(0, 4)
                planete_random = random.randint(1, 16)

                # Une seule planete par couloir
                if couloir_random not in self.SpaceGameplay.couloir_utilise:
                        EntitePlanete = Entite.Entite()
                        EntitePlanete.image = self.SpaceGameplay.SpaceWindow.images["Planete{}".format(planete_random)]
                        EntitePlanete.place(self.COULOIRS[couloir_random][0], -self.SpaceGameplay.SpaceWindow.TAILLE_PLANETE, couloir_random)
                        self.SpaceGameplay.PLANETE_EN_LISTE.append(EntitePlanete)
                        self.SpaceGameplay.couloir_utilise.append(couloir_random)

    def spawn_ufo(self):
        random_timer = random.randint(0, 14)
        if random_timer == 2:
            if len(self.SpaceGameplay.UFO_EN_LISTE) < 1:
                couloir_random = random.randint(0, 4)
                hauteur_random = random.randint(-200, -80)

                if couloir_random not in self.SpaceGameplay.couloir_utilise_ufo:
                    for planete in self.SpaceGameplay.PLANETE_EN_LISTE:

                        if planete.afficherCouloir() == couloir_random:
                            if hauteur_random > planete.position[1] + self.SpaceGameplay.SpaceWindow.TAILLE_PLANETE or hauteur_random < \
                                    planete.position[1] - self.SpaceGameplay.SpaceWindow.TAILLE_PLANETE:

                                EntiteUFO = Entite.Entite()
                                EntiteUFO.image = self.SpaceGameplay.SpaceWindow.images["UFOImg"]
                                EntiteUFO.place(self.COULOIRS[couloir_random][0], hauteur_random, couloir_random)
                                self.SpaceGameplay.UFO_EN_LISTE.append(EntiteUFO)
                                self.SpaceGameplay.couloir_utilise_ufo.append(couloir_random)

                                #TODO: Ajouter missile à l'UFO

    def tir_random_ufo(self):
        for ufo in self.SpaceGameplay.UFO_EN_LISTE:

            if self.SpaceGameplay.COMPTEUR_BOUCLE % self.SpaceGameplay.FREQUENCE_TIR == 0:
                missile = Missiles.Missile(self.SpaceGameplay)
                missile.placeMissile(ufo.position[0] + self.SpaceGameplay.SpaceWindow.VAISSEAU_LARGEUR / 2,
                                     ufo.position[1] + self.SpaceGameplay.SpaceWindow.VAISSEAU_HAUTEUR / 2)
                self.SpaceGameplay.missiles_ufo.append(missile)
