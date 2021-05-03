import unittest
import pygame
from ball import Ball

class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball(380, 280, 800, 600)
        
    def test_konstruktori_asetti_pallon_haluttuun_kohtaan(self):
        self.assertEqual((self.ball.rect.x), 380)
        self.assertEqual((self.ball.rect.y), 280)
        
    def test_pallon_sijainnin_asetus(self):
        self.ball.set_position(100, 99)
        self.assertEqual((self.ball.rect.x), 100)
        self.assertEqual((self.ball.rect.y), 99)                                         
        
    def test_pallon_nopeus_on_oikea_ja_se_muuttuu_oikein(self):
        self.ball.set_velocity(3, 2)
        self.assertEqual((self.ball.get_x_velocity()), 3)
        self.assertEqual((self.ball.get_y_velocity()), 2)        
        self.ball.set_velocity(-2, -3)
        self.assertEqual((self.ball.get_x_velocity()), -2)
        self.assertEqual((self.ball.get_y_velocity()), -3)
        
    def test_pallon_nopeus_ei_nouse_liikaa_pos(self):
        self.ball.set_velocity(6, 9)
        self.ball.set_velocity(11, 11)
        self.assertEqual((self.ball.get_x_velocity()), 10)
        self.assertEqual((self.ball.get_y_velocity()), 9)

    def test_pallon_nopeus_ei_nouse_liikaa_neg(self):
        self.ball.set_velocity(-8, -8)
        self.ball.set_velocity(-11, -11)
        self.assertEqual((self.ball.get_x_velocity()), -10)
        self.assertEqual((self.ball.get_y_velocity()), -8)        

    def test_pallon_tilanne_paivittyy(self):
        self.ball.set_position(50, 50)
        self.ball.set_velocity(4, 2)
        self.ball.update()
        self.assertEqual((self.ball.rect.x), 54)
        self.assertEqual((self.ball.rect.y), 52)
        

    def test_pallon_tilanne_paivittyy_ja_suunta_muuttuu_alas(self):
        self.ball.set_position(70, 1)
        self.ball.set_velocity(2, -3)
        self.ball.update()
        self.assertEqual((self.ball.rect.y), 0)
        self.ball.update()
        self.assertEqual((self.ball.rect.y), 3)
        

    def test_pallon_tilanne_paivittyyja_suunta_muuttuu_ylos(self):
        self.ball.set_position(85, 513)
        self.ball.set_velocity(2, 3)
        self.ball.update()
        self.assertEqual((self.ball.rect.y), 515)
        self.ball.update()
        self.assertEqual((self.ball.rect.y), 512)
