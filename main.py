from data import Data
FILEFLAG = 4


def file_switch(flag):
    switcher = {
        1: 'hw1-inst1.txt',
        2: 'hw1-inst2.txt',
        3: 'hw1-inst3.txt',
        4: 'testfile.txt',
    }
    return switcher.get(flag, "Invalid flag")


if __name__ == '__main__':

    party = Data()
    party.readfile(file_switch(FILEFLAG))
    print("Hello World")

