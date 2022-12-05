import sys
import pathlib
import parse

def part1(data):
    calorie_sum = 0
    max_sum = 0
    for calorie in data:
        if calorie == '':
            if calorie_sum > max_sum:
                max_sum = calorie_sum
            calorie_sum = 0
        else:
            calorie_sum += int(calorie)
    return max_sum

def part2(input):
    calorie_sum = 0
    sums = []
    for calorie in data:
        if calorie == '':
            sums.append(calorie_sum)
            calorie_sum = 0
        else:
            calorie_sum += int(calorie)
    sums.sort()
    return sum(sums[-3:])

if __name__ == "__main__":
    path = sys.argv[0][:-3] + ".txt"
    data = pathlib.Path(path).read_text().splitlines()
    output1 = part1(data)
    output2 = part2(data)
    print(output1, output2)