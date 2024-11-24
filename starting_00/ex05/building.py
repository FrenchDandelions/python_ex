import sys


def main():
    """***
This main takes a string as parameter and if no string
is provided, input is requested from the user
***"""
    args = sys.argv
    num_ags = len(args)
    assert num_ags <= 2, "AssertionError: more than one argument is provided"
    s = ""
    if num_ags == 1:
        print("What is the text to count?")
        s = input()
    else:
        s = args[1]
    num = {"UP": 0, "LOW": 0, "SPACE": 0, "PUNC": 0, "DIGITS": 0}
    punc = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for i in s:
        if i.isupper():
            num["UP"] += 1
        elif i.isnumeric():
            num["DIGITS"] += 1
        elif i.islower():
            num["LOW"] += 1
        elif i in punc:
            num["PUNC"] += 1
        elif i.isspace():
            num["SPACE"] += 1
    print(f"The text contains {len(s)} characters:")
    print(f"{num['UP']} upper letters")
    print(f"{num['LOW']} lower letters")
    print(f"{num['PUNC']} punctuation marks")
    print(f"{num['SPACE']} spaces")
    print(f"{num['DIGITS']} digits")
    return


if __name__ == "__main__":
    try:
        # print(main.__doc__)
        main()
    except Exception as e:
        print(e)
