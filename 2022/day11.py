import sys
import pathlib
import parse
from collections import deque
import numpy as np

def parse_monkeys(data):
    parsed = parse.findall(
"""Monkey {id}:
  Starting items: {items}
  Operation: new = old {operation} {amount}
  Test: divisible by {test}
    If true: throw to monkey {true}
    If false: throw to monkey {false}""", data)
    
    monkeys = {}
    for result in parsed:
        #print(result)
        id = result.named["id"]
        items = deque([int(x) for x in result.named["items"].split(",")])
        operation = result.named["operation"]
        amount = result.named["amount"]
        test = int(result.named["test"])
        true = result.named["true"]
        false = result.named["false"]
        monkeys[id] = {}
        monkeys[id]["items"] = items
        monkeys[id]["operation"] = operation
        monkeys[id]["amount"] = amount
        monkeys[id]["test"] = test
        monkeys[id]["true"] = true
        monkeys[id]["false"] = false
        monkeys[id]["inspected"] = 0

    return monkeys

def part1(data):

    monkeys = parse_monkeys(data)

    for round in range(20):
        for monkey in monkeys.values():
            for i in range(len(monkey["items"])):
                item = monkey["items"].popleft()
                if monkey["amount"] == "old":
                    amount = item
                else:
                    amount = int(monkey["amount"])
                if monkey["operation"]== "*":
                    item *= amount
                else:
                    item += amount
                item = item // 3
                if item % monkey["test"] == 0:
                    monkeys[monkey["true"]]["items"].append(item)
                else:
                    monkeys[monkey["false"]]["items"].append(item)
                monkey["inspected"] += 1
                #[print(monkey) for monkey in monkeys.values()]
                #print()

    monkey_business = sorted([m["inspected"] for m in monkeys.values()])
    return monkey_business[-1] * monkey_business[-2]

def part2(data):
    
    monkeys = parse_monkeys(data)

    # multiply all the test divisors to get the modulus
    modulus = np.prod([monkey["test"] for monkey in monkeys.values()])

    for round in range(10000):
        for monkey in monkeys.values():
            for i in range(len(monkey["items"])):
                # set the item as the remainder when divided by the product of test divisors
                item = monkey["items"].popleft() % modulus

                if monkey["amount"] == "old":
                    amount = item
                else:
                    amount = int(monkey["amount"])
                if monkey["operation"]== "*":
                    item *= amount
                else:
                    item += amount
                if item % monkey["test"] == 0:
                    monkeys[monkey["true"]]["items"].append(item)
                else:
                    monkeys[monkey["false"]]["items"].append(item)
                monkey["inspected"] += 1
                #[print(monkey) for monkey in monkeys.values()]
                #print()
    
    monkey_business = sorted([m["inspected"] for m in monkeys.values()])
    #[print(monkey) for monkey in monkeys.values()]
    #print(monkey_business)
    return monkey_business[-1] * monkey_business[-2]

if __name__ == "__main__":
    path = sys.argv[0][:-3] + ".txt"
    data = pathlib.Path(path).read_text()# .splitlines()
    output1 = part1(data)
    output2 = part2(data)
    print(output1, output2)