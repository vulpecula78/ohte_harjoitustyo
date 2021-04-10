import pygame
from pygame.locals import QUIT, KEYDOWN, K_a, K_LEFT # pylint: disable=no-name-in-module

class Wait:

    def wait(self, player):
        '''Wait for player action after scoring'''
        pygame.event.clear()

        while True:
            key_pressed = pygame.event.wait()
            if key_pressed.type == QUIT:
                return False
            if key_pressed.type == KEYDOWN and player == 1:
                if key_pressed.key == K_a:
                    return True
            if key_pressed.type == KEYDOWN and player == 2:
                if key_pressed.key == K_LEFT:
                    return True
