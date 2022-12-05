import sys
import pathlib

def part1(input):
    increases = 0
    previous_measure = input[0]
    for measure in input:
        if measure > previous_measure:
            increases += 1
        previous_measure = measure
    return increases

def part2(input):
    increases = 0
    previous_window = list(map(int, input[:3]))
    for i in range(len(input) - 2):
        current_window = list(map(int, input[i:i+3]))
        if sum(current_window) > sum(previous_window):
            #print("increases", sum(current_window), sum(previous_window))
            increases += 1
        #else:
            #print("decreases", sum(current_window), sum(previous_window))
        previous_window = current_window
    return increases

if __name__ == "__main__":
    path = sys.argv[1]
    input = pathlib.Path(path).read_text().splitlines()
    output = part2(input)
    print(output)