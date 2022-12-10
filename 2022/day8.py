import sys
import pathlib
from parse import parse
import numpy as np
import math

def part1(data):
    num_visible = 0
    for row in range(len(data)):
        for col in range(len(data[0])):
            value = int(data[row][col])
            visible = [1, 1, 1, 1]
            # check from left
            for left in range(col):
                if int(data[row][left]) >= value:
                    visible[0] = 0
            # check from right
            for right in range(col+1, len(data[0])):
                if int(data[row][right]) >= value:
                    visible[1] = 0
            # check from up
            for up in range(row):
                if int(data[up][col]) >= value:
                    visible[2] = 0
            # check from down
            for down in range(row+1, len(data)):
                if int(data[down][col]) >= value:
                    visible[3] = 0
            
            if sum(visible) != 0:
                num_visible += 1
    return num_visible

def part2(data):
    best_score = 0
    for row in range(len(data)):
        for col in range(len(data[0])):
            value = int(data[row][col])
            sees_trees = [0, 0, 0, 0]
            # check from left
            for left in reversed(range(col)):
                if int(data[row][left]) < value:
                    sees_trees[0] += 1
                else:
                    sees_trees[0] += 1
                    break
            # check from right
            for right in range(col+1, len(data[0])):
                if int(data[row][right]) < value:
                    sees_trees[1] += 1
                else:
                    sees_trees[1] += 1
                    break
            # check from up
            for up in reversed(range(row)):
                if int(data[up][col]) < value:
                    sees_trees[2] += 1
                else:
                    sees_trees[2] += 1
                    break
            # check from down
            for down in range(row+1, len(data)):
                if int(data[down][col]) < value:
                    sees_trees[3] += 1
                else:
                    sees_trees[3] += 1
                    break
            
            score = np.prod(sees_trees)
            if score > best_score:
                best_score = score
            
    return best_score

if __name__ == "__main__":
    path = sys.argv[0][:-3] + ".txt"
    data = pathlib.Path(path).read_text().splitlines()
    output1 = part1(data)
    output2 = part2(data)
    print(output1, output2)