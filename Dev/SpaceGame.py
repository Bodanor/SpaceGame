import pygame
import Affichage
import Sound

print("Initialisation...")
pygame.mixer.init()
SpaceWindow = Affichage.SpaceWindow('Space Game')
SpaceSound = Sound.SpaceSound()
while True:
    pygame.display.flip()

