import sys
import pathlib
import parse

def part1(data):
    count = 0
    for line in data:
        parsed = parse.parse("{}-{},{}-{}", line)
        first_pair = (int(parsed[0]), int(parsed[1]))
        second_pair = (int(parsed[2]), int(parsed[3]))
        first_set = set(range(first_pair[0], first_pair[1]+1))
        second_set = set(range(second_pair[0], second_pair[1]+1))
        intersect = first_set.intersection(second_set)
        if intersect == first_set or intersect == second_set:
            count += 1
    return count

def part2(data):
    count = 0
    for line in data:
        parsed = parse.parse("{}-{},{}-{}", line)
        first_pair = (int(parsed[0]), int(parsed[1]))
        second_pair = (int(parsed[2]), int(parsed[3]))
        first_set = set(range(first_pair[0], first_pair[1]+1))
        second_set = set(range(second_pair[0], second_pair[1]+1))
        intersect = first_set.intersection(second_set)
        if len(intersect) > 0:
            count += 1
    return count

if __name__ == "__main__":
    path = sys.argv[0][:-3] + ".txt"
    data = pathlib.Path(path).read_text().splitlines()
    output1 = part1(data)
    output2 = part2(data)
    print(output1, output2)