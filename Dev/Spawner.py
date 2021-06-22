import random
import Entite

class Spawner():
    def __init__(self, SpaceWindow, SpaceGameplay):
        self.COULOIRS = []
        self.SpaceWindow = SpaceWindow
        self.SpaceGameplay = SpaceGameplay

    def creation_couloirs_planete(self):
        for x in range(0, 5):
            self.COULOIRS.append(((self.SpaceWindow.FENETRE_LARGEUR / 5) * x, (self.SpaceWindow.FENETRE_LARGEUR / 5) * (x + 1)))

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
                        EntitePlanete.image = self.SpaceWindow.images["Planete{}".format(planete_random)]
                        EntitePlanete.place(self.COULOIRS[couloir_random][0], -self.SpaceWindow.TAILLE_PLANETE, couloir_random)
                        self.SpaceGameplay.PLANETE_EN_LISTE.append(EntitePlanete)
                        self.SpaceGameplay.couloir_utilise.append(couloir_random)