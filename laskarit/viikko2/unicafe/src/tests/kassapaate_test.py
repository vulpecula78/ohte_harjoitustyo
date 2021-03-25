import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(500)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_konstruktori_asettaa_edulliset_myynnit_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_konstruktori_asettaa_maukkaat_myynnit_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_kassassaoleva_rahamaara_muuttuu_oikein_kun_edullisesti(self):
        self.kassapaate.syo_edullisesti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        
    def test_palauttaa_rahaa_oikein_edulliset(self):
        self.assertEqual((self.kassapaate.syo_edullisesti_kateisella(400)), 160)
        
    def test_lisaa_edulliset_myynteja(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        
    def test_kassassaoleva_rahamaara_muuttuu_oikein_kun_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        
    def test_palauttaa_rahaa_oikein_maukkaat(self):
        self.assertEqual((self.kassapaate.syo_maukkaasti_kateisella(500)), 100)
        
    def test_lisaa_maukkaat_myynteja(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        
    def test_syo_edullisesti_rahamaara_ei_muutu_kun_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(150)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
 
    def test_syo_edullisesti_palauttaa_oikein_kun_ei_tarpeeksi_rahaa(self):
        self.assertEqual((self.kassapaate.syo_edullisesti_kateisella(220)), 220)
        
    def test_syo_edullisesti_myydyt_ei_muutu_kun_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(210)
        self.assertEqual(self.kassapaate.edulliset, 0)        
        
    def test_syo_maukkaasti_rahamaara_ei_muutu_kun_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(150)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
 
    def test_syo_maukkaasti_palauttaa_oikein_kun_ei_tarpeeksi_rahaa(self):
        self.assertEqual((self.kassapaate.syo_maukkaasti_kateisella(220)), 220)
        
    def test_syo_maukkaasti_myydyt_ei_muutu_kun_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(210)
        self.assertEqual(self.kassapaate.maukkaat, 0)   
        
    def test_kortilla_tarpeeksi_rahaa_syoda_edullisesti(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(str(self.maksukortti), "saldo: 2.6")

    def test_kortilla_tarpeeksi_rahaa_syoda_maukkaasti(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")        
        
    def test_syo_edullisesti_kortilla_lisaa_edullisesti_myytyja(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        
    def test_syo_maukkaasti_kortilla_lisaa_maukkaasti_myytyja(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        
    def test_kortilla_ei_tarpeeksi_rahaa_syoda_edullisesti(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")
        
    def test_kortilla_ei_tarpeeksi_rahaa_syoda_edullisesti_ei_lisaa_myytyja(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_kortilla_ei_tarpeeksi_rahaa_syoda_maukkaasti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)
        self.assertEqual(str(self.maksukortti), "saldo: 2.6")
        
    def test_kortilla_ei_tarpeeksi_rahaa_syoda_maukkaasti_ei_lisaa_myytyja(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_kassassa_oleva_rahamaara_ei_muutu_kortilla_ostettaessa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_rahaa_ladattaessa_kassaan_tulee_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 5000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 105000)
        
    def test_rahaa_ladattaessa_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 5000)
        self.assertEqual(str(self.maksukortti), "saldo: 55.0")
        
    def test_negatiivista_summaa_ei_voi_ladata(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -5000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
