import pygame
import os

dirname = os.path.dirname(__file__)

class Bat(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.image = pygame.image.load(os.path.join(dirname,
                                                    "assets", "bat.png"))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y        

    def setYposition(self, yPos):
        if yPos >= 0 and yPos <= 500:#Change to screen height variable
            self.rect.y = yPos

    def moveUp(self):
        if self.rect.top > 1:
            self.rect.y -= 2

    def moveDown(self):
        if self.rect.top < 499: #Change to screen height variable
            self.rect.y += 2

        
        
