'''Another Pong Clone Again main loop'''
import os
import pygame

from objects.bat import Bat
from objects.ball import Ball
from settings_rw import SettingsRW
from ui.game import Game
from ui.mmenu import Mmenu

dirname = os.path.dirname(__file__)

class Main:
    """Main program for Another pong clone again game. This calls for main menu,
    and runs selected game."""
    def __init__(self):
        """Initializes main program with default values. These values will be used
        if apca_settings.txt file is not found. """
        self.scr_width = 800
        self.scr_height = 600
        self.sound = "False"
        self.ai_lvl = "easy"
        self.setup = [800, 600, "False", "easy", 0, 0 ,0]
        self.settings_rw = SettingsRW("apca_settings.txt")

    def main(self):
        """Main loop. Loads settings if file exist. If not, then creates file
        and initializes with default values. Runs main menu and starts selected game."""
        lsetup = self.settings_rw.load_settings(self.setup)

        #init settings
        self.scr_width = int(lsetup[0])
        self.scr_height = int(lsetup[1])
        self.sound = lsetup[2]
        self.ai_lvl = lsetup[3]
        if self.scr_width == 1024:
            hiscore = int(lsetup[6])
            backgrd1 = "background1_1024x768.png"
            backgrd2 = "background2_1024x768.png"
        elif self.scr_width == 800:
            hiscore = int(lsetup[5])
            backgrd1 = "background1_800x600.png"
            backgrd2 = "background2_800x600.png"
        else:
            hiscore = int(lsetup[4])
            backgrd1 = "background1_640x480.png"
            backgrd2 = "background2_640x480.png"
        restart = False

        #setup screen
        pygame.init()   # pylint: disable=no-member
        screen = pygame.display.set_mode((self.scr_width, self.scr_height))
        pygame.display.set_caption("APCA")
        menu = Mmenu(self.scr_width, self.scr_height, screen)
        pygame.key.set_repeat(1, 2)

        main_loop = True
        #Start main loop
        while main_loop:
        #Title screen
            action = menu.menu(lsetup)

            if action == "PvP":
                self._normal_game(screen, "pvp", backgrd1)
            elif action == "computer":
                self._normal_game(screen, "computer", backgrd1)
            elif action == "wall":
                score = self._against_wall(screen, "wall", hiscore, backgrd2)
                if score > hiscore:
                    hiscore = score
                    lsetup = self._new_hiscore(lsetup, score)
            elif action == "settings":
                main_loop = False
                restart = True
            elif action == "quit":
                main_loop = False
        if restart:
            self.main()

    def _normal_game(self, screen, game_type, backgrd1):
        '''initializes and starts 2 player game or game against computer.

        Args:
            screen: pygame display mode settings
            game_type: String, selected game type: "pvp" or "computer"
            backgrd1: background image according to screen size
        '''
        sprites = pygame.sprite.Group()
        background = pygame.image.load(os.path.join(dirname, "assets", backgrd1))
        bat1 = Bat(5, self.scr_height/2, self.scr_width, self.scr_height)
        bat2 = Bat(self.scr_width - 25, self.scr_height/2, self.scr_width, self.scr_height)
        ball = Ball(320, 240, self.scr_width, self.scr_height)

        sprites.add(bat1)
        sprites.add(bat2)
        sprites.add(ball)

        game = Game(ball, bat1, bat2, self.scr_width, self.scr_height, self.sound)
        game.main(game_type, sprites, background, screen, 0, self.ai_lvl)

    def _against_wall(self, screen, game_type, hiscore, backgrd2):
        '''initializes and starts against the wall game.

        Args:
            screen: pygame display mode settings
            game_type: String, selected game type: "wall"
            hiscore: Current hiscore in selected screen size.
            backgrd2: background image according to screen size
        '''
        sprites = pygame.sprite.Group()
        background = pygame.image.load(os.path.join(dirname, "assets", backgrd2))
        bat1 = Bat(5, self.scr_height/2, self.scr_width, self.scr_height)
        ball = Ball(320, 240, self.scr_width, self.scr_height)

        sprites.add(bat1)
        sprites.add(ball)

        game = Game(ball, bat1, None, self.scr_width, self.scr_height, self.sound)
        hiscore = game.main(game_type, sprites, background, screen, hiscore, self.ai_lvl)
        return hiscore

    def _new_hiscore(self, lsetup, score):
        """Writes new hiscore into settings file.

        Args:
            lsetup: list of settings and hiscores
            score: New hiscore

        Returns:
            lsetup: list of current settings and hiscores
        """
        if self.scr_width == 1024:
            lsetup[6] = score
        elif self.scr_width == 800:
            lsetup[5] = score
        else:
            lsetup[4] = score
        lsetup = self.settings_rw.write_settings(lsetup)
        return lsetup
