import sys


def main() -> int:
    args = sys.argv
    size = len(args)
    # print(size)
    # for i in range(1, size):
    #     print(i)
    if size == 0:
        return 0
    elif size > 2:
        s = "AssertionError: more than one argument is provided"
        raise AssertionError(s)
    try:
        i = int(args[1])
        if i % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except Exception as e:
        raise AssertionError("AssertionError: argument is not an integer")
        print(e)
    return


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
