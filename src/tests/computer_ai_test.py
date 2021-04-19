import unittest
import pygame
from ball import Ball
from bat import Bat
from computer_ai import ComputerAi


class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball(380, 280, 800, 600)
        self.bat = Bat(575, 250, 800, 600)
        self.computer = ComputerAi(self.ball, self.bat, 600)
        
    def test_maila_ei_liiku_kun_pallo_menossa_pois(self):
        self.ball.set_velocity(-2, -3)
        self.ball.update()
        self.computer.ai_player_move()
        self.assertEqual((self.bat.rect.y), 250)
        
    def test_maila_liikkuu_ylos_kun_pallo_tulossa_kohti_ylos(self):
        self.ball.set_velocity(5, -3)
        self.ball.update()
        self.computer.ai_player_move()
        self.assertEqual((self.bat.rect.y), 248)
        
    def test_maila_liikkuu_alas_kun_pallo_tulossa_kohti_alas(self):
        self.bat.set_y_position(200)
        self.ball.set_velocity(5, 3)
        self.ball.update()
        self.computer.ai_player_move()
        self.assertEqual((self.bat.rect.y), 202)
