import sys
import math as m
import json
import calendar as cal
from statistics import median

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python basics.py NAME")
    name = sys.argv[1]
    print("Hiker:", name)
    print("Tent side:", m.sqrt(49))
    print("Leap year:", cal.isleap(2028))
    print(json.dumps({"hiker": name, "days": 2}))
    print("Typical pace:", median([2, 3, 7]))


if __name__ == "__main__":
    main()
