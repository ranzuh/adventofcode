import sys
import pathlib
import parse

def part1(data):
    scores = {
        'A X': 1 + 3,
        'A Y': 2 + 6,
        'A Z': 3 + 0,
        'B X': 1 + 0,
        'B Y': 2 + 3,
        'B Z': 3 + 6,
        'C X': 1 + 6,
        'C Y': 2 + 0,
        'C Z': 3 + 3,
    }

    total_score = 0
    for round in data:
        total_score += scores[round]
    return total_score

def part2(data):
    scores = {
        'A X': 3 + 0,
        'A Y': 1 + 3,
        'A Z': 2 + 6,
        'B X': 1 + 0,
        'B Y': 2 + 3,
        'B Z': 3 + 6,
        'C X': 2 + 0,
        'C Y': 3 + 3,
        'C Z': 1 + 6,
    }

    total_score = 0
    for round in data:
        total_score += scores[round]
    return total_score

if __name__ == "__main__":
    path = sys.argv[0][:-3] + ".txt"
    data = pathlib.Path(path).read_text().splitlines()
    output1 = part1(data)
    output2 = part2(data)
    print(output1, output2)