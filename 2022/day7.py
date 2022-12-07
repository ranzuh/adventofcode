import sys
import pathlib
from parse import parse
from collections import defaultdict
import numpy as np

def part1(data):
    folder_sizes = defaultdict(list)
    folder_encountered = defaultdict(int)
    sizesum = 0
    for line in reversed(data):
        first_char = line[0]
        if first_char == "$":
            #print("cmd", line)
            parsed = parse("$ cd {}", line)
            if parsed and parsed[0] != "..":
                #print(parsed[0])
                folder_sizes[parsed[0]].append(sizesum)
                sizesum = 0
                
        elif first_char == "d":
            #print("dir", line)
            parsed = parse("dir {}", line)
            # if parsed[0] in folder_sizes.keys():
            #     folder_encountered[parsed[0]] += 1
            sizesum += folder_sizes[parsed[0]][-1]
            
            #folder_sizes.pop(parsed[0])
        else:
            #print("file", line)
            parsed = parse("{:d} {}", line)
            sizesum += parsed[0]
    
    print(folder_sizes)
    foldsizelist = []
    for k, v in folder_sizes.items():
        for i in v:
            foldsizelist.append(i)
    print(foldsizelist)
    #print(folder_encountered)
    atmost100k = [x for x in foldsizelist if x <= 100_000 ]
    return sum(atmost100k)

def part2(data):
    folder_sizes = defaultdict(list)
    folder_encountered = defaultdict(int)
    sizesum = 0
    for line in reversed(data):
        first_char = line[0]
        if first_char == "$":
            #print("cmd", line)
            parsed = parse("$ cd {}", line)
            if parsed and parsed[0] != "..":
                #print(parsed[0])
                folder_sizes[parsed[0]].append(sizesum)
                sizesum = 0
                
        elif first_char == "d":
            #print("dir", line)
            parsed = parse("dir {}", line)
            # if parsed[0] in folder_sizes.keys():
            #     folder_encountered[parsed[0]] += 1
            sizesum += folder_sizes[parsed[0]][-1]
            
            #folder_sizes.pop(parsed[0])
        else:
            #print("file", line)
            parsed = parse("{:d} {}", line)
            sizesum += parsed[0]
    
    print(folder_sizes)
    foldsizelist = []
    for k, v in folder_sizes.items():
        for i in v:
            foldsizelist.append(i)
    print(foldsizelist)

    foldsizelist_np = np.array(foldsizelist)
    unused = 70_000_000 - foldsizelist_np
    print(unused)
    atmost100k = [x for x in foldsizelist if x <= 100_000 ]
    #return sum(atmost100k)

if __name__ == "__main__":
    path = sys.argv[0][:-3] + ".txt"
    data = pathlib.Path(path).read_text().splitlines()
    output1 = part1(data)
    output2 = part2(data)
    print(output1, output2)