import sys
import pathlib
from parse import parse
from collections import Counter

def part1(data):
    data = data[0]
    for i in range(len(data)-3):
        if len(Counter(data[i:i+4]).keys()) == 4:
            return i+4

def part2(data):
    data = data[0]
    for i in range(len(data)-13):
        if len(Counter(data[i:i+14]).keys()) == 14:
            return i+14

if __name__ == "__main__":
    path = sys.argv[0][:-3] + ".txt"
    data = pathlib.Path(path).read_text().splitlines()
    output1 = part1(data)
    output2 = part2(data)
    print(output1, output2)