from tqdm import tqdm
from time import sleep
from Loading import ft_tqdm
import sys


def main() -> None:
    n = int(input("Please put the number of iterations necessary: "))
    t = float(input("Please, put the time to sleep between each iterations: "))
    a = ["a", "b", "c"]
    for elem in tqdm(range(n), file=sys.stdout):
        sleep(t)
    for elem in ft_tqdm(range(n)):
        sleep(t)
    s = "Please give us the list to iterate over, separated by a space: "
    a = input(s).split()
    list_a, list_b = [], []
    for elem in tqdm(a, file=sys.stdout):
        list_a.append(elem)
        sleep(t)
    for elem in ft_tqdm(a):
        list_b.append(elem)
        sleep(t)
    print("This is the list with the real tqdm:", *list_a)
    print("This is the list with the ft_tqdm:", *list_b)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as k:
        print(type(k).__name__, k, sep=": ")
    except EOFError as eof:
        print(type(eof).__name__, eof, sep=": ")
    except Exception as e:
        print(type(e).__name__, e)
