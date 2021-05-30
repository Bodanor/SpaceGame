import pygame
import Affichage
import Sound
import Entite
print("Initialisation...")
pygame.mixer.init()
SpaceWindow = Affichage.SpaceWindow('Space Game')
SpaceSound = Sound.SpaceSound()

chris = Entite.Entite()
chris.prendsPose(SpaceWindow.images['UFOImg'])

running = True
while running:
    SpaceWindow.fenetre.fill(SpaceWindow.ESPACE)
    SpaceWindow.dessiner(chris)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

