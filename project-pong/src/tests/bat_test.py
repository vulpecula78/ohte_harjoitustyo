import unittest
import pygame
from bat import Bat

class TestBat(unittest.TestCase):
    def setUp(self):
        self.bat = Bat(5, 250)

    def test_konstruktori_luo_mailan_haluttuun_kohtaan(self):
        self.assertEqual((self.bat.rect.x), 5)
        self.assertEqual((self.bat.rect.y), 250)

    def test_sijoita_maila(self):
        self.bat.setYposition(500)
        self.assertEqual((self.bat.rect.y), 500)

    def test_mailaa_ei_voi_sijoittaa_liian_alas(self):
        self.bat.setYposition(520)
        self.assertEqual((self.bat.rect.y), 250)

    def test_mailaa_ei_voi_sijoittaa_liian_ylos(self):
        self.bat.setYposition(-25)
        self.assertEqual((self.bat.rect.y), 250)        

    def test_liikuta_mailaa_ylos(self):
        self.bat.moveUp()
        self.assertEqual((self.bat.rect.y), 248)

    def test_liikuta_mailaa_alas(self):
        self.bat.moveDown()
        self.assertEqual((self.bat.rect.y), 252)

    def test_maila_ei_saa_Y_arvoksi_pienempaa_kuin_0(self):
        self.bat.setYposition(2)
        self.bat.moveUp()
        self.bat.moveUp()
        self.assertEqual((self.bat.rect.y), 0)
        
    def test_maila_ei_saa_Y_arvoksi_suurempaa_kuin_500(self):
        self.bat.setYposition(497)
        self.bat.moveDown()
        self.bat.moveDown()
        self.assertEqual((self.bat.rect.y), 499)
