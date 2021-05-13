import os
import random
import pygame

dirname = os.path.dirname(__file__)

class SoundEffects:
    """Plays sound effects"""
    def __init__(self):
        """Initializes pygame.mixer and loads sound effects."""
        pygame.mixer.init()
        self.ball_hit1 = pygame.mixer.Sound(os.path.join(dirname,
                                                         "../assets/sounds","bat_sound1.wav"))
        self.ball_hit2 = pygame.mixer.Sound(os.path.join(dirname,
                                                         "../assets/sounds","bat_sound2.wav"))
        self.cheer = pygame.mixer.Sound(os.path.join(dirname, "../assets/sounds","cheer.wav"))
        self.hit = pygame.mixer.Sound(os.path.join(dirname, "../assets/sounds","hit.wav"))
        self.cheer.set_volume(0.5)

    def bat_sound(self):
        """Plays randomly selected sound when collision between bat and ball."""
        effect = random.randint(1,2)
        if effect == 1:
            self.ball_hit1.play()
        elif effect == 2:
            self.ball_hit2.play()

    def hit_sound(self):
        """Plays hit sound when ball is hit."""
        self.hit.play()

    def cheer_sound(self):
        """Plays cheer sound when somebody scores."""
        self.cheer.play()
