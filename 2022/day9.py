import sys
import pathlib
from parse import parse
import itertools

def move_tail_after_head(dir, tail, head):
    # param dir is the (x,y) direction of the head movement
    touching = False
    # go through all 9 coordinates where the rope would be touching
    for adj_dir in set(itertools.product((-1,0,1),(-1,0,1))):
        if tail == [head[0] + adj_dir[0], head[1] + adj_dir[1]]:
            touching = True
            break
    if not touching:
        # set the tail to be after head
        tail = [head[0]-dir[0], head[1]-dir[1]]
    return tail

def part1(data):
    head = [0, 0] # x, y
    tail = [0, 0]

    tail_visited = set()

    for line in data:
        parsed = parse("{} {:d}", line)
        direction, amount = parsed[0], parsed[1]
        
        for i in range(amount):
            if direction == "R":
                head[0] += 1
                tail = move_tail_after_head((1,0), tail, head)
            if direction == "L":
                head[0] -= 1
                tail = move_tail_after_head((-1,0), tail, head)
            if direction == "U":
                head[1] += 1
                tail = move_tail_after_head((0,1), tail, head)
            if direction == "D":
                head[1] -= 1
                tail = move_tail_after_head((0,-1), tail, head)

            tail_visited.add(tuple(tail))

    return len(tail_visited)

# if the head moved diagonally, move tail according the examples
def move_diagonal(movement, tail, head):
    # returns the movement of the tail
    touching = False
    for adj_dir in set(itertools.product((-1,0,1),(-1,0,1))):
        if tail == [head[0] + adj_dir[0], head[1] + adj_dir[1]]:
            touching = True
            break

    if not touching:
        tailcopy = tail
        # if on same row or column move tail in that same column
        if tail[0] == head[0]:
            tail = [tail[0], tail[1]+movement[1]]
        elif tail[1] == head[1]:
            tail = [tail[0]+movement[0], tail[1]]
        # else move it same way as the head
        else:
            tail = [tail[0]+movement[0], tail[1]+movement[1]]
        
        movement = (tail[0]-tailcopy[0], tail[1]-tailcopy[1])
    else:
        movement = (0,0)
    return tail, movement

# if the head moved horizontal move the tail as in part1
def move_horizontal(dir, tail, head):
    # returns the movement of the tail
    touching = False
    for adj_dir in set(itertools.product((-1,0,1),(-1,0,1))):
        if tail == [head[0] + adj_dir[0], head[1] + adj_dir[1]]:
            touching = True
            break
    if not touching:
        tailcopy = tail
        # tail (1,0) head (3,0) -> tail (2,0)
        tail = [head[0]-dir[0], head[1]-dir[1]]
        movement = (tail[0]-tailcopy[0], tail[1]-tailcopy[1])
    else:
        movement = (0,0)
    return tail, movement

# for visualising the grid
def visualise(knots):
    grid = []
    x_size = 30
    y_size = 20
    for i in range(y_size):
        row = []
        for j in range(x_size):
            row.append(".")
        grid.append(row)
    
    for i, k in enumerate(knots):
        grid[k[1]+10][k[0]+10] = i
    
    for i in reversed(range(y_size)):
        for j in range(x_size):
            print(grid[i][j], end="")
        print()


def part2(data):
    knots = [[0, 0] for _ in range(10)]
    tail_visited = set()

    for line in data:
        parsed = parse("{} {:d}", line)
        direction, amount = parsed[0], parsed[1]
        
        for j in range(amount):
            copy_tail = knots[1]
            if direction == "R":
                knots[0][0] += 1
                knots[1], movement = move_horizontal((1,0), knots[1], knots[0])
                for i in range(2, 10):
                    if movement in [(1,1), (1,-1), (-1,1), (-1,-1)]:
                        # move_diagonal
                        knots[i], movement = move_diagonal(movement, knots[i], knots[i-1])
                    else:
                        # move horizontal
                        knots[i], movement = move_horizontal(movement, knots[i], knots[i-1])

            if direction == "L":
                knots[0][0] -= 1
                knots[1], movement = move_horizontal((-1,0), knots[1], knots[0])
                for i in range(2, 10):
                    if movement in [(1,1), (1,-1), (-1,1), (-1,-1)]:
                        # move_diagonal
                        knots[i], movement = move_diagonal(movement, knots[i], knots[i-1])
                    else:
                        # move horizontal
                        knots[i], movement = move_horizontal(movement, knots[i], knots[i-1])

            if direction == "U":
                knots[0][1] += 1
                knots[1], movement = move_horizontal((0,1), knots[1], knots[0])
                for i in range(2, 10):
                    if movement in [(1,1), (1,-1), (-1,1), (-1,-1)]:
                        # move_diagonal
                        knots[i], movement = move_diagonal(movement, knots[i], knots[i-1])
                    else:
                        # move horizontal
                        knots[i], movement = move_horizontal(movement, knots[i], knots[i-1])

            if direction == "D":
                knots[0][1] -= 1
                knots[1], movement = move_horizontal((0,-1), knots[1], knots[0])
                for i in range(2, 10):
                    if movement in [(1,1), (1,-1), (-1,1), (-1,-1)]:
                        # move_diagonal
                        knots[i], movement = move_diagonal(movement, knots[i], knots[i-1])
                    else:
                        # move horizontal
                        knots[i], movement = move_horizontal(movement, knots[i], knots[i-1])
            
            tail_visited.add(tuple(knots[-1]))
            #print(knots)
            
            # uncomment to visualise
            # visualise(knots)
            # input()
        
    #print(tail_visited)
    return len(tail_visited)

if __name__ == "__main__":
    path = sys.argv[0][:-3] + ".txt"
    data = pathlib.Path(path).read_text().splitlines()
    output1 = part1(data)
    output2 = part2(data)
    print(output1, output2)