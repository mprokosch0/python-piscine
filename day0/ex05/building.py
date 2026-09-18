import sys


def analyze_input(text: str) -> None:
    """Analyze the input string and print its statistics.

    Args:
        text (str): The string to analyze.

    Returns:
        None.
    """
    stats = {"upper letters": 0,
             "lower letters": 0,
             "punctuation marks": 0,
             "spaces": 0,
             "digits": 0}

    p_marks = ['?', '!', ',', '.', ';', ':', '\'', '\"', '<', '>', '-']

    for char in text:
        if (char.isdigit()):
            stats["digits"] += 1
        elif (char.isupper()):
            stats["upper letters"] += 1
        elif (char.islower()):
            stats["lower letters"] += 1
        elif (char.isspace()):
            stats["spaces"] += 1
        elif (char in p_marks):
            stats["punctuation marks"] += 1
    for name, value in stats.items():
        print(f"{value}{" "}{name}")


def main():
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        text = sys.argv[1] if len(sys.argv) > 1 else input()
        analyze_input(text)

    except KeyboardInterrupt:
        print(f"{KeyboardInterrupt.__name__}{":"}", "Ctrl+C")
    except EOFError:
        print(f"{EOFError.__name__}{":"}", "Ctrl+D")
    except AssertionError as e:
        print(f"{AssertionError.__name__}{":"}", e)


if __name__ == "__main__":
    main()
