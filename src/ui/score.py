import pygame

class Score:
    '''Score class prints scores on the screen, handles scoring, game over
    and victory conditions'''
    def __init__(self, screen, scr_width, scr_height, hiscore):
        """Score class is initialized by screen, screen size and hiscore

        Args:
            screen: pygame display module initialized in main.py
            scr_width: Screen width in pixels.
            scr_height: Screen hight in pixels.
            hiscore: Against wall game hiscore.
        """
        self.screen = screen
        self.scr_width = scr_width
        self.scr_height = scr_height
        self.hiscore = hiscore
        self.txtcol = (185, 225, 150)

    def scores(self, p1_points, p2_points):
        """Prints scores on the screen.

        Args:
            p1_points, p2_points: Integers, current player scores.
        """
        p_1 = str(p1_points)
        font = pygame.font.Font(pygame.font.match_font('arial'), 32)
        score_p1 = font.render(p_1, True, self.txtcol)
        score1 = score_p1.get_rect()
        score1.midtop = (0.28 * self.scr_width, self.scr_height - 40)
        if p2_points is not None:
            p_2 = str(p2_points)
            score_p2 = font.render(p_2, True, self.txtcol)
            score2 = score_p2.get_rect()
            score2.midtop = (0.72 * self.scr_width, self.scr_height - 40)
            self.screen.blit(score_p2, score2)
        else:
            high = font.render('HiScore: %s' % self.hiscore , True, self.txtcol)
            high_rect = high.get_rect()
            high_rect.midtop = (0.65 * self.scr_width, self.scr_height - 40)
            self.screen.blit(high, high_rect)
        self.screen.blit(score_p1, score1)

    def player_scores(self, player):
        """Prints message on screen when somebody scores.

        Args:
            player: Int, player number
        """
        font = pygame.font.Font(pygame.font.match_font('arial'), 40)
        text = font.render('Player %s Scores!!!' % player, True, self.txtcol)
        text_rect = text.get_rect(center=(self.scr_width/2, 200))
        self.screen.blit(text, text_rect)

    def victory(self, player):
        """Prints victory message on the screen, when player winst the game.

        Args:
            player: Int, player number
        """
        font = pygame.font.Font(pygame.font.match_font('arial'), 44)
        if player != 3:
            text = font.render('PLAYER %s WINS!!!' % player, True, (255, 215, 0))
        else:
            text = font.render('COMPUTER WINS!!!', True, (255, 215, 0))
        text_rect = text.get_rect(center=(self.scr_width/2, 200))
        self.screen.blit(text, text_rect)
        pygame.display.update()

    def wall_game_over(self, score):
        """Prints message on the screen when game is over in againts the wall mode.

        Args:
            score: Int, current score

        returns:
            hiscore: Int, New or old hiscore."""
        font = pygame.font.Font(pygame.font.match_font('arial'), 42)
        if score > self.hiscore:
            self.hiscore = score
            text = font.render('New HiScore: %s' % score, True, (255, 215, 0))
        else:
            text = font.render('Game Over!', True, self.txtcol)
        text_rect = text.get_rect(center=(self.scr_width/2, 200))
        self.screen.blit(text, text_rect)
        pygame.display.update()
        return self.hiscore
