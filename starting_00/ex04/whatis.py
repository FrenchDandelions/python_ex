import sys


def main() -> int:
    args = sys.argv
    size = len(args)
    if size == 1:
        return 0
    s = "more than one argument is provided"
    if size != 2:
        raise AssertionError(s)
    try:
        i = int(args[1])
        if i % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except Exception as e:
        raise AssertionError("argument is not an integer")
        print(e)
    return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as k:
        print(type(k).__name__, k, sep=": ")
    except EOFError as eof:
        print(type(eof).__name__, eof, sep=": ")
    except Exception as e:
        print(type(e).__name__, e, sep=": ")
