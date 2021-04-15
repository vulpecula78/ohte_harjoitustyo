'''Game loop for Another Pong Clone Again'''
import random
import pygame
from wait import Wait

class Game():
    def __init__(self, render, score, ball, bat1, bat2, clock, scr_width, scr_height):
        self.render = render
        self.bat1 = bat1
        self.bat2 = bat2
        self.ball = ball
        self.score = score
        self.clock = clock
        self.scr_width = scr_width
        self.scr_height = scr_height
        self.wait = Wait()

    def launch(self, player):
        running = True
        if player != 0:
            running = self.wait.wait(player)
        y_velocity = random.randint(-4, 5)
        x_velocity = random.randint(2, 6)

        if player == 0:
            if random.randint(1, 3) == 2:
                player = 2

        if player == 2:
            x_velocity = x_velocity * -1
            xpos = self.scr_width - 80
        else:
            xpos = 80

        ypos = random.randint(20, self.scr_height - 65)
        self.ball.set_position(xpos, ypos)
        self.ball.set_velocity(x_velocity, y_velocity)
        return running

    def main(self, fps):
        '''Game main loop'''
        running = True
        p1_score = 0
        p2_score = 0
        self.launch(0)

        while running:
            self.clock.tick(fps)
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q]:            # pylint: disable=no-member
                    self.bat1.move_up()
                if keys[pygame.K_z]:            # pylint: disable=no-member
                    self.bat1.move_down()
                if keys[pygame.K_UP]:           # pylint: disable=no-member
                    self.bat2.move_up()
                if keys[pygame.K_DOWN]:         # pylint: disable=no-member
                    self.bat2.move_down()
                if event.type == pygame.QUIT:   # pylint: disable=no-member
                    running = False

            if pygame.sprite.collide_rect(self.ball, self.bat1) or \
                pygame.sprite.collide_rect(self.ball, self.bat2):
                x_acc = random.randint(0, 2)
                y_acc = random.randint(-1, 2)
                xvel = self.ball.get_x_velocity()
                yvel = self.ball.get_y_velocity()
                if pygame.sprite.collide_rect(self.ball, self.bat1):
                    self.ball.set_position(26, self.ball.rect.y)
                else:
                    self.ball.set_position(self.scr_width - 66, self.ball.rect.y)
                    if -xvel + x_acc == 0:
                        xvel = xvel + 1
                self.ball.set_velocity(-xvel + x_acc, yvel + y_acc)

            if self.ball.rect.x < -20:
                p2_score += 1
                #Player 2 wins 
                self.score.player_scores(2)
                pygame.display.update()
                running = self.launch(1)

            if self.ball.rect.x > self.scr_width:
                p1_score += 1
                self.score.player_scores(1)
                pygame.display.update()
                running = self.launch(2)

            self.ball.update()
            self.render.update()
            self.score.scores(p1_score, p2_score)
            pygame.display.update()
