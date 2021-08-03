from Dev.Source import Affichage, Menu, Mouvements, Sound, Spawner, Collisions

class SpaceGamePlay:

    def __init__(self):
        self.NOMBRE_VIE = 3
        self.VITESSE_ETOILE = 3
        self.MUNITIONS = 20
        self.niveau_difficulte = 0
        self.AJOUT_MUNITION = 20
        self.MUNITIONS = 20
        self.VITESSE_JEU = 3
        self.VITESSE_MISSILE = 15
        self.DEPLACEMENT_VAISSEAU = 7
        self.FREQUENCE_APPARITION_TROU_NOIR = 500
        self.FREQUENCE_TIR = 180
        self.missiles = []
        self.missiles_ufo = []
        self.COMPTEUR_BOUCLE = 0
        self.PLANETE_EN_LISTE = []
        self.UFO_EN_LISTE = []
        self.couloir_utilise = []
        self.couloir_utilise_ufo = []
        self.collision_active = True

        self.SpaceWindow = Affichage.SpaceWindow('Space Game')
        self.SpaceMenu = Menu.SpaceMenu(self)
        self.SpaceSound = Sound.SpaceSound()

        # Creation de couloirs pour le jeu
        self.SpaceSpawner = Spawner.Spawner(self)
        self.SpaceSpawner.creation_couloirs_planete()

        self.SpaceMouvements = Mouvements.SpaceMouvements(self)

        self.SpaceCollisions = Collisions.SpaceCollisions(self)

    def changer_difficulte(self, SpaceMenu):
        if self.niveau_difficulte == 0:
            SpaceMenu.MENU = ['Jouer', 'Facile>', 'Quitter']
            self.AJOUT_MUNITION = 20
            self.MUNITIONS = 20
            self.VITESSE_JEU = 3
            self.VITESSE_MISSILE = 15
            self.NOMBRE_VIE = 3
            self.DEPLACEMENT_VAISSEAU = 7
            self.FREQUENCE_APPARITION_TROU_NOIR = 500
            self.FREQUENCE_TIR = 180

        elif self.niveau_difficulte == 1:
            SpaceMenu.MENU = ['Jouer', '<Moyen>', 'Quitter']
            self.AJOUT_MUNITION = 15
            self.MUNITIONS = 15
            self.VITESSE_JEU = 5
            self.VITESSE_MISSILE = 10
            self.NOMBRE_VIE = 2
            self.DEPLACEMENT_VAISSEAU = 6
            self.FREQUENCE_APPARITION_TROU_NOIR = 250
            self.FREQUENCE_TIR = 120

        elif self.niveau_difficulte == 2:
            SpaceMenu.MENU = ['Jouer', '<Difficile', 'Quitter']

