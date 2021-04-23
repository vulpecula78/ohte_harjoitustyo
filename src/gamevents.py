import random
import pygame
from pygame.locals import QUIT, KEYDOWN, K_d, K_LEFT # pylint: disable=no-name-in-module

class Gamevents:
    '''Class for handling game events'''
    def __init__(self, scr_width,scr_height):
        self.scr_width = scr_width
        self.scr_height = scr_height


    def wait(self, player):
        '''Wait for player action after scoring'''
        pygame.event.clear()
        if player == 3:
            pygame.time.delay(2000)
            return False

        while True:
            #wait for the player launch
            key_pressed = pygame.event.wait()
            if key_pressed.type == QUIT:
                return False
            if key_pressed.type == KEYDOWN and player == 1:
                if key_pressed.key == K_d:
                    return True
            if key_pressed.type == KEYDOWN and player == 2:
                if key_pressed.key == K_LEFT:
                    return True


    def launch(self, player, ball):
        '''Player1 = 1, player2 = 2, Player3 = computer, 0 = starting from the middle'''
        running = True
        if 1 <=  player <= 2:
            running = self.wait(player)
        y_velocity = random.randint(-4, 5)
        x_velocity = random.randint(3, 5)

        if player == 0:
            if random.randint(1, 3) == 2:
                player = 2
        if 2 <= player <= 3:
            if player == 3:     #if computer player, wait for 1,5s before launch
                pygame.time.delay(1500)
            x_velocity = x_velocity * -1
            xpos = self.scr_width - 80
        else:
            xpos = 80
        ypos = random.randint(20, self.scr_height - 65)
        ball.set_position(xpos, ypos)
        ball.set_velocity(x_velocity, y_velocity)
        return running


    def collision(self, bat1, bat2, ball, sound, hit):
        '''Check collision between bats and ball'''
        if pygame.sprite.collide_rect(ball, bat1) or pygame.sprite.collide_rect(ball, bat2):
            x_acc = random.randint(-1, 2)
            if hit:
                x_acc += 2
            y_acc = random.randint(-1, 2)
            xvel = ball.get_x_velocity()
            yvel = ball.get_y_velocity()
            if -xvel + x_acc == 0:
                xvel = xvel + 1
            if sound is not None:
                if hit:
                    sound.hit_sound()
                else:
                    sound.bat_sound()
            if pygame.sprite.collide_rect(ball, bat1) and ball.rect.x >= 15:
                ball.set_position(ball.rect.x + 26, ball.rect.y)
                ball.set_velocity(-xvel + x_acc, yvel + y_acc)
            elif pygame.sprite.collide_rect(ball, bat2) and ball.rect.x < self.scr_width - 55:
                ball.set_position(self.scr_width - 86, ball.rect.y) #Fix this formula
                ball.set_velocity((xvel + x_acc) * -1, yvel + y_acc)
            else:
                return


    def collision_wall(self, ball, bat1, p1_score, sound):
        if pygame.sprite.collide_rect(ball, bat1) and ball.rect.x >= 15:
            y_acc = random.randint(-2, 2)
            xvel = ball.get_x_velocity() - random.randint(-1, 2)
            yvel = ball.get_y_velocity() - (1 + y_acc)
            if sound is not None:
                sound.bat_sound()
            if ball.rect.x >= 15:
                ball.set_position(26, ball.rect.y)
            ball.set_velocity(-xvel, yvel)
            p1_score += 1
        elif ball.rect.x > 0.75 * self.scr_width - 45:
            ball.set_position(0.75 * self.scr_width - 45, ball.rect.y)
            xvel = ball.get_x_velocity() * -1
            ball.set_velocity(xvel, ball.get_y_velocity())
            if sound is not None:
                sound.bat_sound()
        return p1_score


    def ball_on_table(self, ball, score, p1_score, hi_score):
        if ball.rect.x < -40:
            high = score.wall_game_over(p1_score)
            self.wait(1)
            return False, high
        return True, hi_score


    def is_p2_score(self, ball, p2_score, score, running, player2, sound):
        if ball.rect.x < -40:
            p2_score += 1
            if sound is not None:
                sound.cheer_sound()
            #Player 2 wins if xx pts
            if p2_score == 3:
                score.victory(player2)
                self.wait(player2)
                running = False
                return running, p2_score
            score.player_scores(2)
            pygame.display.update()
            running = self.launch(1, ball)
        return running, p2_score


    def is_p1_score(self, ball, p1_score, score, running, pvp, sound):
        if ball.rect.x > self.scr_width:
            p1_score += 1
            if sound is not None:
                sound.cheer_sound()
            #Player 1 wins if xx pts
            if p1_score == 3:
                score.victory(1)
                self.wait(1)
                running = False
                return running, p1_score
            score.player_scores(1)
            pygame.display.update()
            if pvp:
                running = self.launch(2, ball)
            else:
                running = self.launch(3, ball)
        return running, p1_score
