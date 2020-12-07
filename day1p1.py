import sys

# You'll need to paste numbers to stdin and close it with CTRL-Z
s = sys.stdin.read()
s = str(s)
list = s.splitlines()

for i in range(len(list)):
    for j in list[i:]:
        if int(list[i]) + int(j) == 2020:
            print(int(list[i]), "+", int(j), "=", 2020)
            print("Answer is", int(list[i]) * int(j))