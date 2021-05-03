'''Another Pong Clone Again main loop'''
import os
import pygame

from objects.bat import Bat
from objects.ball import Ball
from settings_rw import Settings_rw
from ui.game import Game
from ui.mmenu import Mmenu


FPS = 120
dirname = os.path.dirname(__file__)

class Main:
    def __init__(self):
        self.scr_width = 800
        self.scr_height = 600
        self.sound = "False"
        self.ai_lvl = "easy"
        self.setup = [800, 600, "False", "easy", 0, 0 ,0]

    def main(self):
        #load settings if file exist.
        #If not, then create file.
        settings_rw = Settings_rw()
        lsetup = settings_rw.load_settings(self.setup)
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
        clock = pygame.time.Clock()
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
                self._normal_game(screen, clock, "pvp", backgrd1)
            elif action == "computer":
                self._normal_game(screen, clock, "computer", backgrd1)
            elif action == "wall":
                hiscore = self._against_wall(screen, clock, "wall", hiscore, backgrd2)
            elif action == "settings":
                main_loop = False
                restart = True
            elif action == "quit":
                main_loop = False
        if restart:
            self.main()

    def _normal_game(self, screen, clock, game_type, backgrd1):
        '''2 player game or game against computer'''
        sprites = pygame.sprite.Group()
        background = pygame.image.load(os.path.join(dirname, "assets", backgrd1))
        bat1 = Bat(5, self.scr_height/2, self.scr_width, self.scr_height)
        bat2 = Bat(self.scr_width - 25, self.scr_height/2, self.scr_width, self.scr_height)
        ball = Ball(320, 240, self.scr_width, self.scr_height)

        sprites.add(bat1)
        sprites.add(bat2)
        sprites.add(ball)

        game = Game(ball, bat1, bat2, clock, self.scr_width, self.scr_height, self.sound)
        game.main(FPS, game_type, sprites, background, screen, 0, self.ai_lvl)

    def _against_wall(self, screen, clock, game_type, hiscore, backgrd2):
        sprites = pygame.sprite.Group()
        background = pygame.image.load(os.path.join(dirname, "assets", backgrd2))
        bat1 = Bat(5, self.scr_height/2, self.scr_width, self.scr_height)
        ball = Ball(320, 240, self.scr_width, self.scr_height)

        sprites.add(bat1)
        sprites.add(ball)

        game = Game(ball, bat1, None, clock, self.scr_width, self.scr_height, self.sound)
        hiscore = game.main(FPS, game_type, sprites, background, screen, hiscore, self.ai_lvl)
        return hiscore
