import unittest
import pygame
from wait import Wait

class TestWait(unittest.TestCase):
    def setUp(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        self.wait = Wait(800, 600)
        
    def test_tietokone_odotuksen_jalkeen_palauttaa_false(self):
        self.assertEqual(self.wait.wait(3), False)
        
