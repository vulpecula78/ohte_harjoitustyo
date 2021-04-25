import unittest
import pygame
from gamevents import Gamevents
from ball import Ball
from bat import Bat
from ui.score import Score
from unittest.mock import MagicMock
import builtins

class TestGamevents(unittest.TestCase):
    def setUp(self):
        self.mock = MagicMock()
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        self.gamevents = Gamevents(800, 600)
        self.score = Score(screen, 800, 600, 5)
        self.ball = Ball(380, 280, 800, 600)
        self.bat1 = Bat(5, 280, 800, 600)
        self.bat2 = Bat(775, 280, 800, 600)
        
    def test_tietokone_odotuksen_jalkeen_palauttaa_false(self):
        self.assertEqual(self.gamevents.wait(3), False)
    
    def test_pallo_lahtee_liikkeelle_kun_peli_alkaa(self):
        self.assertEqual(self.gamevents.launch(0, self.ball), True)
        
    def test_against_wall_pallo_pysyy_poydalla_hiscore_ei_muutu(self):
        run, hiscore = self.gamevents.ball_on_table(self.ball, self.score, 4, 5)
        self.assertEqual(run, True)
        self.assertEqual(hiscore, 5)
    '''
    def test_against_wall_pallo_ulos_poydalta_hiscore_muuttuu(self):
        self.ball.rect.x = -45
        with self.mock.patch.object(builtins, self.wait(1), lambda _: 'self.wait(3)'):
            run, hiscore = self.gamevents.ball_on_table(self.ball, self.score, 7, 5)
            self.assertEqual(run, False)
            self.assertEqual(hiscore, 7)
'''
            
    def test_pelaaja_saa_pisteen_tietokonetta_vastaan(self):
        self.ball.rect.x = 805
        run, score = self.gamevents.is_p1_score(self.ball, 1, self.score, True, False, None)
        self.assertEqual(run, True)
        self.assertEqual(score, 2)
        
    def test_tietokone_voittaa_pelin(self):
        self.ball.rect.x = -44
        run, score = self.gamevents.is_p2_score(self.ball, 2, self.score, True, 3, None)
        self.assertEqual(run, False)
        self.assertEqual(score, 3)
        
    def test_pallo_kimpoaa_mailasta_against_wall(self):
        self.ball.rect.x = 28
        self.ball.set_velocity(-6 , 1)
        self.bat1.set_y_position(275)
        self.ball.update()
        score = self.gamevents.collision_wall(self.ball, self.bat1, 1, None)
        self.assertGreater(self.ball.get_x_velocity(), 3)
        self.assertEqual(score, 2)
