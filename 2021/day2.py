import sys
import pathlib

def part1(input):
    horizontal_pos = 0
    depth = 0

    for line in input:
        cmd, val = line.split()
        if cmd == "forward":
            horizontal_pos += int(val)
        elif cmd == "up":
            depth -= int(val)
        elif cmd == "down":
            depth += int(val)
    
    return horizontal_pos * depth

def part2(input):
    horizontal_pos = 0
    depth = 0
    aim = 0

    for line in input:
        cmd, val = line.split()
        if cmd == "forward":
            horizontal_pos += int(val)
            depth += aim * int(val)
        elif cmd == "up":
            aim -= int(val)
        elif cmd == "down":
            aim += int(val)
    
    return horizontal_pos * depth

if __name__ == "__main__":
    path = sys.argv[1]
    input = pathlib.Path(path).read_text().splitlines()
    output1 = part1(input)
    output2 = part2(input)
    print(output1, output2)