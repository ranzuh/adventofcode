import sys
import pathlib
from parse import parse
import numpy as np

def parse_stacks_and_orders(data):
    # ugh hard coded row and collumn sizes
    all_stacks = []
    for col in [1, 5, 9, 13, 17, 21, 25, 29, 33]:
        stack = []
        for row in reversed(data[:8]):
            if row[col] != " ":
                stack.append(row[col])
        all_stacks.append(stack)

    orders = [parse("move {amount:d} from {from:d} to {to:d}", row) for row in data[10:]]

    return all_stacks, orders

def build_last_items_string(all_stacks):
    result = ""
    for stack in all_stacks:
        result += stack[-1]
    return result

def part1(data):
    all_stacks, orders = parse_stacks_and_orders(data)

    for current_order in orders:
    
        for i in range(current_order["amount"]):
            item = all_stacks[current_order["from"]-1].pop()
            all_stacks[current_order["to"]-1].append(item)
    
    return build_last_items_string(all_stacks)

def part2(data):
    all_stacks, orders = parse_stacks_and_orders(data)

    for current_order in orders:
        to_be_moved = all_stacks[current_order["from"]-1][-current_order["amount"]:]
        all_stacks[current_order["to"]-1] += to_be_moved
        for i in range(current_order["amount"]):
            all_stacks[current_order["from"]-1].pop()
    
    return build_last_items_string(all_stacks)

if __name__ == "__main__":
    path = sys.argv[0][:-3] + ".txt"
    data = pathlib.Path(path).read_text().splitlines()
    output1 = part1(data)
    output2 = part2(data)
    print(output1, output2)