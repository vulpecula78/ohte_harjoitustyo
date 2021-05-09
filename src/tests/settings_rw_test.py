import os
import unittest

from settings_rw import SettingsRW


dirname = os.path.dirname(__file__)

class TestSettingsRW(unittest.TestCase):
    def setUp(self):
        self.test_setup = ["640", "480", "True", "average", "7", "7", "7"]
        self.settings = SettingsRW("test_settings.txt")
        self.testfile = os.path.join(dirname, "..", "test_settings.txt")
            
    def test_tiedostoa_ei_ole_luodaan_uusi(self):
        palautus = self.settings.load_settings(["333", "222", "True", "average", "1", "1", "1"])
        self.assertEqual(palautus[1], "222")
        
    def test_tieto_tallentuu_tiedostoon(self):
        self.settings.write_settings(self.test_setup)
        
        self.assertEqual(self.settings.load_settings(self.test_setup), self.test_setup)
        os.remove(self.testfile)

    def test_puutteellinen_tiedosto_korvataan_oletus_asetuksilla(self):
        test_setup = open(self.testfile, "w")
        test_setup.write("screen width: \n")
        test_setup.write(str(self.test_setup[0]))
        test_setup.write("\nscreen height: \n")
        test_setup.write(str(self.test_setup[1]))
        test_setup.write("\nsounds: \n")
        test_setup.close()
        
        palautus = self.settings.load_settings(self.test_setup)
        self.assertEqual(palautus[0], "640")
        
        os.remove(self.testfile)
