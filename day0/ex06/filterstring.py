import sys
from ft_filter import ft_filter


def main():
    try:
        assert len(sys.argv) == 3
        try:
            int(sys.argv[2])
        except ValueError:
            raise AssertionError()
        wds = sys.argv[1].split()
        print(type(wds)(ft_filter(lambda x: len(x) > int(sys.argv[2]), wds)))

    except AssertionError:
        print(f"{AssertionError.__name__}{":"}", "Arguments are bad")


if __name__ == "__main__":
    main()
