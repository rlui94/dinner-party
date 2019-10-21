from unittest import TestCase
from data import Data

default_matrix = [[0, -4, 6, 5], [-6, 0, 3, -7], [-8, 1, 0, 5], [2, -4, 0, 0]]
default_members = 4


class TestData(TestCase):

    def test_getmembers(self):
        party = Data(default_members)
        self.assertEqual(party.getmembers(), default_members)

    def test_getmatrix(self):
        party = Data(default_members, default_matrix)
        self.assertEqual(party.getmatrix(), default_matrix)

    def test_pref(self):
        party = Data(default_members, default_matrix)
        self.assertEqual(party.pref(1, 3), -7)

    def test_pref2(self):
        party = Data()
        with self.assertRaises(AssertionError):
            party.pref(1, 3)

    def test_readfile(self):
        with open("testfile.txt", 'r') as file:
            party = Data()
            party.readfile("testfile.txt")
            self.assertEqual(party.getmembers(), default_members)
            self.assertEqual(party.getmatrix(), default_matrix)