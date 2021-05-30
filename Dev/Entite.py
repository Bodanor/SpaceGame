
class Entite():
    def __init__(self):
        self.visible = True
        self.position = [0,0]
        self.image = None
        self.listeImage = {}
        self.couloir = 0

    def visible(self):
        self.visible = True


    def invisible(self):
        self.visible = False


    def estVisible(self):
        return self.visible


    def place(self, x ,y, couloir):
        self.position[0] = x
        self.position[1] = y
        self.couloir = couloir


    def position(self):
        return self.position


    def afficherCouloir(self):
        return self.couloir


    def prendsPose(self, pose):
        self.image = pose
