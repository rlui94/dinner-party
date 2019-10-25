from data import Data
from search import Search
import time
FILEFLAG = 1
FLIPS = 100000


def file_switch(flag):
    switcher = {
        1: 'hw1-inst1.txt',  # 1m f flips = ~20 sec, 100,000 g flips = ~55 sec
        2: 'hw1-inst2.txt',
        3: 'hw1-inst3.txt',
        4: 'testfile.txt',
    }
    return switcher.get(flag, "Invalid flag")


def soln_switch(flag):
    switcher = {
        1: 'hw1-soln1.txt',
        2: 'hw1-soln2.txt',
        3: 'hw1-soln3.txt',
    }
    return switcher.get(flag, "Invalid flag")


if __name__ == '__main__':
    start = time.time()
    party = Data()
    party.readfile(file_switch(FILEFLAG))
    searcher = Search(party)
    searcher.solve(flips=FLIPS, strat="g")
    searcher.print_state()
    end = time.time()
    print("Ran %d flips in %.3f seconds." % (FLIPS, end-start))
    searcher.print_state_file(soln_switch(FILEFLAG))

