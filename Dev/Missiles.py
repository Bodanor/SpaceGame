class Missile():
    def __init__(self, SpaceGameplay):
        self.visible = True
        self.position = [0, 0]
        self.vitesse_missile = SpaceGameplay.VITESSE_MISSILE

    def visibleMissile(self):
        self.visible = True

    def invisibleMissile(self):
        self.visible = False

    def estVisibleMissile(self):
        return self.visible

    def placeMissile(self, x, y):
        self.position[0] = x
        self.position[1] = y

    def positionMissile(self):
        return self.position


    def deplace_missile(self, vitesse_missile):
        position_y = self.position[1] - vitesse_missile
        self.placeMissile(self.position[0], position_y)

