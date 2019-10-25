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

    def test_score_seat(self):
        search = Search(Data(default_members, default_matrix))
        state = [0, 1, 2, 3]
        self.assertEqual(-10, search.score_seat(state, 0))
        self.assertEqual(-19, search.score_seat(state, 1))
        self.assertEqual(-4, search.score_seat(state, 3))
        self.assertEqual(5, search.score_seat(state, 2))
        state = [0, 2, 1, 3]
        self.assertEqual(4, search.score_seat(state, 1))
        self.assertEqual(-20, search.score_seat(state, 2))

    def test_score_compare(self):
        search = Search(Data(default_members, default_matrix))
        old_state = [0, 1, 2, 3]
        new_state = [0, 2, 1, 3]
        # old score should be -14, new should be -16
        self.assertEqual(search.score_compare(1, 2, old_state, new_state), False)
        self.assertEqual(search.score_compare(2, 1, new_state, old_state), True)

    def test_print(self):
        search = Search(Data(default_members, default_matrix))
        search.print_state()

    def test_solve(self):
        search = Search(Data(default_members, default_matrix))
        search.solve(1, True)
        search.print_state(True)

    def test_solve_hill(self):
        search = Search(Data(default_members, default_matrix))
        search.solve(1, True, "g")
        search.print_state(True)

    def test_solve_hw(self):
        FILEFLAG = 1

        def file_switch(flag):
            switcher = {
                1: 'hw1-inst1.txt',  # 1m flips = ~20 seconds
                2: 'hw1-inst2.txt',
                3: 'hw1-inst3.txt',
                4: 'testfile.txt',
            }
            return switcher.get(flag, "Invalid flag")

        party = Data()
        party.readfile(file_switch(FILEFLAG))
        searcher = Search(party)
        searcher.solve(3000000)
        searcher.print_state()

