import pygame, time,sys, random

#Initialisation de PYGAME :
pygame.init()

#Changement d'icone pour le jeu :
iconejeu = pygame.image.load('Images/vaisseau_sans_flamme.png')
pygame.display.set_icon(iconejeu)

#Dictionnaire contennant le nom donner et le nom du fichier (permet le chargement de toute les images:
Images = {}


#Variables Constantes de la fenêtre :
FENETRE_LARGEUR = 800
FENETRE_HAUTEUR = 800

#Création de la fenetre:

fenetre = pygame.display.set_mode((FENETRE_LARGEUR, FENETRE_HAUTEUR))
pygame.display.set_caption('SpaceGame')


#Variables Constantes des couleurs ET POLICE:
NOIR = (0,0,0)
BLANC = (255,255,255)
BOUTON_COULEUR_CLAIR = (170,170,170)
BOUTON_COULEUR_FONCE = (100,100,100)
POLICE_ECRITURE_BOUTON = pygame.font.SysFont('Corbel',36)


#Liste Des textes pour menus :
TEXTES = ['Jouer','Quitter']
NOMBRES_TEXTES_MENU = len(TEXTES)

#Variables pour la taille du vaisseau :
VAISSEAU_LARGEUR = 60
VAISSEAU_HAUTEUR = 51

largeurfenetre = fenetre.get_width()
hauteurfenetre = fenetre.get_height()



def chargerToutesImages():
    for nom, nom_fichier in (('imagejeu', 'vaisseau_avec_flamme.png'),
                             ('vaisseau_sans_flammes','vaisseau_sans_flamme.png'),
                             ('vaisseau_avec_flammes','vaisseau_avec_flamme.png'),
                             ('planete1', 'planete1.png'),
                             ('planete2','planete2.png'),
                             ('planete3','planete3.png'),
                             ('planete4','planete4.png'),
                             ('planete5','planete5.png'),
                             ('planete6','planete6.png'),
                             ('planete7', 'planete7.png'),
                             ('planete8', 'planete8.png'),
                             ('planete9', 'planete9.png'),
                             ('planete10', 'planete10.png'),
                             ('planete11', 'planete11.png'),
                             ('planete12', 'planete12.png'),
                             ('planete13', 'planete13.png'),
                             ('planete14', 'planete14.png'),
                             ('planete15', 'planete15.png'),
                             ('planete16', 'planete16.png')):

        chemin = 'Images/' +nom_fichier
        if nom == 'vaisseau_sans_flammes' or nom == 'vaisseau_avec_flammes':
            image = pygame.image.load(chemin).convert_alpha(fenetre)
            image = pygame.transform.scale(image, (VAISSEAU_LARGEUR, VAISSEAU_HAUTEUR))

        else:
            image = pygame.image.load(chemin).convert_alpha(fenetre)

        Images[nom] = image




print("Chargement des Images ...")
chargerToutesImages()
print("Images Chargée !")

def afficherBoutonMenu():

    hauteur = hauteurfenetre / NOMBRES_TEXTES_MENU

    for index, text in enumerate(TEXTES):

        if largeurfenetre / 2 - 70 <= mouse[0] <= largeurfenetre / 2 + 70 and (hauteurfenetre / 2 - 20) + (
                hauteur / 2 * index) <= mouse[
            1] <= (hauteurfenetre / 2 + 20) + (hauteur / 2 * index):
            pygame.draw.rect(fenetre, BOUTON_COULEUR_CLAIR,
                             [(largeurfenetre / 2) - 70, ((hauteurfenetre / 2) - 20) + (hauteur / 2 * index), 140, 40])

        else:
            pygame.draw.rect(fenetre, BOUTON_COULEUR_FONCE,
                             [(largeurfenetre / 2) - 70, ((hauteurfenetre / 2) - 20) + (hauteur / 2 * index), 140, 40])

        text_afficher = POLICE_ECRITURE_BOUTON.render(text, True, BLANC)

        fenetre.blit(text_afficher, ((largeurfenetre / 2) - text_afficher.get_width() // 2,
                                     (hauteurfenetre / 2) - (text_afficher.get_height() - (hauteur * index)) // 2))


#SECTIONS BOUCLE INTRO:

while True:

    for evenement in pygame.event.get():

        if evenement.type == pygame.MOUSEBUTTONDOWN:
            if largeurfenetre / 2 - 70 <= mouse[0] <= largeurfenetre / 2 + 70 and hauteurfenetre / 2 - 20 <= mouse[
                1] <= hauteurfenetre / 2 + 20:
                pygame.quit()

            if largeurfenetre / 2 - 70 <= mouse[0] <= largeurfenetre / 2 + 70 and (hauteurfenetre / 2 - 20) + 133 <= \
                    mouse[
                        1] <= (hauteurfenetre / 2 + 20) + 266:
                pygame.quit()


    fenetre.fill(NOIR)
    mouse = pygame.mouse.get_pos()

    afficherBoutonMenu()

    pygame.display.update()


    #entrées (Maxime)
# def ajuster_altitude_vaisseau(y):
#     global altitude_vaisseau
#
#     position_max = FENETRE_HAUTEUR - 50 - image_vaisseau.get_height() // 2
#
#     if y > position_max:
#        y = position_max
#
#     altitude_vaisseau = (altitude_vaisseau * 5.0 + y) / 6.0
#     return
#
# altitude_vaisseau = FENETRE_HAUTEUR / 2
#





#SECTIONS BOUCLE PRINCIPALE :

# for evenement in pygame.event.get():
#     if evenement.type == pygame.QUIT:
#         pygame.quit()
#         sys.exit();
#      elif evenement.type == pygame.MOUSEMOTION:
#           ajuster_altitude_vaisseau(evenement.pos[1])