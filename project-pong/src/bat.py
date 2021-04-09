import pygame
import os

dirname = os.path.dirname(__file__)

class Bat(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, scr_width, scr_height):
        super().__init__()

        self.image = pygame.image.load(os.path.join(dirname,
                                                    "assets", "bat.png"))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.scr_width = scr_width
        self.scr_height = scr_height

    def setYposition(self, yPos):
        if yPos >= 0 and yPos <= self.scr_height - 145: #45 pixels for scores
            self.rect.y = yPos

    def moveUp(self):
        if self.rect.top > 1:
            self.rect.y -= 2

    def moveDown(self):
        if self.rect.top < self.scr_height - 145: #45 pixels for scores
            self.rect.y += 2

        
        
