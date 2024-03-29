######CONSTANTES#######
# Couleur
ESPACE = (0, 0, 15)
BLANC = (255, 255, 255)
BLEU = (129, 78, 216)
ROUGE = (255, 0, 0)
VERT = (0,255,0)
ORANGE = (255, 165, 0)
JAUNE = (255,255,0)
VERT_CLAIR = (51,255,51)
GRIS = (128,128,128)
CYAN = (51,255,255)

BOUTON_COULEUR_CLAIR = (170, 170, 170)
BOUTON_COULEUR_FONCE = (100, 100, 100)

# Etoile en fond
NOMBRE_ETOILES = 500
NOMBRE_UFO = 5
NOMBRE_TROU_NOIR = 5
NOMBRE_BONUS = 5


# Dimension Fenetre
FENETRE_LARGEUR = 1080
FENETRE_HAUTEUR = 720

# Données Vaisseau
VAISSEAU_LARGEUR = 70
VAISSEAU_HAUTEUR = 60
DEPLACEMENT_VAISSEAU = 7

# Dimension UFO
UFO_TAILLE = 80

# Données trous noirs
TROU_NOIR_TAILLE = 80
FREQUENCE_APPARITION_TROU_NOIR = 500

#Données bonus
BONUS_TAILLE = 40
FREQUENCE_APPARITION_BONUS = 1000

# Apparence vie
VIE_LARGEUR = 30
VIE_HAUTEUR = 25

# dimension planete
TAILLE_PLANETE = int(FENETRE_LARGEUR / 6)

# Pose Planete et vaisseau
POSE_PLANETE = (
    'Planete1', 'Planete2', 'Planete3', 'Planete4', 'Planete5', 'Planete6', 'Planete7', 'Planete8', 'Planete9',
    'Planete10',
    'Planete11', 'Planete12', 'Planete13', 'Planete14', 'Planete15', 'Planete16')
POSE_VAISSEAU_SANS_FLAMME = ('vaisseau_jaune_sans_flamme','vaisseau_bleu_sans_flamme', 'vaisseau_vert_sans_flamme','vaisseau_rose_sans_flamme', 'vaisseau_blanc_sans_flamme','vaisseau_rouge_sans_flamme')
POSE_VAISSEAU_FLAMME = ('vaisseau_jaune_avec_flamme','vaisseau_bleu_avec_flamme', 'vaisseau_vert_avec_flamme','vaisseau_rose_avec_flamme', 'vaisseau_blanc_avec_flamme','vaisseau_rouge_avec_flamme')

# Vitesse du Jeu
VITESSE_JEU = 3
VITESSE_JEU_AVANT_BONUS = VITESSE_JEU
# Données tir (en facile de base)
MUNITIONS = 20
AJOUT_MUNITION = 20
VITESSE_MISSILE = 15
FREQUENCE_TIR = 180

# Score et compteur
SCORE = 0
COMPTEUR_BOUCLE = 0
COMPTEUR_PAUSE = 0
COMPTEUR_COLLISION = 0
COMPTEUR_NOTIF = 180
COMPTEUR_MUTE = 1
COMPTEUR_BONUS = 0
NOMBRE_VIE = 3
MEILLEURS_SCORE = []

# CONSTANTE POUR LE MENU
MENU = ['Jouer', 'Facile>', 'Quitter']
MENU_PAUSE = ['REPRENDRE', 'QUITTER']
CHOIX_MENU = 1
MENU_LONGUEUR = len(MENU)
MENU_PAUSE_LONGUEUR = len(MENU_PAUSE)
HAUTEUR = FENETRE_HAUTEUR / MENU_LONGUEUR
HAUTEUR_PAUSE = FENETRE_HAUTEUR / MENU_PAUSE_LONGUEUR
BOUTON_LARGEUR = 220
BOUTON_HAUTEUR = 41
BOUTON = 0

# DECLARATION DES LISTES
LISTE_PLANETE = []
PLANETE_EN_LISTE = []
LISTE_UFO = []
UFO_EN_LISTE = []
MISSILE_UFO = []
MISSILE_UFO_EN_LISTE = []
LISTE_TROU_NOIR = []
TROU_NOIR_EN_LISTE = []
COULOIRS = []
missile = []
BONUS_LISTE = []
BONUS_EN_LISTE = []

#Son
SON_EN_PAUSE = False
SON_EN_COURS = False



########FIN CONSTANTE#######