import random
import pygame
from pygame.locals import QUIT, KEYDOWN, K_a, K_LEFT # pylint: disable=no-name-in-module

class Wait:
    def __init__(self, scr_width,scr_height):
        self.scr_width = scr_width
        self.scr_height = scr_height

    def wait(self, player):
        '''Wait for player action after scoring'''
        pygame.event.clear()
        if player == 3:
            pygame.time.delay(2000)
            return

        while True:
            '''wait for the player launch'''
            key_pressed = pygame.event.wait()
            if key_pressed.type == QUIT:
                return False
            if key_pressed.type == KEYDOWN and player == 1:
                if key_pressed.key == K_a:
                    return True
            if key_pressed.type == KEYDOWN and player == 2:
                if key_pressed.key == K_LEFT:
                    return True

    def launch(self, player, ball):
        '''Player1 = 1, player2 = 2, Player3 = computer, 0 = starting from the middle'''
        running = True
        if player == 1 or player == 2:
            running = self.wait(player)
        y_velocity = random.randint(-4, 5)
        x_velocity = random.randint(2, 6)

        if player == 0:
            if random.randint(1, 3) == 2:
                player = 2
        if player == 2 or player == 3:
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

    def collision(self, bat1, bat2, ball):
        '''Check collision between bats and ball'''
        if pygame.sprite.collide_rect(ball, bat1) or pygame.sprite.collide_rect(ball, bat2):
            x_acc = random.randint(0, 2)
            y_acc = random.randint(-1, 2)
            xvel = ball.get_x_velocity()
            yvel = ball.get_y_velocity()
            if pygame.sprite.collide_rect(ball, bat1) and ball.rect.x >= 20:
                ball.set_position(26, ball.rect.y)
            elif pygame.sprite.collide_rect(ball, bat2) and ball.rect.x < self.scr_width - 20:
                ball.set_position(self.scr_width - 66, ball.rect.y)
                if -xvel + x_acc == 0:
                    xvel = xvel + 1
            else:
                return
            ball.set_velocity(-xvel + x_acc, yvel + y_acc)
