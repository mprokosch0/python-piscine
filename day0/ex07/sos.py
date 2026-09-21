import sys


def main():
    try:
        assert len(sys.argv) == 2
        NESTED_MORSE = {" ": "/ ",
                        "A": ".- ",
                        "B": "-... ",
                        "C": "-.-. ",
                        "D": "-.. ",
                        "E": ". ",
                        "F": "..-. ",
                        "G": "--. ",
                        "H": ".... ",
                        "I": ".. ",
                        "J": ".--- ",
                        "K": "-.- ",
                        "L": ".-.. ",
                        "M": "-- ",
                        "N": "-. ",
                        "O": "--- ",
                        "P": ".--. ",
                        "Q": "--.- ",
                        "R": ".-. ",
                        "S": "... ",
                        "T": "- ",
                        "U": "..- ",
                        "V": "...- ",
                        "W": ".-- ",
                        "X": "-..- ",
                        "Y": "-.-- ",
                        "Z": "--.. ",
                        "1": ".---- ",
                        "2": "..--- ",
                        "3": "...-- ",
                        "4": "....- ",
                        "5": "..... ",
                        "6": "-.... ",
                        "7": "--... ",
                        "8": "---.. ",
                        "9": "----. ",
                        "0": "----- "}
        s = str()
        for x in sys.argv[1]:
            if x.isalnum() is False and x != " ":
                raise AssertionError()
            s += NESTED_MORSE[x.upper()]
        print(s)

        
    except AssertionError:
        print(f"{AssertionError.__name__}{":"}", "The arguments are bad")

if __name__ == "__main__":
    main()