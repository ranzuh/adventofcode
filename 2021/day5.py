import sys
import pathlib
import parse
from collections import Counter

def part1(input):
    output = []
    for line in data:
        parsed = parse.parse("{},{} -> {},{}", line)
        start = (int(parsed[0]), int(parsed[1]))
        end = (int(parsed[2]), int(parsed[3]))
        if start[0] == end[0] or start[1] == end[1]:
            for x in range(min(start[0], end[0]), max(start[0], end[0])+1):
                for y in range(min(start[1], end[1]), max(start[1], end[1])+1):
                    output.append((x,y))
        else:
            for x in range(min(start[0], end[0]), max(start[0], end[0])+1):
                print(x)

    values = list(Counter(output).values())

    return sum(1 for i in values if i >= 2)

def part2(input):
    pass

if __name__ == "__main__":
    path = sys.argv[1]
    data = pathlib.Path(path).read_text().splitlines()
    output1 = part1(data)
    output2 = part2(data)
    print(output1, output2)