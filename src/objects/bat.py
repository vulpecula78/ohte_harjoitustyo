'''Bat module for another pong clone again'''
import os
import pygame

dirname = os.path.dirname(__file__)

class Bat(pygame.sprite.Sprite):
    """Initializes bat with starting position and screen size.
    """
    def __init__(self, pos_x, pos_y, scr_width, scr_height):
        """Initializes bat with starting position and screen size.
        
        Args:
            pos_x: horizontal starting position.
            pos_y: vertical starting position.
            scr_width: Screen width in pixels.
            scr_height: Screen height in pixels.
        """
        super().__init__()

        self.image = pygame.image.load(os.path.join(dirname, "../assets", "bat.png"))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.scr_width = scr_width
        self.scr_height = scr_height

    def set_y_position(self, y_pos):
        """Sets new vertical position with given value.
        Bat vertical position can be set between 0 and
        screen height - 100 (bat size) - 45(score area).
        
            Args:
            y_pos: new vertical position for bat.
        """
        if 0 <= y_pos <= self.scr_height - 145:
            self.rect.y = y_pos

    def move_up(self):
        '''Moves bat up by 2 pixels, until y position is 0'''
        self._reset_x()
        if self.rect.top > 1:
            self.rect.y -= 2

    def move_down(self):
        '''Moves bat down by 2 pixels until y position is screen height - 145
            (100 from bat, 45 from score area)'''
        self._reset_x()
        if self.rect.top < self.scr_height - 145:
            self.rect.y += 2

    def hit(self):
        '''Moves bat forward to hit the ball.'''
        if self.rect.x == 5:
            self.rect.x = 25
        if self.rect.x == self.scr_width - 25:
            self.rect.x = self.scr_width - 45

    def _reset_x(self):
        '''Reset the x position of the bat.'''
        if self.rect.x == 25:
            self.rect.x = 5
        if self.rect.x == self.scr_width - 45:
            self.rect.x = self.scr_width - 25
