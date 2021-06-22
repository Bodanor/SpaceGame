class SpaceMouvements():

    def __init__(self, SpaceWindow, SpaceGameplay,):
        self.SpaceWindow = SpaceWindow
        self.SpaceGameplay = SpaceGameplay

    def deplace_planete(self):
            for planete in self.SpaceGameplay.PLANETE_EN_LISTE:

                planete.place(planete.position[0], planete.position[1] + self.SpaceGameplay.VITESSE_JEU, planete.couloir)
                if planete.position[1] > self.SpaceWindow.FENETRE_HAUTEUR:
                    self.SpaceGameplay.PLANETE_EN_LISTE.remove(planete)
                    self.SpaceGameplay.couloir_utilise.remove(planete.couloir)
