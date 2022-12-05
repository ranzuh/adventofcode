import sys

# You'll need to paste numbers to stdin and close it with CTRL-Z
s = sys.stdin.read()
s = str(s)
list = s.splitlines()


# puzzle 1
for i in range(len(list)):
    for j in list[i:]:
        if int(list[i]) + int(j) == 2020:
            print(int(list[i]), "+", int(j), "=", 2020)
            print("Answer is", int(list[i]) * int(j))


# puzzle 2
for i in range(len(list)):
    for j in range(i, len(list)):
        for k in range(j, len(list)):
            if int(list[i]) + int(list[j]) + int(list[k]) == 2020:
                print(int(list[i]), "+", int(list[j]), "+", int(list[k]), "=", 2020)
                print("Answer is", int(list[i]) * int(list[j]) * int(list[k]))