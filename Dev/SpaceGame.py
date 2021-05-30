import pygame
import Affichage
import Sound

print("Initialisation...")
pygame.mixer.init()
SpaceWindow = Affichage.SpaceWindow('Space Game')
SpaceSound = Sound.SpaceSound()
running = True
while running:
    SpaceWindow.fenetre.fill(SpaceWindow.ESPACE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

