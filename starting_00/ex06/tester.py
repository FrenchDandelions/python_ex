from ft_filter import ft_filter


def main():
    print(list(ft_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))  # Output: [2, 4]
    print(list(ft_filter(None, [0, 1, 2, 3, 4])))
    print(ft_filter.__doc__)
    print(filter.__doc__)
    print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))  # Output: [2, 4]
    print(list(filter(None, [0, 1, 2, 3, 4])))
    return

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
