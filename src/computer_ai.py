class ComputerAi:
    """Class for computer to control bat"""
    def __init__(self, ball, bat2, scr_width, ai_lvl):
        """Computer ai is initialized with ball and bat objects,
        screen width and ai level.

        Args:
            ball: Ball object.
            bat2: bat object.
            scr_width: screen width in pixels.
            ai_lvl: String, "easy" or "average"
        """
        self.ball = ball
        self.bat = bat2
        self.scr_width = scr_width
        self.ai_lvl = ai_lvl
        if self.ai_lvl == "easy":
            self.hit_vel = 5
        else:
            self.hit_vel = 7

    def ai_player_move(self, hit):
        ''' When ball is on half way to computer's end,
        bat follows the movement of the ball. If the speed of the ball is
        low enough and is close enough hit the ball.

        Args:
            hit: bool, True or False

        Returns:
            hit: bool, True or False.
        '''
        if self.ball.rect.x > self.scr_width - 86 and self.ball.get_x_velocity() < self.hit_vel:
            if self.bat.rect.y < self.ball.rect.y < self.bat.rect.y + 60:
                self.bat.hit()
                return True
        if self.ball.rect.x > self.scr_width / 2 - 60 and self.ball.get_x_velocity() > 0:
            if self.ball.rect.y >= self.bat.rect.y + 50:
                self.bat.move_down()
                if self.ai_lvl != "easy":
                    self.bat.move_down()
            if self.ball.rect.y < self.bat.rect.y + 50:
                self.bat.move_up()
                if self.ai_lvl != "easy":
                    self.bat.move_up()
        return hit
