import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
        
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        
    def test_kortin_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(650)
        self.assertEqual(str(self.maksukortti),"saldo: 6.6")
        
    def test_saldo_vahenee_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(3)
        self.assertEqual(str(self.maksukortti), "saldo: 0.07")
        
    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(12)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        
    def test_palauttaa_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)
        
    def test_palauttaa_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(11), False)   
    