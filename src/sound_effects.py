import os
import random
import pygame

dirname = os.path.dirname(__file__)

class SoundEffects:
    def __init__(self):
        pygame.mixer.init()
        self.ball_hit1 = pygame.mixer.Sound(os.path.join(dirname, "assets", "bat_sound1.wav"))
        self.ball_hit2 = pygame.mixer.Sound(os.path.join(dirname, "assets", "bat_sound2.wav"))
        self.cheer = pygame.mixer.Sound(os.path.join(dirname, "assets", "cheer.wav"))
        self.hit = pygame.mixer.Sound(os.path.join(dirname, "assets", "hit.wav"))
        self.cheer.set_volume(0.5)

    def bat_sound(self):
        effect = random.randint(1,2)
        if effect == 1:
            self.ball_hit1.play()
        elif effect == 2:
            self.ball_hit2.play()

    def hit_sound(self):
        self.hit.play()

    def cheer_sound(self):
        self.cheer.play()
