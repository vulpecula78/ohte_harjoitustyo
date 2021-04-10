import unittest
import pygame
from ball import Ball

class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball(380, 280, 800, 600)
        
    def test_konstruktori_asetti_pallon_haluttuun_kohtaan(self):
        self.assertEqual((self.ball.rect.x), 380)
        self.assertEqual((self.ball.rect.y), 280)
