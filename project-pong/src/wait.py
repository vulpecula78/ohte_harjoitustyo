import pygame
from pygame.locals import *

class Wait:
    
    def wait(self, player):
        pygame.event.clear()
        
        while True:
            keypressed = pygame.event.wait()
            if keypressed.type == QUIT:
                return False
            if keypressed.type == KEYDOWN and player == 1:
                if keypressed.key == K_a:
                    return True
            if keypressed.type == KEYDOWN and player == 2:
                if keypressed.key == K_LEFT:
                    return True
