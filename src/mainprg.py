'''Another Pong Clone Again'''

import os
import pygame

from bat import Bat
from ball import Ball
from game import Game
from mmenu import Mmenu
from score import Score

FPS = 120
dirname = os.path.dirname(__file__)

def main():
    scr_width = 800
    scr_height = 600

    pygame.init()   # pylint: disable=no-member
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((scr_width, scr_height))
    pygame.display.set_caption("APCA")
    menu = Mmenu(scr_width, scr_height, screen)
    pygame.key.set_repeat(1, 2)

    main_loop =True
    #Title screen
    while main_loop:
        action = menu.menu()

        if action == "PvP":
            normal_game(scr_width, scr_height, screen, clock, "pvp")
        elif action =="computer":
            normal_game(scr_width, scr_height, screen, clock, "computer")
        elif action == "quit":
            main_loop = False

def normal_game(scr_width, scr_height, screen, clock, game_type):
    all_sprites = pygame.sprite.Group()
    background = pygame.image.load(os.path.join(dirname, "assets", "background1.png"))
    bat1 = Bat(5, scr_height/2, scr_width, scr_height)
    bat2 = Bat(scr_width - 25, scr_height/2, scr_width, scr_height)
    ball = Ball(scr_width/2 - 20, scr_height/2 - 20, scr_width, scr_height)

    all_sprites.add(bat1)
    all_sprites.add(bat2)
    all_sprites.add(ball)

    score = Score(screen, scr_width, scr_height)
    game = Game(score, ball, bat1, bat2, clock, scr_width, scr_height)

    game.main(FPS, game_type, all_sprites, background, screen)


if __name__ == "__main__":
    main()
