class Data:
    """Contains given information on party members."""

    def __init__(self):
        self.members = 0
        self.guests = 0
        self.hosts = 0
        self.prefmatrix = []

    def readfile(self, filename):
        """Reads a file in the format described in the README and stores info"""
        with open(filename, 'r') as file:
            self.members = int(file.readline())
            # first line is always an even number, this is our number of members
            for line in file:
                self.prefmatrix.append(
                    list(int(num) for num in line.split())
                )
            # For each line, create new list of numbers cast from string to int
            # Append to the empty preference matrix to create full prefmatrix
            # https://stackoverflow.com/a/6583635
        print(self.prefmatrix[1][3])