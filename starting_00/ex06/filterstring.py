import sys
from ft_filter import ft_filter


def filter_string():
    """this function calls the ft_filter function.
    It gets the sys args and apply a lambda function that filters
    the first arg
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        try:
            N = int(sys.argv[2])
        except Exception:
            raise AssertionError(
                "the arguments are bad")
        S = str(sys.argv[1])
        lst = list(ft_filter(lambda word: len(word) > N, S.split()))
        print(lst)
    except KeyboardInterrupt as k:
        print(type(k).__name__, k, sep=": ")
    except EOFError as eof:
        print(type(eof).__name__, eof, sep=": ")
    except AssertionError as e:
        print(type(e).__name__, e, sep=": ")
    except Exception as e:
        print(e)
    return


def main():
    filter_string()


if __name__ == "__main__":
    main()
