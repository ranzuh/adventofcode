import sys
import pathlib
import numpy as np

def binary_to_integer(binary):
    number = 0
    for bit in binary:
        number = (2 * number) + bit
    return number

def part1(input):
    bit_sums = np.zeros(len(input[0]))
    for binary in input:
        for i, bit in enumerate(binary):
            bit_sums[i] += int(bit)

    quotients = len(input) // bit_sums

    gamma_rate = (quotients == 1) * 1
    epsilon_rate = 1 - gamma_rate

    gamma_rate_int = binary_to_integer(gamma_rate)
    epsilon_rate_int = binary_to_integer(epsilon_rate)

    return gamma_rate_int * epsilon_rate_int

def part2(input):
    most_common = input
    for i in range(len(input[0])):
        if len(most_common) == 1:
            break
        most_common, _ = most_least_common(most_common, i)
    
    least_common = input
    for i in range(len(input[0])):
        if len(least_common) == 1:
            break
        _, least_common = most_least_common(least_common, i)
    
    most_common = [int(i) for i in most_common[0]]
    least_common = [int(i) for i in least_common[0]]

    o2_rating = binary_to_integer(most_common)
    co2_rating = binary_to_integer(least_common)
    
    return o2_rating * co2_rating

def most_least_common(input, index):
    ones = list(filter(lambda x: x[index] == '1', input))
    zeros = list(filter(lambda x: x[index] == '0', input))

    most_common = ones if len(ones) >= len(zeros) else zeros
    least_common = ones if len(ones) < len(zeros) else zeros

    return most_common, least_common

if __name__ == "__main__":
    path = sys.argv[1]
    input = pathlib.Path(path).read_text().splitlines()
    output1 = part1(input)
    output2 = part2(input)
    print(output1, output2)