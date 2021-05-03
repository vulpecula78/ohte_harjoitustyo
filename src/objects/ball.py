'''Ball class for Another Pong Clone Again'''
import os
import pygame

dirname = os.path.dirname(__file__)

class Ball(pygame.sprite.Sprite):
    """Class for handling ball sprite.
    
    Attributes:
        pos_x: Balls horizontal position.
        pos_y: Balls vertical position.
        x_velocity: How many pixels balls horizontal position changes in every update.
        y_velocity: How many pixels balls vertical position changes in every update.
    """
    
    def __init__(self, pos_x, pos_y, scr_width, scr_height):
        """initializes ball object
    
        Args:
            pos_x: Balls horizontal position.
            pos_y: Balls vertical position.
            scr_width: Screen width in pixels.
            scr_height: Screen height in pixels.
        """
        super().__init__()

        self.image = pygame.image.load(os.path.join(dirname, "../assets", "ball.png"))
        self.image.set_colorkey((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.x_velocity = 0
        self.y_velocity = 0
        self.scr_width = scr_width
        self.scr_height = scr_height

    def set_velocity(self, xvel, yvel):
        """Set balls velocity with x and y component. Limits velocities
        to |10| pixels. Y_velocity doesn't change if values more than 10
        is given.
        
        Args:
            xvel: new horizontal velocity.
            yvel: new vertical velocity.            
        """                
        if xvel < -10:
            self.x_velocity = -10
        elif xvel > 10:
            self.x_velocity = 10
        else:
            self.x_velocity = xvel
        if -11 < yvel < 11:
            self.y_velocity = yvel

    def set_position(self, x_pos, y_pos):
        """Set ball position with given x and y coordinate.
        
        Args:
            x_pos: new horizontal position.
            y_pos: new vertical position.
        """
        self.rect.x = x_pos
        self.rect.y = y_pos

    def get_x_velocity(self):
        """Returns balls horizontal velocity.
        
        Returns:
            x_velocity: Balls horizontal velocity.
        """
        return self.x_velocity

    def get_y_velocity(self):
        """Returns balls vertical velocity.
        
        Returns:
            y_velocity: balls vertical velocity.
        """
        return self.y_velocity

    def update(self):
        '''Updates ball location and changes direction if hitting top or bottom border.'''
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity
        if self.rect.bottom >= self.scr_height - 45: #45 pixels reserved for scores
            self.rect.y = self.scr_height - 85
            self.y_velocity = -(self.y_velocity)
        if self.rect.top <= 0:
            self.rect.y = 0
            self.y_velocity = -(self.y_velocity)
