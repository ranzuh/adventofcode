import sys
from typing import List, Set, Tuple, Dict

# You'll need to paste numbers to stdin and close it with CTRL-Z
s = sys.stdin.read()
s = str(s)
list = s.splitlines()


# puzzle 1
valids = 0
for i in list:
    #split line
    splits : List[str] = i.split(' ')

    #find bounds
    minus_index = splits[0].find('-')
    lower_bound = int(splits[0][:minus_index])
    higher_bound = int(splits[0][minus_index + 1:])

    #find letter
    letter = splits[1][0]

    #calculate how many times letter is found in password
    count = splits[2].count(letter)

    # check if count is in bounds
    valid = lower_bound <= count <= higher_bound

    if valid: valids += 1

print(valids)


# puzzle 2
valids = 0
for i in list:
    #split line
    splits : List[str] = i.split(' ')

    #find positions
    minus_index = splits[0].find('-')
    position1 = int(splits[0][:minus_index])
    position2 = int(splits[0][minus_index + 1:])

    #find letter
    letter = splits[1][0]

    #check positions
    if splits[2][position1 - 1] == letter: 
        if splits[2][position2 - 1] != letter:
            valids += 1
    elif splits[2][position2 - 1] == letter:
        valids += 1

print(valids)

    

