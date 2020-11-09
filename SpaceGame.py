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
TEXTES = ['Jouer', 'Multijoueur','Quitter']
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
                             ('planete4','planete4.png')):
        chemin = 'Images/' +nom_fichier
        if nom == 'vaisseau_sans_flammes' or nom == 'vaisseau_avec_flammes':
            image = pygame.image.load(chemin).convert_alpha(fenetre)
            image = pygame.transform.scale(image, (VAISSEAU_LARGEUR, VAISSEAU_HAUTEUR))

        else:
            image = pygame.image.load(chemin).convert_alpha(fenetre)

        Images[nom] = image




def dessineBouton(list_text, nombre_boutons):

    hauteur = hauteurfenetre / nombre_boutons


    for index, text in enumerate(list_text):

        if largeurfenetre / 2 - 70 <= mouse[0] <= largeurfenetre / 2 + 70 and (hauteurfenetre / 2 - 20) + (hauteur/2*index)<= mouse[
            1] <= (hauteurfenetre / 2 + 20) +(hauteur/2*index):
            pygame.draw.rect(fenetre, BOUTON_COULEUR_CLAIR,
                             [(largeurfenetre / 2) - 70, ((hauteurfenetre / 2) - 20) + (hauteur/2*index), 140, 40])

        else:
            pygame.draw.rect(fenetre, BOUTON_COULEUR_FONCE,
                             [(largeurfenetre / 2) - 70, ((hauteurfenetre / 2) - 20) + (hauteur/2*index), 140, 40])




        text_afficher = POLICE_ECRITURE_BOUTON.render(text, True, BLANC)

        fenetre.blit(text_afficher, ((largeurfenetre / 2) - text_afficher.get_width() // 2, (hauteurfenetre / 2) - (text_afficher.get_height()-(hauteur*index))// 2))


print("Chargement des Images ...")
chargerToutesImages()
print("Images Chargée !")



#SECTIONS BOUCLE INTRO:

while True:

    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()

        if evenement.type == pygame.MOUSEBUTTONDOWN:
            if largeurfenetre/2-70 <= mouse[0] <= largeurfenetre/2+70 and hauteurfenetre/2-20 <= mouse[1] <= hauteurfenetre/2+20:
                pygame.quit()

    fenetre.fill(NOIR)

    mouse = pygame.mouse.get_pos()


    dessineBouton(TEXTES, NOMBRES_TEXTES_MENU)


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