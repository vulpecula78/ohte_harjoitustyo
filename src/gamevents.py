import random
import pygame
from pygame.locals import QUIT, KEYDOWN, K_s, K_LEFT # pylint: disable=no-name-in-module

WIN = 5 #Score, that is  needed to win the game.

class Gamevents:
    '''Class for handling game events such as scoring, collisions,
    launching ball.'''
    def __init__(self, scr_width, scr_height):
        """Initializes Gamevents.

        Args:
            scr_width: screen width in pixels.
            scr_height: screen height in pixels.
        """
        self.scr_width = scr_width
        self.scr_height = scr_height


    def wait(self, player):
        '''Waits for player to press key or computer to wait 2s.

        Args:
            player: the player which is being waited for. 1 = player1,
                    2 = player2 and 3 = computer.

        Returns: Boolean for running status.
        '''
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
                if key_pressed.key == K_s:
                    return True
            if key_pressed.type == KEYDOWN and player == 2:
                if key_pressed.key == K_LEFT:
                    return True


    def launch(self, player, ball):
        """Launch ball into game in the beginning or wait for a player to
        launch ball back into game after scoring.

        Args:
            player: player to launch the ball. 1 = player1, 2 = player2,
                    3 = computer and 0 = starting from the middle
            ball: ball object getting the direction and speed.

        Returns: Boolean, running true or false.
        """
        running = True
        if 1 <=  player <= 2:
            running = self.wait(player)
        else: #if computer player, wait for 1,5s before launch
            pygame.time.delay(1500)

        y_velocity = random.randint(-4, 5)
        x_velocity = random.randint(3, 5)

        if player == 0:
            if random.randint(1, 2) == 2:
                player = 2
        if 2 <= player <= 3:
            x_velocity = x_velocity * -1
            xpos = self.scr_width - 80
        else:
            xpos = 80
        ypos = random.randint(20, self.scr_height - 65)
        ball.set_position(xpos, ypos)
        ball.set_velocity(x_velocity, y_velocity)
        return running


    def collision(self, bat1, bat2, ball, sound, hit):
        '''Check collision between bats and ball in 2 player or
        player versus computer gamemodes. Changes balls direction
        when hit on bat.

        Args:
            bat1: Bat object for player1
            bat2: Bat object for player2 or computer
            ball: ball object
            sound: None or sound objects. Defines if the sounds effects are played.
            hit: Boolean, if True gives little more horizontal velocity for the ball.

        Returns:
            None.
        '''
        if pygame.sprite.collide_rect(ball, bat1) or pygame.sprite.collide_rect(ball, bat2):
            x_acc = random.randint(-1, 2)
            if hit:
                x_acc += 2
            y_acc = random.randint(-1, 2)
            xvel = ball.get_x_velocity()
            yvel = ball.get_y_velocity()
            if -(xvel + -x_acc) == 0 or (xvel + x_acc) == 0:
                xvel = xvel + 1
            if sound is not None:
                if hit:
                    sound.hit_sound()
                else:
                    sound.bat_sound()
            if pygame.sprite.collide_rect(ball, bat1) and ball.rect.x >= 15:
                ball.set_position(46, ball.rect.y)
                ball.set_velocity(-(xvel + -x_acc), yvel + y_acc)
            elif pygame.sprite.collide_rect(ball, bat2) and ball.rect.x <= self.scr_width - 55:
                ball.set_position(self.scr_width - 87, ball.rect.y)
                ball.set_velocity((xvel + x_acc) * -1, yvel + y_acc)
            return


    def collision_wall(self, ball, bat1, p1_score, sound):
        """Checks collision between ball and bat and also between ball and
        back wall. Changes direction of ball on collision and counts the score.

        Args:
            ball: ball object
            bat1: bat object
            p1_score: Points for player1.
            sound: None or sound objects. Defines if the sounds effects are played.

        Returns:
            p1_score: Currents score.
        """
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


    def ball_on_table(self, ball, score, p1_score, hiscore, running):
        """Checks if the ball stays on the table in against the wall game mode.
        If ball gets out, the game end.

        Args:
            ball: the ball object
            score: score object
            p1_score: points for player1
            hiscore: current hiscore.
            running: Boolean, game continues?

        Returns:
            running: False if ball gets out and game over.
            hiscore: current hiscore.
        """
        if ball.rect.x < -40:
            high = score.wall_game_over(p1_score)
            self.wait(1)
            return False, high
        return running, hiscore


    def is_p2_score(self, ball, p2_score, score, running, player2, sound):
        """Checks scoring and victory condition for player2.

        Args:
            ball: the ball object.
            p2_score: player 2 current score.
            score: score object.
            running: Boolean, game still continues?
            player2: integer. 2 if human player, 3 if computer.
            sound: sound object or None

        Returns:
            running: True, if score less than WIN variable.
            p2_score: player 2 current score.
        """
        if ball.rect.x < -40:
            p2_score += 1
            if sound is not None:
                sound.cheer_sound()
            if p2_score == WIN:
                score.victory(player2)
                self.wait(player2)
                running = False
                return running, p2_score
            score.player_scores(2)
            pygame.display.update()
            running = self.launch(1, ball)
        return running, p2_score


    def is_p1_score(self, ball, p1_score, score, running, game_type, sound):
        """Checks scoring and victory condition for player1.

        Args:
            ball: the ball object.
            p1_score: player 1 current score.
            score: score object.
            running: Boolean, game still continues?
            game_type: String "pvp" or "computer" to determine that is the
                      ball launched back to game by player or computer.
            sound: sound object or None

        Returns:
            running: True, if score less than WIN variable.
            p1_score: player 1 current score.
        """
        if ball.rect.x > self.scr_width:
            p1_score += 1
            if sound is not None:
                sound.cheer_sound()
            if p1_score == WIN:
                score.victory(1)
                self.wait(1)
                running = False
                return running, p1_score
            score.player_scores(1)
            pygame.display.update()
            if game_type == "pvp":
                running = self.launch(2, ball)
            else:
                running = self.launch(3, ball)
        return running, p1_score
