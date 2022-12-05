import sys
import pathlib
import numpy as np

def part1(input_data):
    input_data = input_data.split("\n\n")

    numbers = input_data[0].split(",")
    boards = input_data[1:]
    boards = [i.split("\n") for i in boards]
    boards = [[j.split() for j in i] for i in boards]

    numbers_np = np.array(numbers, dtype=int)
    boards_np = np.array(boards, dtype=int)

    marked = np.zeros_like(boards_np)

    for num in numbers_np:
        indicies = np.where(boards_np == num)
        marked[indicies] = 1

        for i in range(len(marked)):
                    # columns                       # rows
            if 5 in marked[i].sum(axis=0) or 5 in marked[i].sum(axis=1):
                #print("board is", i+1, "number was", num)
                marked_inverse = 1 - marked[i]
                unmarked = boards_np[i] * marked_inverse
                return unmarked.sum() * num
        

def part2(input_data):
    input_data = input_data.split("\n\n")

    numbers = input_data[0].split(",")
    boards = input_data[1:]
    boards = [i.split("\n") for i in boards]
    boards = [[j.split() for j in i] for i in boards]

    numbers_np = np.array(numbers, dtype=int)
    boards_np = np.array(boards, dtype=int)

    marked = np.zeros_like(boards_np)
    winning_boards = np.zeros(len(boards_np), dtype=int)

    for num in numbers_np:
        indicies = np.where(boards_np == num)
        marked[indicies] = 1

        for i in range(len(marked)):
                    # columns                       # rows
            if 5 in marked[i].sum(axis=0) or 5 in marked[i].sum(axis=1):
                winning_boards[i] = 1
                if winning_boards.sum() == len(boards_np):
                    #print("board is", i+1, "number was", num)
                    marked_inverse = 1 - marked[i]
                    unmarked = boards_np[i] * marked_inverse
                    return unmarked.sum() * num

if __name__ == "__main__":
    path = sys.argv[1]
    input_data = pathlib.Path(path).read_text().strip()
    output1 = part1(input_data)
    output2 = part2(input_data)
    print(output1, output2)