import sys
import pathlib
import parse
import numpy as np

def part1(data):
    list_of_strings = data[0].split(',')
    fish = np.array(list_of_strings, dtype=np.int32)
    
    for i in range(80):
        fish_size = fish.shape[0]
        zeros = fish_size - np.count_nonzero(fish)
        fish = np.where(fish == 0, 7, fish)
        fish = np.concatenate((fish, np.ones(zeros, dtype=np.int32)*9))
        fish -= 1
    
    return fish.shape[0]

def part2(data):
    import collections

    list_of_strings = data[0].split(',')
    fish = np.array(list_of_strings, dtype=np.int64)
    counts = collections.Counter(fish)
    fish = np.zeros(9, dtype=np.int64)

    for value, count in counts.items():
        fish[value] = count

    for i in range(256):
        fish = np.roll(fish, -1)
        fish[6] += fish[8]
    
    return fish.sum(dtype=np.int64)

if __name__ == "__main__":
    path = sys.argv[0][:-3] + ".txt"
    data = pathlib.Path(path).read_text().splitlines()
    output1 = part1(data)
    output2 = part2(data)
    print(output1, output2)