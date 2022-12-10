import sys
import pathlib
from parse import parse

def part1(data):
    cycle = 1
    register = 1
    signal_sum = 0
    for line in data:
        if line == "noop":
            if cycle == 20 or (cycle-20) % 40 == 0:
                #print(register, cycle, cycle*register)
                signal_sum += cycle*register
            cycle += 1
        else:
            for i in range(2):
                if cycle == 20 or (cycle-20) % 40 == 0:
                    #print(register, cycle, cycle*register)
                    signal_sum += cycle*register
                cycle += 1
            value = parse("addx {:d}", line)[0]
            register += value
    return signal_sum

def handle_crt_drawing(position, register, cycle, crt_row, crt_rows):
    if position in [register-1, register, register+1]:
        crt_row += "#"
    else:
        crt_row += "."
    cycle += 1
    position += 1
    if position == 40:
        crt_rows.append(crt_row)
        crt_row = ""
        position = 0
    return position, register, cycle, crt_row, crt_rows

def part2(data):
    cycle = 1
    register = 1
    signal_sum = 0
    position = 0

    crt_rows = []
    crt_row = ""

    for line in data:
        if line == "noop":
            position, register, cycle, crt_row, crt_rows = \
                handle_crt_drawing(position, register, cycle, crt_row, crt_rows)
        else:
            for i in range(2):
                position, register, cycle, crt_row, crt_rows = \
                    handle_crt_drawing(position, register, cycle, crt_row, crt_rows)
            value = parse("addx {:d}", line)[0]
            register += value
    
    [print(row) for row in crt_rows]
    

if __name__ == "__main__":
    path = sys.argv[0][:-3] + ".txt"
    data = pathlib.Path(path).read_text().splitlines()
    output1 = part1(data)
    output2 = part2(data)
    print(output1, output2)