from data import Data
from state import State
import random


class Search:
    """This class performs the search to find the optimal dinner party seating arrangement."""
    party = 0
    members = 0
    hosts = 0

    def __init__(self, partydata):
        self.party = partydata
        self.members = self.party.getmembers()
        self.hosts = int(self.members / 2)

    def getparty(self):
        return self.party

    def getmembers(self):
        return self.members

    def are_host_and_guest(self, p1, p2):
        """Checks if p1 and p2 are a host/guest pair
            :param p1: First person as int
            :param p2: Second person as int
            :returns: True if either p1 is a host and p2 is a guest or vice versa, False otherwise"""
        if p1 >= self.members/2 > p2 or p2 >= self.members/2 > p1:
            return True
        else:
            return False

    def score(self, state):
        """Given a list of size n where n is the number of party members
            1 through n/2 is the first row of the table from left to right
            n/2 through n is the second row of the table from left to right
            such that n/2 is across from n.
            This method returns the score of given state.
            - 1 point for every adjacent pair (seated next to each other)
                of people with one a host and the other a guest.
            - 2 points for every opposite pair (seated across from each other)
                of people with one a host and the other a guest.
            - h(p1, p2) + h(p2, p1) points for every adjacent or opposite pair of people p1, p2.
            Remember that lists start at 0!!!
            :param state: List of int of size n
            :return: Int score for the given state
            """
        score = self.party.pref(state[0], state[self.hosts]) + self.party.pref(state[self.hosts], state[0])
        if self.are_host_and_guest(state[0], state[self.hosts]):
            score += 2
        # Left edge across
        for x in range(1, self.hosts):
            score += self.party.pref(state[x], state[x+self.hosts]) + self.party.pref(state[x+self.hosts], state[x])
            score += self.party.pref(state[x], state[x-1]) + self.party.pref(state[x-1], state[x])
            if self.are_host_and_guest(state[x], state[x-1]):
                score += 1
            if self.are_host_and_guest(state[x], state[x+self.hosts]):
                score += 2
            # Each iteration is for the seat to the left and across for the top row
        for x in range(self.hosts+1, self.members):
            score += self.party.pref(state[x], state[x-1]) + self.party.pref(state[x-1], state[x])
            if self.are_host_and_guest(state[x], state[x-1]):
                score += 1
            # Each iteration is for the seat to the left for the bottom row
        return score

    def score_seat(self, state, seat):
        """:param state: Current state of party as list of int
            :param seat: seat to score
            :returns: score of seat as int"""
        # check if seat is a corner
        if seat == 0 or seat == self.members:
            return 0

    def swap_and_score(self, pos1, pos2, old_state, new_state):
        return 0

    def solve(self, flips=10, flag=False):
        # set the default state and score
        best_state = []
        for i in range(0, self.members):
            best_state.append(i)
        top_score = self.score(best_state)
        if flag:
            print("best", best_state)
            print("top", top_score)
        # randomize list until we get a score better than default
        while True:
            new_state = random.sample(best_state, len(best_state))
            new_score = self.score(new_state)
            if flag:
                print("new", new_state)
                print("new score", new_score)
            if new_score > top_score:
                break
        best_state = new_state
        top_score = new_score
        # swap two people
        for i in range(0, flips):
            new_state = best_state.copy()
            pos1 = random.randrange(0, self.members, 1)
            pos2 = random.randrange(0, self.members, 1)
            new_state[pos1], new_state[pos2] = new_state[pos2], new_state[pos1]
            if flag:
                print("old state", best_state)
                print("new state", new_state)

