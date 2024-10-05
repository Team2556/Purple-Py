

class NavX:
    def __init__(self):
        self.angle = 0

    def getAngle(self):
        return self.angle

    def reset(self):
        self.angle = 0

    def setAngle(self, angle):
        self.angle = angle