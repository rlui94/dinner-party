from data import Data


class State:
    """Contains information about a theoretical state of the dinner party.
        Assuming members are numbered 1..n, the seats are numbered such that
        the top half of the table has seats 1..n/2 left-to-right,
        and the bottom half of the table has seats n/2+1..n left-to-right;
        thus seat n/2 is opposite seat n."""

    def __init__(self, position):
        self.position = position

    def setpos(self, position):
        self.position = position

    def getpos(self):
        return self.position

