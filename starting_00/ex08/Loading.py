def getBar(percentage, totalsize=67):
    """This function returns the progress bar"""
    to_fill = min(round(percentage / 100 * totalsize), totalsize)
    empty = totalsize - to_fill
    return "█" * to_fill + ' ' * empty


def ft_tqdm(lst: range) -> None:
    """This is the ft_tqdm function that takes in param a list.
This function iters over it, prints a progress bar and
returns the element of said list at x index"""
    # size_terminal = shutil.get_terminal_size().columns
    # print("Size terminal =",size_terminal, file=sys.stderr)
    size_iterable = len(lst)
    bar_length = 67
    for index in range(size_iterable):
        num = round(((index + 1) / size_iterable) * 100)
        perc = (str(num) + "%").rjust(4)
        len_totaliter = len(f'{index + 1}/{size_iterable}')
        # print("Total iter =",len_totaliter,file=sys.stderr)
        bar_length = 72 - len_totaliter
        bar = getBar(num, totalsize=bar_length)
        s = f'\r{perc}|{bar}| {index + 1}/{size_iterable}\033[?25l'
        print(s, end='', flush=True)
        if index + 1 == size_iterable:
            print("\033[?25h")
        yield lst[index]
