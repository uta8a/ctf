# 'Uryyb, Jbeyq!'

from unittest import TestCase
from scripts.rot import ROT

class TestROT(TestCase):

    def test_rot(self):
        self.assertEqual(ROT.rot(13, 'Uryyb, Jbeyq!'), 'Hello, World!')
        self.assertEqual(ROT.rot(8, 'Lzw kwugfv hsjl gx lzw xdsy ak: _uDskk!usd_u'), 'The second part of the flag is: _cLass!cal_c')