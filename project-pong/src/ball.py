import pygame
import os

dirname = os.path.dirname(__file__)

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, scr_width, scr_height):
        super().__init__()

        self.image = pygame.image.load(os.path.join(dirname, "assets", "ball.png"))
        self.image.set_colorkey((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.xvelocity = 0
        self.yvelocity = 0
        self.scr_width = scr_width
        self.scr_height = scr_height

    def setVelocity(self, xvel, yvel):
        self.xvelocity = xvel
        self.yvelocity = yvel

    def setPosition(self, xpos, ypos):
        self.rect.x = xpos
        self.rect.y = ypos 

    def getXvelocity(self):
        return self.xvelocity

    def getYvelocity(self):
        return self.yvelocity

    def getXpos(self):
        xpos = self.rect.x
        return xpos
    
    def update(self):
        self.rect.x += self.xvelocity
        self.rect.y += self.yvelocity
        if self.rect.bottom >= self.scr_height - 45: #45 pixels reserved for scores
            self.rect.y = self.scr_height - 85
            self.yvelocity = -(self.yvelocity)
        if self.rect.top <= 0:
            self.yvelocity = -(self.yvelocity)
