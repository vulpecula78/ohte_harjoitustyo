import pygame

class Screen_render():
    def __init__(self, screen, display, sprites, background):
        self.display = pygame.display
        self.screen = screen
        self.background = background
        self.sprites = sprites
    
    def update(self):      
        self.screen.blit(self.background, (0,0))
        self.sprites.draw(self.screen)
        #self.display.update()
