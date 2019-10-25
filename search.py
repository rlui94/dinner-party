from data import Data
import random
import os


class Search:
    """This class performs the search to find the optimal dinner party seating arrangement."""

    def __init__(self, partydata):
        """ :var party: Information on party as type Data
            :var members: number of party members as Int
            :var hosts: number of hosts as int (should be members/2)
            :var state: Currently held state"""
        self.party = partydata
        self.members = self.party.getmembers()
        self.hosts = int(self.members / 2)
        self.state = []
        for i in range(0, self.members):
            self.state.append(i)

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
        score = 0
        # is seat in the top?
        if 0 <= seat <= self.hosts-1:
            score += self.party.pref(state[seat], state[seat+self.hosts])
            score += self.party.pref(state[seat+self.hosts], state[seat])
            if self.are_host_and_guest(state[seat], state[seat+self.hosts]):
                score += 2
            # is seat in top left corner?
            if seat == 0:
                score += self.party.pref(state[seat], state[seat+1])
                score += self.party.pref(state[seat+1], state[seat])
                if self.are_host_and_guest(state[seat], state[seat+1]):
                    score += 1
            # is seat top right corner?
            elif seat == self.hosts-1:
                score += self.party.pref(state[seat], state[seat-1])
                score += self.party.pref(state[seat-1], state[seat])
                if self.are_host_and_guest(state[seat], state[seat-1]):
                    score += 1
            # else seat is somewhere else in the top row
            else:
                score += self.party.pref(state[seat], state[seat + 1])
                score += self.party.pref(state[seat + 1], state[seat])
                score += self.party.pref(state[seat], state[seat - 1])
                score += self.party.pref(state[seat - 1], state[seat])
                if self.are_host_and_guest(state[seat], state[seat+1]):
                    score += 1
                if self.are_host_and_guest(state[seat], state[seat-1]):
                    score += 1
        # else seat is a bottom row seat
        else:
            score += self.party.pref(state[seat], state[seat-self.hosts])
            score += self.party.pref(state[seat-self.hosts], state[seat])
            if self.are_host_and_guest(state[seat-self.hosts], state[seat]):
                score += 2
            # is seat in bottom left corner?
            if seat == self.hosts:
                score += self.party.pref(state[seat], state[seat+1])
                score += self.party.pref(state[seat+1], state[seat])
                if self.are_host_and_guest(state[seat+1], state[seat]):
                    score += 1
            # is seat in bottom right corner?
            elif seat == self.members-1:
                score += self.party.pref(state[seat], state[seat-1])
                score += self.party.pref(state[seat-1], state[seat])
                if self.are_host_and_guest(state[seat-1], state[seat]):
                    score += 1
            # else seat is somewhere else in bottom row
            else:
                score += self.party.pref(state[seat], state[seat + 1])
                score += self.party.pref(state[seat + 1], state[seat])
                score += self.party.pref(state[seat], state[seat - 1])
                score += self.party.pref(state[seat - 1], state[seat])
                if self.are_host_and_guest(state[seat+1], state[seat]):
                    score += 1
                if self.are_host_and_guest(state[seat-1], state[seat]):
                    score += 1
        return score

    def score_compare(self, pos1, pos2, old_state, new_state):
        """Uses score_seat method to compare sum of old seat scores and sum of new seat scores.
            :param old_state: Old state as list of int
            :param new_state: New state as list of int
            :param pos1: First position in the swap as int
            :param pos2: Second position in the swap as int
            :returns: True if new seating is better (new score is higher) else False"""
        old_seat_score = self.score_seat(old_state, pos1) + self.score_seat(old_state, pos2)
        new_seat_score = self.score_seat(new_state, pos1) + self.score_seat(new_state, pos2)
        if new_seat_score > old_seat_score:
            return True
        else:
            return False

    def solve(self, flips=10, flag=False):
        """Uses other Search methods to find better scoring states.
            Set the default state, randomize list until we get a score better than default.
            Swap two positions in a newly created state, then compare the scores of the two seats in old a new states.
            Repeat until desired flips have been made.
            :param flips: Number of flips to be made as an int, default 10
            :param flag: Debug flag as bool, default False"""
        if flag:
            self.state = [0, 1, 2, 3]
            print("start state", self.state)
            print("start score", self.score(self.state))
            new_state = [0, 2, 1, 3]
            print("new", new_state)
            print("new score", self.score(new_state))
        else:
            # randomize list until we get a score better than default
            while True:
                new_state = random.sample(self.state, self.members)
                if self.score(self.state) > self.score(new_state):
                    self.state = new_state
                    break
        # swap two people
        for i in range(0, flips):
            new_state = self.state.copy()
            pos1 = random.randrange(0, self.members, 1)
            pos2 = random.randrange(0, self.members, 1)
            new_state[pos1], new_state[pos2] = new_state[pos2], new_state[pos1]
            if flag:
                print("old state", self.state)
                print("new state", new_state)
            # if new state has a better score, store it
            if self.score_compare(pos1, pos2, self.state, new_state):
                self.state = new_state

    def print_state(self, pretty=False):
        """Prints state variable stored. We add +1 to the results because states are numbered 0-members.
            :param pretty: Bool that prints pretty if True, default False"""
        if pretty:
            print("State score:", self.score(self.state))
            print("Person Number\tSeat Number")
            for i in range(0, self.members):
                print(self.state[i]+1, '\t\t\t\t', i+1)
        else:
            print(self.score(self.state))
            for i in range(0, self.members):
                print(self.state[i]+1, i+1)

    def print_state_file(self, filename, pretty=False):
        """Outputs state variable stored to a file. We add +1 to the results because states are numbered 0-members.
            :param filename: path to file as string
            :param pretty: Bool that prints pretty if True, default False"""
        if os.path.exists(filename):
            os.remove(filename)
        with open(filename, 'w') as file:
            if pretty:
                file.write("State score: %d\n" % self.score(self.state))
                file.write("Person Number\tSeat Number\n")
                for i in range(0, self.members):
                    file.write("%d\t\t\t\t%d\n" % (self.state[i]+1, i+1))
            else:
                file.write("%d\n" % self.score(self.state))
                for i in range(0, self.members):
                    file.write("%d %d\n" % (self.state[i]+1, i+1))