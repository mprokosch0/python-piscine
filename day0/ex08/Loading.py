import os


def ft_tqdm(lst: range) -> None:
    """Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progress bar every time a value is requested."""
    max_num_len = len(str(lst[-1]))
    term_width = os.get_terminal_size().columns - 32 - ((max_num_len * 2) + 3)
    carre = "\033[47m \033[0m"
    for i in lst:
        percent = (i / (len(lst) - 1))
        print(f"{int(percent * 100):>3}{"%|"}", end="")
        for x in range(int(term_width * percent)):
            print(f"{carre}", end="")
        for x in range(int(term_width * percent), term_width):
            print(" ", end="")
        print(f"{"| "}{i + 1:>{max_num_len}}{'/'}{lst[-1] + 1}", end="")
        if (i != lst[-1]):
            yield print('\r', end="")
        else:
            print("")
