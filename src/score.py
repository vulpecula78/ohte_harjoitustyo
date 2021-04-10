import pygame

class Score:
    def __init__(self, screen, scr_width, scr_height):
        self.screen = screen
        self.scr_width = scr_width
        self.scr_height = scr_height
        self.txtcol = (175, 225, 150)

    def scores(self, player1, player2):
        p_1 = str(player1)
        p_2 = str(player2)
        font = pygame.font.Font(pygame.font.match_font('arial'), 32)
        score_p1 = font.render(p_1, True, self.txtcol)
        score_p2 = font.render(p_2, True, self.txtcol)
        score1 = score_p1.get_rect()
        score2 = score_p2.get_rect()
        score1.midtop = (0.28 * self.scr_width, self.scr_height - 40)
        score2.midtop = (0.72 * self.scr_width, self.scr_height - 40)
        self.screen.blit(score_p1, score1)
        self.screen.blit(score_p2, score2)
