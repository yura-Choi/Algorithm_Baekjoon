import sys

def dp(x):
    if x == 0:
        return [1, 0]
    elif x == 1:
        return [0, 1]

    if cache[x][0] or cache[x][1]:
        return cache[x]

    dp_1 = dp(x-1)
    dp_2 = dp(x-2)
    cache[x][0] = dp_1[0] + dp_2[0]
    cache[x][1] = dp_1[1] + dp_2[1]
    return cache[x]

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    cache = [[0, 0] for _ in range(N+1)]

    print(*dp(N))