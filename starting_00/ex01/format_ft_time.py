import time
from datetime import datetime


def main():
    cur_t = time.time()
    print(f"Seconds since January 1, 1970: {cur_t:,}", end='')
    print(f" or {cur_t:.2e} in scientific notation")
    cur_t = datetime.now()
    formatted_date = cur_t.strftime("%b %d %Y")
    print(formatted_date)


if __name__ == "__main__":
    main()
