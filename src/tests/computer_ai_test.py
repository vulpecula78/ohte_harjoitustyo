import unittest
import pygame
from ball import Ball
from bat import Bat
from computer_ai import ComputerAi


class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball(580, 280, 800, 600)
        self.bat = Bat(775, 250, 800, 600)
        self.computer = ComputerAi(self.ball, self.bat, 800, "average")
        
    def test_maila_ei_liiku_kun_pallo_menossa_pois(self):
        self.ball.set_velocity(-2, -3)
        self.ball.update()
        self.computer.ai_player_move(False)
        self.assertEqual((self.bat.rect.y), 250)
        
    def test_maila_liikkuu_ylos_kun_pallo_tulossa_kohti_ylos(self):
        self.ball.set_velocity(5, -3)
        self.ball.update()
        self.computer.ai_player_move(False)
        self.assertEqual((self.bat.rect.y), 246)
        
    def test_maila_liikkuu_alas_kun_pallo_tulossa_kohti_alas(self):
        self.bat.set_y_position(200)
        self.ball.set_velocity(5, 3)
        self.ball.update()
        self.computer.ai_player_move(False)
        self.assertEqual((self.bat.rect.y), 204)
        
    def test_ai_lyo_palloa_kun_x_nopeus_alle_7(self):
        self.ball.rect.x = 720
        self.ball.set_velocity(4, 4)
        self.computer.ai_player_move(False)
        self.assertEqual(self.computer.ai_player_move(False), True)
        
    def test_ai_ei_lyo_palloa_kun_x_nopeus_yli_7(self):
        self.ball.rect.x = 720
        self.ball.set_velocity(8, 4)
        self.computer.ai_player_move(False)
        self.assertEqual(self.computer.ai_player_move(False), False)
        
    def test_ai_ei_lyo_palloa_kun_maila_ei_ole_kohdalla(self):
        self.ball.rect.x = 720
        self.ball.rect.y = 100
        self.ball.set_velocity(4, 4)
        self.computer.ai_player_move(False)
        self.assertEqual(self.computer.ai_player_move(False), False)

    def test_maila_liikkuu_alas_kun_pallo_tulossa_kohti_easy(self):
        self.computer = ComputerAi(self.ball, self.bat, 800, "easy")
        self.bat.set_y_position(200)
        self.ball.set_velocity(4, 3)
        self.ball.update()
        self.computer.ai_player_move(False)
        self.assertEqual((self.bat.rect.y), 202)
        
    def test_maila_liikkuu_ylos_kun_pallo_tulossa_kohti_easy(self):
        self.computer = ComputerAi(self.ball, self.bat, 800, "easy")
        self.ball.set_velocity(6, -3)
        self.ball.update()
        self.computer.ai_player_move(False)
        self.assertEqual((self.bat.rect.y), 248)
