import sys

T = int(sys.stdin.readline())
for _ in range(T):
    items = {}
    N = int(sys.stdin.readline())
    for _ in range(N):
        name, type_ = sys.stdin.readline().split()
        if type_ in items.keys():
            items[type_] += 1
        else:
            items[type_] = 1

    count = 1
    for v in items.values():
        count *= (v+1)
    print(count-1)
