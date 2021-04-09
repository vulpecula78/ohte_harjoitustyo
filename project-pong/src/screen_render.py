
class ScreenRender():
    def __init__(self, screen, sprites, background):
        self.screen = screen
        self.background = background
        self.sprites = sprites

    def update(self):
        self.screen.blit(self.background, (0,0))
        self.sprites.draw(self.screen)
