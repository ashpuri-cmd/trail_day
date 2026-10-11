from textwrap import shorten as trim
from math import floor, ceil
from string import ascii_uppercase, digits
from datetime import date
from datetime import timedelta as gap


def main():
    print(trim("Pack light and start early to beat the heat", 20))
    print("Water stops:", floor(7 / 2), "to", ceil(7 / 2))
    print("Tag:", ascii_uppercase[:3] + digits[:3])
    print("Back by:", date(2026, 10, 10) + gap(days=2))


if __name__ == "__main__":
    main()
