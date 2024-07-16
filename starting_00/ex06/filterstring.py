import sys
from ft_filter import ft_filter


def filter_string():
    try:
        if len(sys.argv) != 3:
            raise AssertionError(
                "the arguments are bad")
        try:
            N = int(sys.argv[2])
        except Exception:
            raise AssertionError(
                "the arguments are bad")
        S = str(sys.argv[1])
        lst = list(ft_filter(lambda word: len(word) > N, S.split()))
        print(lst)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(e)
    return


def main():
    filter_string()


if __name__ == "__main__":
    main()
