import sys
from typing import List, Set, Tuple, Dict

# You'll need to paste numbers to stdin and close it with CTRL-Z
s = sys.stdin.read()
s = str(s)
list = s.splitlines()

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

    

