import pygame
import random
from bat import Bat
from ball import Ball
from game import Game
from score import Score
from screen_render import Screen_render

scr_width = 800
scr_height = 600
FPS = 100
GREEN = (0, 255, 0)
p1_score = 0
p2_score = 0

def main():
    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode((scr_width, scr_height))
    screen = pygame.display.set_mode((scr_width, scr_height))
    pygame.display.set_caption("APCA")
    
    background = pygame.image.load( "assets/background1.png")
    all_sprites = pygame.sprite.Group()

    bat1 = Bat(5, 300, scr_width, scr_height)
    bat2 = Bat(775, 300,scr_width, scr_height)
    ball = Ball(400, 300, scr_width, scr_height)    
    
    all_sprites.add(bat1)
    all_sprites.add(bat2)
    all_sprites.add(ball)

    pygame.key.set_repeat(1, 2)
    
    score = Score(screen, scr_width, scr_height)
    render = Screen_render(screen, display, all_sprites, background)
    game = Game(FPS, render, score, ball, bat1, bat2, display, clock, scr_width, scr_height)
    
    game.main()
    

if __name__ == "__main__":
    main()

 
