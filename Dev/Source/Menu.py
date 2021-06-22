import pygame

class SpaceMenu():

    def __init__(self, fenetre, FENETRE_HAUTEUR, FENETRE_LARGEUR):
        self.MENU = ['Jouer', 'Facile>', 'Quitter']
        self.BLANC = (255, 255, 255)
        self.BOUTON = 0
        self.BOUTON_LARGEUR = 220
        self.BOUTON_HAUTEUR = 41
        self.fenetre = fenetre
        self.FENETRE_HAUTEUR = FENETRE_HAUTEUR
        self.FENETRE_LARGEUR = FENETRE_LARGEUR
        self.POLICE_ECRITURE_BOUTON = pygame.font.SysFont('monospace', 36)
        self.BOUTON_COULEUR_CLAIR = (170, 170, 170)
        self.BOUTON_COULEUR_FONCE = (100, 100, 100)
        self.MENU_LONGUEUR = len(self.MENU)
        self.HAUTEUR = self.FENETRE_HAUTEUR / self.MENU_LONGUEUR

    def afficherBoutonMenu(self):
        for index, text in enumerate(self.MENU):

            text_afficher = self.POLICE_ECRITURE_BOUTON.render(text, True, self.BLANC)
            texte_largeur, texte_hauteur = text_afficher.get_size()

            if index == self.BOUTON:

                pygame.draw.rect(self.fenetre, self.BOUTON_COULEUR_CLAIR,
                                 [(self.FENETRE_LARGEUR / 2) - self.BOUTON_LARGEUR // 2,
                                  ((self.FENETRE_HAUTEUR / self.MENU_LONGUEUR) - self.BOUTON_HAUTEUR) + (self.HAUTEUR / 2 * index),
                                  self.BOUTON_LARGEUR, 40])

            else:  # Afficher les boutons d'une couleur normale

                pygame.draw.rect(self.fenetre, self.BOUTON_COULEUR_FONCE,
                                 [(self.FENETRE_LARGEUR / 2) - self.BOUTON_LARGEUR // 2,
                                  ((self.FENETRE_HAUTEUR / self.MENU_LONGUEUR) - self.BOUTON_HAUTEUR) + (self.HAUTEUR / 2 * index),
                                  self.BOUTON_LARGEUR, 40])

            self.fenetre.blit(text_afficher, ((self.FENETRE_LARGEUR / 2) - texte_largeur // 2,
                                         (self.FENETRE_HAUTEUR / self.MENU_LONGUEUR) - texte_hauteur + (self.HAUTEUR * index) / 2))