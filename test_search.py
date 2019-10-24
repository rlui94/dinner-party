from unittest import TestCase
from data import Data
from search import Search

default_matrix = [[0, -4, 6, 5], [-6, 0, 3, -7], [-8, 1, 0, 5], [2, -4, 0, 0]]
default_members = 4


class TestSearch(TestCase):
    def test_init(self):
        party = Data(default_members, default_matrix)
        search = Search(party)
        self.assertEqual(search.getparty(), party)
        self.assertEqual(search.getmembers(), default_members)

    def test_are_host_and_guest(self):
        search = Search(Data(default_members, default_matrix))
        self.assertEqual(search.are_host_and_guest(0, 1), False)
        self.assertEqual(search.are_host_and_guest(1, 0), False)
        self.assertEqual(search.are_host_and_guest(2, 3), False)
        self.assertEqual(search.are_host_and_guest(3, 2), False)
        self.assertEqual(search.are_host_and_guest(0, 2), True)
        self.assertEqual(search.are_host_and_guest(0, 3), True)
        self.assertEqual(search.are_host_and_guest(1, 3), True)
        self.assertEqual(search.are_host_and_guest(1, 2), True)

    def test_score(self):
        search = Search(Data(default_members, default_matrix))
        state = [0, 1, 2, 3]
        self.assertEqual(search.score(state), -14)
