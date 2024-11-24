import sys


def getMorse() -> dict:
    """
This function returns a dict containing all the necessary keys to decode
a string with alphanum characters to a morse code"""
    return {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        " ": "/",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----"
    }


def main() -> None:
    """This is the main function to decode"""
    morse = getMorse()
    assert len(sys.argv) == 2, "the arguments are bad"
    line = sys.argv[1].upper()
    assert not any(i not in morse for i in line), "the arguments are bad"
    line = [morse[i] for i in line]
    print(*line)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(type(e).__name__, e, sep=": ")
