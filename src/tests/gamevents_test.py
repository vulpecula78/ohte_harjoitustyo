import unittest
import pygame
from gamevents import Gamevents
from objects.ball import Ball
from objects.bat import Bat
from ui.score import Score


class TestGamevents(unittest.TestCase):
    def setUp(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        self.gamevents = Gamevents(800, 600)
        self.score = Score(screen, 800, 600, 5)
        self.ball = Ball(380, 280, 800, 600)
        self.bat1 = Bat(5, 280, 800, 600)
        self.bat2 = Bat(775, 280, 800, 600)
        
    def test_tietokone_odotuksen_jalkeen_palauttaa_false(self):
        self.assertEqual(self.gamevents.wait(3), False)
        
    def test_tietokone_laukaisee_pallon(self):
        self.assertEqual(self.gamevents.launch(3, self.ball), True)
    
    def test_pallo_lahtee_liikkeelle_kun_peli_alkaa(self):
        self.assertEqual(self.gamevents.launch(0, self.ball), True)
        
    def test_against_wall_pallo_pysyy_poydalla_hiscore_ei_muutu(self):
        run, hiscore = self.gamevents.ball_on_table(self.ball, self.score, 4, 5, True)
        self.assertEqual(run, True)
        self.assertEqual(hiscore, 5)
            
    def test_pelaaja_saa_pisteen_tietokonetta_vastaan(self):
        self.ball.rect.x = 805
        run, score = self.gamevents.is_p1_score(self.ball, 1, self.score, True, False, None)
        self.assertEqual(run, True)
        self.assertEqual(score, 2)
        
    def test_tietokone_voittaa_pelin(self):
        self.ball.rect.x = -44
        run, score = self.gamevents.is_p2_score(self.ball, 4, self.score, True, 3, None)
        self.assertEqual(run, False)
        self.assertEqual(score, 5)
        
    def test_pallo_kimpoaa_mailasta_against_wall(self):
        self.ball.rect.x = 28
        self.ball.set_velocity(-6 , 1)
        self.bat1.set_y_position(275)
        self.ball.update()
        score = self.gamevents.collision_wall(self.ball, self.bat1, 1, None)
        self.assertGreater(self.ball.get_x_velocity(), 3)
        self.assertEqual(score, 2)
        
    def test_pallo_vaihtaa_suuntaa_pelaajan1_mailasta(self):
        self.ball.set_position(31, 120)
        self.ball.set_velocity(-8, 3)
        self.bat1.set_y_position(100)
        self.ball.update()
        self.gamevents.collision(self.bat1, self.bat2, self.ball, None, False)
        self.assertGreater(self.ball.get_x_velocity(), 6)

    def test_pallo_vaihtaa_suuntaa_pelaajan2_mailasta(self):
        self.ball.set_position(735, 120)
        self.ball.set_velocity(8, 3)
        self.bat2.set_y_position(100)
        self.ball.update()
        self.gamevents.collision(self.bat1, self.bat2, self.ball, None, False)
        self.assertLess(self.ball.get_x_velocity(), -6)
