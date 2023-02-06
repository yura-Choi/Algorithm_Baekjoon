import sys
from collections import deque

stack = deque()
size = 0

N = int(sys.stdin.readline())
for i in range(N):
    command = list(sys.stdin.readline().split())
    if command[0] == "push":
        stack.append(command[1])
        size += 1
    elif command[0] == "pop":
        if size == 0:
            print(-1)
        else:
            print(stack.pop())
            size -= 1
    elif command[0] == "size":
        print(size)
    elif command[0] == "empty":
        print(1 if size == 0 else 0)
    elif command[0] == "top":
        if size == 0:
            print(-1)
        else:
            print(stack[size-1])