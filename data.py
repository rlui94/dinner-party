class Data:
    """Contains given information on party members."""

    def __init__(self, members=0, prefmatrix=[]):
        self.members = members
        self.prefmatrix = prefmatrix

    def readfile(self, filename):
        """Reads a file in the format described in the README and stores info"""
        with open(filename, 'r') as file:
            self.members = int(file.readline().strip())
            # first line is always an even number, this is our number of members
            for line in file:
                self.prefmatrix.append(
                    [int(num) for num in line.split()]
                )
            # For each line, create new list of numbers cast from string to int
            # Append to the empty preference matrix to create full prefmatrix
            # https://stackoverflow.com/a/6583635 for concise matrix appending

    def getmembers(self):
        return self.members

    def getmatrix(self):
        return self.prefmatrix

    def pref(self, p1, p2):
        """Given a pair of people p1,p2
            return the preference score.
            Remember people are numbered 0-(n-1)!"""
        assert self.prefmatrix, 'prefixmatrix is empty'
        return self.prefmatrix[p1][p2]