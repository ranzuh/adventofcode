import sys
import pathlib
import parse
import collections

def get_priority(item):
    ascii = ord(item)
    
    if ascii >= 97 and ascii <= 122:
        priority = ascii-96
    elif ascii >= 65 and ascii <= 90:
        priority = ascii-38
    
    return priority

def part1(data):
    sum = 0
    for item in data:
        left_half = item[:len(item)//2]
        right_half = item[len(item)//2:]

        common = ''
        for i in left_half:
            for j in right_half:
                if i == j:
                    common = i
                    break
        
        sum += get_priority(common)

    return sum

def part2(data):
    sum = 0
    for i in range(0, len(data), 3):
        rucksacks = data[i:i+3]
        common = ''
        for i in rucksacks[0]:
            for j in rucksacks[1]:
                if i == j:
                    for k in rucksacks[2]:
                        if j == k:
                            common = k
        
        sum += get_priority(common)
    
    return sum

if __name__ == "__main__":
    path = sys.argv[0][:-3] + ".txt"
    data = pathlib.Path(path).read_text().splitlines()
    output1 = part1(data)
    output2 = part2(data)
    print(output1, output2)