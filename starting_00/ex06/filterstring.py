import sys
from ft_filter import ft_filter


def filter_string():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        try:
            N = int(sys.argv[2])
        except Exception:
            raise AssertionError(
                "the arguments are bad")
        S = str(sys.argv[1])
        lst = list(ft_filter(lambda word: len(word) > N, S.split()))
        print(lst)
    except AssertionError as e:
        print(type(e).__name__, e, sep=": ")
    except Exception as e:
        print(e)
    return


def main():
    filter_string()


if __name__ == "__main__":
    main()
