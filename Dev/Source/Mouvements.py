class SpaceMouvements():

    def __init__(self,SpaceGameplay):

        self.SpaceGameplay = SpaceGameplay

    def deplace_Objets(self):
            for planete in self.SpaceGameplay.PLANETE_EN_LISTE:

                planete.place(planete.position[0], planete.position[1] + self.SpaceGameplay.VITESSE_JEU, planete.couloir)
                if planete.position[1] > self.SpaceGameplay.SpaceWindow.FENETRE_HAUTEUR:
                    self.SpaceGameplay.PLANETE_EN_LISTE.remove(planete)
                    self.SpaceGameplay.couloir_utilise.remove(planete.couloir)

            for ufo in self.SpaceGameplay.UFO_EN_LISTE:

                ufo.place(ufo.position[0], ufo.position[1] + self.SpaceGameplay.VITESSE_JEU, ufo.couloir)
                if ufo.position[1] > self.SpaceGameplay.SpaceWindow.FENETRE_HAUTEUR:
                    self.SpaceGameplay.UFO_EN_LISTE.remove(ufo)
                    self.SpaceGameplay.couloir_utilise_ufo.remove(ufo.couloir)