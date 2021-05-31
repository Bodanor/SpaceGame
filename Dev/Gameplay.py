class SpaceGamePlay:

    def __init__(self):
        self.NOMBRE_VIE = 3
        self.VITESSE_ETOILE = 3
        self.MUNITIONS = 20
        self.niveau_difficulte = 0

    def changer_difficulte(self, SpaceMenu):
        if self.niveau_difficulte == 0:
            SpaceMenu.MENU = ['Jouer', 'Facile>', 'Quitter']

        elif self.niveau_difficulte == 1:
            SpaceMenu.MENU = ['Jouer', '<Moyen>', 'Quitter']

        elif self.niveau_difficulte == 2:
            SpaceMenu.MENU = ['Jouer', '<Difficile', 'Quitter']
