import sys
import pathlib
from parse import parse

def part1(data):
    matching_char = {
        ")" : "(",
        "]" : "[",
        "}" : "{",
        ">" : "<",
    }

    scores = {
        ")" : 3,
        "]" : 57,
        "}" : 1197,
        ">" : 25137,
    }
    
    illegal_chars = []

    for current_line in data:
        line_done = False
        while not line_done:
            for i in range(1, len(current_line)):
                if current_line[i] in [")", "]", "}", ">"]:
                    if current_line[i-1] == matching_char[current_line[i]]:
                        current_line = current_line[:i-1] + current_line[i+1:]
                        break
                    else:
                        illegal_chars.append(current_line[i])
                        line_done = True
                        break
                if i == len(current_line)-1:
                    line_done = True
    
    illegal_scores = [scores[char] for char in illegal_chars]

    return sum(illegal_scores)



def part2(data):
    matching_char = {
        ")" : "(",
        "]" : "[",
        "}" : "{",
        ">" : "<",
    }

    scores = {
        "(" : 1,
        "[" : 2,
        "{" : 3,
        "<" : 4,
    }
    
    incomplete_sequences = []

    for current_line in data:
        line_done = False
        while not line_done:
            for i in range(1, len(current_line)):
                if current_line[i] in [")", "]", "}", ">"]:
                    if current_line[i-1] == matching_char[current_line[i]]:
                        current_line = current_line[:i-1] + current_line[i+1:]
                        break
                    else:
                        line_done = True
                        break
                if i == len(current_line)-1:
                    incomplete_sequences.append(current_line[::-1])
                    line_done = True
    
    sums = []
    for seq in incomplete_sequences:
        sum = 0
        for c in seq:
            sum = sum * 5 + scores[c]
        sums.append(sum)
    
    sums.sort()

    return sums[len(sums)//2]

if __name__ == "__main__":
    path = sys.argv[0][:-3] + ".txt"
    data = pathlib.Path(path).read_text().splitlines()
    output1 = part1(data)
    output2 = part2(data)
    print(output1, output2)