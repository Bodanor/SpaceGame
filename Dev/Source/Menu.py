import pygame

class SpaceMenu():

    def __init__(self, SpaceGameplay):
        self.SpaceGameplay = SpaceGameplay
        self.MENU = ['Jouer', 'Facile>', 'Quitter']
        self.BLANC = (255, 255, 255)
        self.BOUTON = 0
        self.BOUTON_LARGEUR = 220
        self.BOUTON_HAUTEUR = 41
        self.fenetre = self.SpaceGameplay.SpaceWindow.fenetre
        self.POLICE_ECRITURE_BOUTON = pygame.font.SysFont('monospace', 36)
        self.BOUTON_COULEUR_CLAIR = (170, 170, 170)
        self.BOUTON_COULEUR_FONCE = (100, 100, 100)
        self.MENU_LONGUEUR = len(self.MENU)
        self.HAUTEUR = self.SpaceGameplay.SpaceWindow.FENETRE_HAUTEUR / self.MENU_LONGUEUR

    def afficherBoutonMenu(self):
        for index, text in enumerate(self.MENU):

            text_afficher = self.POLICE_ECRITURE_BOUTON.render(text, True, self.BLANC)
            texte_largeur, texte_hauteur = text_afficher.get_size()

            if index == self.BOUTON:

                pygame.draw.rect(self.fenetre, self.BOUTON_COULEUR_CLAIR,
                                 [(self.SpaceGameplay.SpaceWindow.FENETRE_LARGEUR / 2) - self.BOUTON_LARGEUR // 2,
                                  ((self.SpaceGameplay.SpaceWindow.FENETRE_HAUTEUR / self.MENU_LONGUEUR) - self.BOUTON_HAUTEUR) + (self.HAUTEUR / 2 * index),
                                  self.BOUTON_LARGEUR, 40])

            else:  # Afficher les boutons d'une couleur normale

                pygame.draw.rect(self.fenetre, self.BOUTON_COULEUR_FONCE,
                                 [(self.SpaceGameplay.SpaceWindow.FENETRE_LARGEUR / 2) - self.BOUTON_LARGEUR // 2,
                                  ((self.SpaceGameplay.SpaceWindow.FENETRE_HAUTEUR / self.MENU_LONGUEUR) - self.BOUTON_HAUTEUR) + (self.HAUTEUR / 2 * index),
                                  self.BOUTON_LARGEUR, 40])

            self.fenetre.blit(text_afficher, ((self.SpaceGameplay.SpaceWindow.FENETRE_LARGEUR / 2) - texte_largeur // 2,
                                         (self.SpaceGameplay.SpaceWindow.FENETRE_HAUTEUR / self.MENU_LONGUEUR) - texte_hauteur + (self.HAUTEUR * index) / 2))

    def afficher_menu(self):
        controle_echap = self.SpaceGameplay.SpaceWindow.police.render(str("ECHAP : Mettre le jeu en pause"), True, self.BLANC)
        controle_mute = self.SpaceGameplay.SpaceWindow.police.render(str("M : Couper le son du jeu"), True, self.BLANC)
        fleche_vie = self.SpaceGameplay.SpaceWindow.police.render(str("Vies ►"), True, self.BLANC)
        controle_touche = pygame.image.load("Images/fleche.png")
        controle_touche = pygame.transform.scale(controle_touche, (80, 50))
        controle_touche_texte = self.SpaceGameplay.SpaceWindow.police.render(str("Controles ►"), True, self.BLANC)
        controle_espace = pygame.image.load("Images/espace.png")
        controle_espace = pygame.transform.scale(controle_espace, (120, 30))

        self.fenetre.blit(controle_echap, (0, self.SpaceGameplay.SpaceWindow.FENETRE_HAUTEUR * (6.5 / 8)))
        self.fenetre.blit(controle_mute, (0, self.SpaceGameplay.SpaceWindow.FENETRE_HAUTEUR * (7 / 8)))
        self.fenetre.blit(fleche_vie, (self.SpaceGameplay.SpaceWindow.FENETRE_LARGEUR - 6 * self.SpaceGameplay.SpaceWindow.VIE_LARGEUR, self.SpaceGameplay.SpaceWindow.FENETRE_HAUTEUR - self.SpaceGameplay.SpaceWindow.VIE_HAUTEUR + 5))
        self.fenetre.blit(controle_touche, (self.SpaceGameplay.SpaceWindow.FENETRE_LARGEUR - 140, self.SpaceGameplay.SpaceWindow.FENETRE_HAUTEUR * (6 / 8)))
        self.fenetre.blit(controle_touche_texte, (self.SpaceGameplay.SpaceWindow.FENETRE_LARGEUR - 280, self.SpaceGameplay.SpaceWindow.FENETRE_HAUTEUR * (6.3 / 8)))
        self.fenetre.blit(controle_espace, (self.SpaceGameplay.SpaceWindow.FENETRE_LARGEUR - 170, self.SpaceGameplay.SpaceWindow.FENETRE_HAUTEUR * (5 / 8)))