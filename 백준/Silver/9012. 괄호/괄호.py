import sys
from collections import deque

def test_vps(ps: str) -> bool:
    stack = deque()
    for alpha in ps:
        if alpha == "(":
            stack.append("(")
        else:
            if len(stack) == 0 or stack.pop() != "(":
                return False

    if len(stack) == 0:
        return True
    else:
        return False

T = int(sys.stdin.readline())

for i in range(T):
    ps = sys.stdin.readline().rstrip()
    if test_vps(ps):
        print("YES")
    else:
        print("NO")
