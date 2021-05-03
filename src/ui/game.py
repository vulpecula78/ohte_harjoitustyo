'''Game loop for Another Pong Clone Again'''
import pygame
from ui.score  import Score
from computer_ai import ComputerAi
from gamevents import Gamevents
from sound_effects import SoundEffects

FPS = 120

class Game():
    """Game class holds main loop for game play. Draws the objects on the screen
    and reads the keyboard.
    """
    def __init__(self, ball, bat1, bat2, scr_width, scr_height, sounds):
        """Game class init sprites, sound and screen size.

        Args:
            ball: ball object.
            bat1: bat object for player 1
            bat2: bat object for player 2 or computer. None if against wall game.
            sounds: string "True" or None
            scr_width: screen width in pixels.
            scr_height: screen height in pixels.
        """
        self.bat1 = bat1
        self.bat2 = bat2
        self.ball = ball
        self.scr_width = scr_width
        self.scr_height = scr_height
        self.events = Gamevents(scr_width, scr_height)
        self.sound = self._init_sound(sounds)

    def _init_sound(self, sounds):
        """Initializes sounds

        Args:
            sounds: "True" if sounds, else None.

        returns:
            SoundEffects class if True
        """
        if sounds == "True":
            return SoundEffects()
        return None

    def _init_game(self, game_type, ai_lvl):
        """Initializes game by game type and sets level of
        computer player to easy or average

        Args:
            game_type: String, "computer", "pvp" or "wall"
            ai_lvl: String, "easy" or "average"

        returns:
            player2: 2 for human player, 3 for computer player.
            p2_score: 0 if game type pvp or computer, None if game type is wall.
            computer: initializes ComputerAi class as computer if game type is computer.
        """
        p2_score = 0
        if game_type == "computer":
            computer = ComputerAi(self.ball, self.bat2, self.scr_width, ai_lvl)
            player2 = 3     #Set player2 to computer player.
            p2_score = 0
            return player2, p2_score, computer
        if game_type == "wall":
            p2_score = None
        player2 = 2
        return player2, p2_score, None

    def main(self, game_type, all_sprites, background, screen, hi_score, ai_lvl):
        '''Game main loop, starts the game, reads the keyboard and draws the game screen.

        Args:
            game_type: String, "computer", "pvp" or "wall".
            all_sprites: Sprite objects.
            background: background image.
            screen: pygame display module initialized in main.py
            hi_score: Int, old hi_score for against the wall game type.
            ai_lvl: String, "easy" or "average"

        Returns:
            hi_score: Int, new hiscore.
        '''
        clock = pygame.time.Clock()
        running = True
        p1_score = 0
        score = Score(screen, self.scr_width, self.scr_height, hi_score)
        player2, p2_score, computer = self._init_game(game_type, ai_lvl)
        self.events.launch(0, self.ball)

        while running:
            clock.tick(FPS)
            hit = False
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q]:            # pylint: disable=no-member
                    self.bat1.move_up()
                if keys[pygame.K_a]:            # pylint: disable=no-member
                    self.bat1.move_down()
                if keys[pygame.K_s] and game_type != "wall":   # pylint: disable=no-member
                    self.bat1.hit()
                    hit = True
                if game_type == "pvp":
                    if keys[pygame.K_UP]:           # pylint: disable=no-member
                        self.bat2.move_up()
                    if keys[pygame.K_DOWN]:         # pylint: disable=no-member
                        self.bat2.move_down()
                    if keys[pygame.K_LEFT]:         # pylint: disable=no-member
                        self.bat2.hit()
                        hit = True
                if event.type == pygame.QUIT:   # pylint: disable=no-member
                    running = False

            if game_type == "computer":
                hit = computer.ai_player_move(hit)

            if game_type != "wall":
                self.events.collision(self.bat1, self.bat2, self.ball, self.sound, hit)
                running, p1_score = self.events.is_p1_score(self.ball, \
                    p1_score, score, running, game_type, self.sound)
                running, p2_score = self.events.is_p2_score(self.ball, \
                    p2_score, score, running, player2, self.sound)
            else:
                p1_score = self.events.collision_wall(self.ball, self.bat1, p1_score, self.sound)
                running, hi_score = self.events.ball_on_table(self.ball, score, p1_score, hi_score, running)

            self.ball.update()
            screen.blit(background, (0,0))
            score.scores(p1_score, p2_score)
            all_sprites.draw(screen)
            pygame.display.update()

        return hi_score
