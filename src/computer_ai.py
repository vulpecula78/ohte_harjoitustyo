class ComputerAi:
    def __init__(self, ball, bat2, scr_width):
        self.ball = ball
        self.bat = bat2
        self.scr_width = scr_width

    def ai_player_move(self, hit):
        ''' When ball is on half way to computer's end,
        bat follows the movement of the ball. If the speed of the ball is
        low enough and is close enough hit the ball.'''
        if self.ball.rect.x > self.scr_width - 86 and self.ball.get_x_velocity() < 5:
            if self.bat.rect.y < self.ball.rect.y < self.bat.rect.y + 60:
                self.bat.hit()
                return True
        if self.ball.rect.x > self.scr_width / 2 - 50 and self.ball.get_x_velocity() > 0:
            if self.ball.rect.y >= self.bat.rect.y + 50:
                self.bat.move_down()
                self.bat.move_down()
            if self.ball.rect.y < self.bat.rect.y + 50:
                self.bat.move_up()
                self.bat.move_up()
        return hit
