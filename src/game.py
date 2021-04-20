'''Game loop for Another Pong Clone Again'''
import pygame
from score  import Score
from computer_ai import ComputerAi
from wait import Wait

class Game():
    def __init__(self, ball, bat1, bat2, clock, scr_width, scr_height):
        self.bat1 = bat1
        self.bat2 = bat2
        self.ball = ball
        self.clock = clock
        self.scr_width = scr_width
        self.scr_height = scr_height
        self.wait = Wait(scr_width, scr_height)

    def main(self, fps, game_type, all_sprites, background, screen):
        '''Game main loop'''
        running = True
        pvp = True
        player2 = 2
        p1_score = 0
        p2_score = 0
        score = Score(screen, self.scr_width, self.scr_height)
        self.wait.launch(0, self.ball)
        if game_type == "computer":
            computer = ComputerAi(self.ball, self.bat2, self.scr_width)
            player2 = 3     #Set player2 to computer player.
            pvp = False

        while running:
            self.clock.tick(fps)
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q]:            # pylint: disable=no-member
                    self.bat1.move_up()
                if keys[pygame.K_z]:            # pylint: disable=no-member
                    self.bat1.move_down()
                if pvp:
                    if keys[pygame.K_UP]:           # pylint: disable=no-member
                        self.bat2.move_up()
                    if keys[pygame.K_DOWN]:         # pylint: disable=no-member
                        self.bat2.move_down()
                if event.type == pygame.QUIT:   # pylint: disable=no-member
                    running = False

            if not pvp:
                computer.ai_player_move()

            self.wait.collision(self.bat1, self.bat2, self.ball)
            running, p1_score = self.wait.is_p1_score(self.ball, p1_score, score, running, pvp)
            running, p2_score = self.wait.is_p2_score(self.ball, p2_score, score, running, player2)

            self.ball.update()
            screen.blit(background, (0,0))
            score.scores(p1_score, p2_score)
            all_sprites.draw(screen)
            pygame.display.update()
