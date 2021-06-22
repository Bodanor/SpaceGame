import pygame

class SpaceSound():
    def __init__(self):
        self.sounds = {}
        self.charger_sons()
        self.SON_EN_PAUSE = False

    def charger_sons(self):
        print("CHARGEMENT DES BRUITAGES...")
        self.sounds['explosion'] = pygame.mixer.Sound("Bruitages/explosion_ufo.wav")
        self.sounds['choix'] = pygame.mixer.Sound("Bruitages/choix_menu.wav")
        self.sounds['choix_droite_gauche'] = pygame.mixer.Sound("Bruitages/droite_gauche.wav")
        self.sounds['choix_gauche_droite'] = pygame.mixer.Sound("Bruitages/gauche_droite.wav")
        self.sounds['piou'] = pygame.mixer.Sound("Bruitages/piou.wav")
        self.sounds['no_bullets'] = pygame.mixer.Sound("Bruitages/no_bullets.wav")
        self.sounds['moinsvie'] = pygame.mixer.Sound("Bruitages/moinsvie.wav")
        self.sounds['sonBonus'] = pygame.mixer.Sound("Bruitages/bonus.wav")
        self.sounds['start'] = pygame.mixer.Sound("Bruitages/start.wav")
        self.sounds['back'] = pygame.mixer.Sound("Bruitages/back.wav")
        print("CHARGEMENT DE LA BANDE SON...")
        self.sounds['musique'] = pygame.mixer.Sound("Bande Son/musiquePrincipal.wav")
        print("CHARGEMENT SON TERMINE !")