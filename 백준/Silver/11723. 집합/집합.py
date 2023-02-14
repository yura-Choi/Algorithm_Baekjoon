import sys

N = int(sys.stdin.readline())
S = 0

for _ in range(N):
    command = list(sys.stdin.readline().split())
    x = int(command[1]) if len(command) > 1 else 0

    if command[0] == "add":
        S |= (1 << x)
    elif command[0] == "remove":
        S &= ~(1 << x)
    elif command[0] == "check":
        print(1 if S & (1 << x) else 0)
    elif command[0] == "toggle":
        S ^= (1 << x)
    elif command[0] == "all":
        S = 2097151
    else: # empty
        S = 0