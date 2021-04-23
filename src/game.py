'''Game loop for Another Pong Clone Again'''
import pygame
from score  import Score
from computer_ai import ComputerAi
from gamevents import Gamevents
from sound_effects import SoundEffects

class Game():
    def __init__(self, ball, bat1, bat2, clock, scr_width, scr_height, sounds):
        self.bat1 = bat1
        self.bat2 = bat2
        self.ball = ball
        self.clock = clock
        self.scr_width = scr_width
        self.scr_height = scr_height
        self.events = Gamevents(scr_width, scr_height)
        if sounds:
            self.sound = SoundEffects()
        else:
            self.sound = None

    def main(self, fps, game_type, all_sprites, background, screen, hi_score):
        '''Game main loop'''
        running = True
        pvp = True
        wall = False
        player2 = 2
        p1_score = 0
        p2_score = 0
        score = Score(screen, self.scr_width, self.scr_height, hi_score)
        if game_type == "computer":
            computer = ComputerAi(self.ball, self.bat2, self.scr_width)
            player2 = 3     #Set player2 to computer player.
            pvp = False
        elif game_type == "wall":
            pvp = False
            wall = True
            p2_score = None
        self.events.launch(0, self.ball)

        while running:
            self.clock.tick(fps)
            hit = False
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q]:            # pylint: disable=no-member
                    self.bat1.move_up()
                if keys[pygame.K_a]:            # pylint: disable=no-member
                    self.bat1.move_down()
                if keys[pygame.K_s] and not wall:   # pylint: disable=no-member
                    self.bat1.hit()
                    hit = True
                if pvp:
                    if keys[pygame.K_UP]:           # pylint: disable=no-member
                        self.bat2.move_up()
                    if keys[pygame.K_DOWN]:         # pylint: disable=no-member
                        self.bat2.move_down()
                    if keys[pygame.K_LEFT]:         # pylint: disable=no-member
                        self.bat2.hit()
                        hit = True
                if event.type == pygame.QUIT:   # pylint: disable=no-member
                    running = False

            if not pvp and not wall:
                hit = computer.ai_player_move(hit)

            if not wall:
                self.events.collision(self.bat1, self.bat2, self.ball, self.sound, hit)
                running, p1_score = self.events.is_p1_score(self.ball, \
                    p1_score, score, running, pvp, self.sound)
                running, p2_score = self.events.is_p2_score(self.ball, \
                    p2_score, score, running, player2, self.sound)
            else:
                p1_score = self.events.collision_wall(self.ball, self.bat1, p1_score, self.sound)
                running, hi_score = self.events.ball_on_table(self.ball, score, p1_score, hi_score)

            self.ball.update()
            screen.blit(background, (0,0))
            score.scores(p1_score, p2_score)
            all_sprites.draw(screen)
            pygame.display.update()

        return hi_score
