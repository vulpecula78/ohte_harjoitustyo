import pygame

class Computer_AI:
    def __init__(self, ball, bat2, scr_width):
        self.ball = ball
        self.bat = bat2
        self.scr_width = scr_width

    def ai_player_move(self):
        ''' When ball is on half way to computer's end, 
        bat follows the movement of the ball.'''
        if self.ball.rect.x > self.scr_width / 2 - 50 and self.ball.get_x_velocity() > 0:
            if self.ball.rect.y >= self.bat.rect.y + 50:
                self.bat.move_down()
                #self.bat.move_down()
            if self.ball.rect.y < self.bat.rect.y + 50:
                self.bat.move_up()
                #self.bat.move_up()
