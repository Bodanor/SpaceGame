import pygame
import random

class SpaceWindow:
    def __init__(self, GameName):
        self.GameName = GameName
        self.images = {}
        self.ESPACE = (0, 0, 15)
        self.BLANC = (255, 255, 255)
        self.BLEU = (129, 78, 216)
        self.ROUGE = (255, 0, 0)
        self.VERT = (0, 255, 0)
        self.ORANGE = (255, 165, 0)
        self.JAUNE = (255, 255, 0)
        self.VERT_CLAIR = (51, 255, 51)
        self.GRIS = (128, 128, 128)
        self.CYAN = (51, 255, 255)
        self.FENETRE_LARGEUR = 1080
        self.FENETRE_HAUTEUR = 720
        self.VAISSEAU_LARGEUR = 70
        self.VAISSEAU_HAUTEUR = 60
        self.VIE_LARGEUR = 30
        self.VIE_HAUTEUR = 25
        self.UFO_TAILLE = 80
        self.BONUS_TAILLE = 40
        self.TAILLE_PLANETE = int(self.FENETRE_LARGEUR / 6)
        self.police = pygame.font.SysFont('monospace', self.FENETRE_HAUTEUR // 40, True)
        self.fenetre = pygame.display.set_mode((self.FENETRE_LARGEUR, self.FENETRE_HAUTEUR), pygame.RESIZABLE)

        self.initialisation()

    def initialisation(self):
        self.charger_images()
        pygame.display.set_icon(self.images['GameIcon'])
        pygame.display.set_caption(self.GameName)
    def charger_images(self):
        print("CHARGEMENT D'IMAGES DIVERSES...")
        self.images["GameIcon"] = pygame.image.load("Images/vaisseau_jaune_avec_flamme.png")
        self.images["VieImg"] = pygame.image.load('Images/vaisseau_rouge_avec_flamme.png')
        self.images["TrouImg"] = pygame.image.load('Images/trou_noir.png')
        self.images['UFOImg'] = pygame.image.load('Images/ufo.png').convert_alpha(self.fenetre)
        self.images['UFOImg'] = pygame.transform.scale(self.images['UFOImg'], (self.UFO_TAILLE, self.UFO_TAILLE))
        self.images['BonusImg'] = pygame.image.load('Images/bonus.png').convert_alpha(self.fenetre)
        self.images['BonusImg'] = pygame.transform.scale(self.images['BonusImg'], (self.BONUS_TAILLE, self.BONUS_TAILLE))
        print("[LOG] CHARGEMENT DES PLANETES...")

        for nom_image, nom_fichier in (('Planete1', 'planete1.png'),
                                       ('Planete2', 'planete2.png'),
                                       ('Planete3', 'planete3.png'),
                                       ('Planete4', 'planete4.png'),
                                       ('Planete5', 'planete5.png'),
                                       ('Planete6', 'planete6.png'),
                                       ('Planete7', 'planete7.png'),
                                       ('Planete8', 'planete8.png'),
                                       ('Planete9', 'planete9.png'),
                                       ('Planete10', 'planete10.png'),
                                       ('Planete11', 'planete11.png'),
                                       ('Planete12', 'planete12.png'),
                                       ('Planete13', 'planete13.png'),
                                       ('Planete14', 'planete14.png'),
                                       ('Planete15', 'planete15.png'),
                                       ('Planete16', 'planete16.png')):
            self.chemin = 'Images/' + nom_fichier
            self.image = pygame.image.load(self.chemin).convert_alpha(self.fenetre)
            self.image = pygame.transform.scale(self.image, (self.TAILLE_PLANETE, self.TAILLE_PLANETE))
            self.images[nom_image] = self.image

        print("[LOG] CHARGEMENT DES VAISSEAUX....")

        for nom_image, nom_fichier in (('vaisseau_jaune_sans_flamme', 'vaisseau_jaune_sans_flamme.png'),
                                       ('vaisseau_jaune_avec_flamme', 'vaisseau_jaune_avec_flamme.png'),
                                       ('vaisseau_rouge_avec_flamme', 'vaisseau_rouge_avec_flamme.png'),
                                       ('vaisseau_rouge_sans_flamme', 'vaisseau_rouge_sans_flamme.png'),
                                       ('vaisseau_blanc_avec_flamme', 'vaisseau_blanc_avec_flamme.png'),
                                       ('vaisseau_blanc_sans_flamme', 'vaisseau_blanc_sans_flamme.png'),
                                       ('vaisseau_bleu_avec_flamme', 'vaisseau_bleu_avec_flamme.png'),
                                       ('vaisseau_bleu_sans_flamme', 'vaisseau_bleu_sans_flamme.png'),
                                       ('vaisseau_rose_avec_flamme', 'vaisseau_rose_avec_flamme.png'),
                                       ('vaisseau_rose_sans_flamme', 'vaisseau_rose_sans_flamme.png'),
                                       ('vaisseau_vert_avec_flamme', 'vaisseau_vert_avec_flamme.png'),
                                       ('vaisseau_vert_sans_flamme', 'vaisseau_vert_sans_flamme.png')):
            chemin = 'Images/' + nom_fichier
            image = pygame.image.load(chemin).convert_alpha(self.fenetre)
            image = pygame.transform.scale(image, (self.VAISSEAU_LARGEUR, self.VAISSEAU_HAUTEUR))
            self.images[nom_image] = image

        print("CHARGEMENT IMAGES TERMINE !")

    def afficher(self, entite):
        if entite.visible == True:
            self.fenetre.blit(entite.image, entite.position)

    def afficher_planetes(self, SpaceGameplay):
        for Planete in SpaceGameplay.PLANETE_EN_LISTE:

            self.fenetre.blit(Planete.image, Planete.position)

    def afficher_ufo(self, SpaceGameplay):

        for ufo in SpaceGameplay.UFO_EN_LISTE:
            self.fenetre.blit(ufo.image, ufo.position)

    def afficher_etoiles(self, etoiles, vitesse_etoiles):
        for etoile in etoiles:
            pygame.draw.line(self.fenetre, (255, 255, 255), (etoile[0], etoile[1]), (etoile[0], etoile[1]))

            etoile[1] = etoile[1] + vitesse_etoiles / 2
            if etoile[1] > self.FENETRE_HAUTEUR:
                etoile[1] = 0
                etoile[0] = random.randint(0, self.FENETRE_LARGEUR)

    def affichervie(self, NOMBRE_VIE):
        for x in range(0, NOMBRE_VIE + 1):
            self.images['VieImg'] = pygame.transform.scale(self.images['VieImg'], (self.VIE_LARGEUR, self.VIE_HAUTEUR))
            self.fenetre.blit(self.images['VieImg'], (self.FENETRE_LARGEUR - self.VIE_LARGEUR * x, self.FENETRE_HAUTEUR - self.VIE_HAUTEUR))

    def afficher_munition(self,MUNITIONS):
        if MUNITIONS == 0:  # Afficher les munitions en rouges quand il n'y en a plus

            munition = self.police.render(str(": {}".format(int(MUNITIONS))), True, self.ROUGE)
            self.fenetre.blit(munition, (35, self.FENETRE_HAUTEUR - 35))
            pygame.draw.rect(self.fenetre, self.BLANC, pygame.Rect(5, self.FENETRE_HAUTEUR - 40, munition.get_size()[0] + 40, 30),
                             width=1)
            pygame.draw.circle(self.fenetre, self.BLEU, (17, self.FENETRE_HAUTEUR - 25), 10, width=1)
            pygame.draw.circle(self.fenetre, self.BLANC, (17, self.FENETRE_HAUTEUR - 25), 5)

        else:  # Afficher les munitions normalement
            munition = self.police.render(str(": {}".format(int(MUNITIONS))), True, self.BLANC)
            self.fenetre.blit(munition, (35, self.FENETRE_HAUTEUR - 35))
            pygame.draw.rect(self.fenetre, self.BLANC, pygame.Rect(5, self.FENETRE_HAUTEUR - 40, munition.get_size()[0] + 40, 30),
                             width=1)
            pygame.draw.circle(self.fenetre, self.BLEU, (17, self.FENETRE_HAUTEUR - 25), 10, width=1)
            pygame.draw.circle(self.fenetre, self.BLANC, (17, self.FENETRE_HAUTEUR - 25), 5)

    def dessine_missile(self, SpaceGameplay):
        for missile in SpaceGameplay.missiles:
            COULEUR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            if missile.estVisibleMissile():
                if missile.positionMissile()[1] < 0:
                    SpaceGameplay.missiles.remove(missile)
            missile.deplace_missile(SpaceGameplay.VITESSE_MISSILE)
            pygame.draw.circle(self.fenetre, COULEUR, list(map(int, missile.positionMissile())), 7)
            pygame.draw.circle(self.fenetre, COULEUR, list(map(int, missile.positionMissile())), 10, width=1)
            pygame.draw.circle(self.fenetre, self.BLANC, list(map(int, missile.positionMissile())), 5)

        for missile_ufo in SpaceGameplay.missiles_ufo:

            COULEUR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            if missile_ufo.estVisibleMissile():
                if missile_ufo.positionMissile()[1] < 0:
                    SpaceGameplay.missiles_ufo.remove(missile_ufo)
            missile_ufo.deplace_missile(-SpaceGameplay.VITESSE_MISSILE)
            pygame.draw.circle(self.fenetre, COULEUR, list(map(int, missile_ufo.positionMissile())), 7)
            pygame.draw.circle(self.fenetre, COULEUR, list(map(int, missile_ufo.positionMissile())), 10, width=1)
            pygame.draw.circle(self.fenetre, self.BLANC, list(map(int, missile_ufo.positionMissile())), 5)

