import unittest
import pygame
from bat import Bat

class TestBat(unittest.TestCase):
    def setUp(self):
        self.bat = Bat(5, 250, 800, 600)

    def test_konstruktori_luo_mailan_haluttuun_kohtaan(self):
        self.assertEqual((self.bat.rect.x), 5)
        self.assertEqual((self.bat.rect.y), 250)

    def test_sijoita_maila(self):
        self.bat.set_y_position(455)
        self.assertEqual((self.bat.rect.y), 455)

    def test_mailaa_ei_voi_sijoittaa_liian_alas(self):
        self.bat.set_y_position(490)
        self.assertEqual((self.bat.rect.y), 250)

    def test_mailaa_ei_voi_sijoittaa_liian_ylos(self):
        self.bat.set_y_position(-25)
        self.assertEqual((self.bat.rect.y), 250)        

    def test_liikuta_mailaa_ylos(self):
        self.bat.move_up()
        self.assertEqual((self.bat.rect.y), 248)

    def test_liikuta_mailaa_alas(self):
        self.bat.move_down()
        self.assertEqual((self.bat.rect.y), 252)

    def test_maila_ei_saa_y_arvoksi_pienempaa_kuin_0(self):
        self.bat.set_y_position(2)
        self.bat.move_up()
        self.bat.move_up()
        self.assertEqual((self.bat.rect.y), 0)
        
    def test_maila_ei_saa_y_arvoksi_suurempaa_kuin_455(self):
        self.bat.set_y_position(453)
        self.bat.move_down()
        self.bat.move_down()
        self.assertEqual((self.bat.rect.y), 455)

    def test_vasen_maila_liikkuu_eteen_kun_lyo(self):
        self.bat.hit()
        self.assertEqual((self.bat.rect.x), 25)
        
    def test_vasen_maila_palaa_takaisin_paikalleen(self):
        self.bat.hit()
        self.bat.move_up()
        self.assertEqual((self.bat.rect.x), 5)
        
    def test_oikea_maila_liikkuu_eteen_kun_lyo(self):
        self.bat.rect.x = 775
        self.bat.hit()
        self.assertEqual((self.bat.rect.x), 755)
        
    def test_oikea_maila_palaa_takaisin_paikalleen(self):
        self.bat.rect.x = 775
        self.bat.hit()
        self.bat.move_up()
        self.assertEqual((self.bat.rect.x), 775)
