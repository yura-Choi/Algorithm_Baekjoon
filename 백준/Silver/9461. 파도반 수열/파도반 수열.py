import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    cache = [0, 1, 1, 1, 2, 2, 3, 4, 5]

    for i in range(9, N+1):
        cache.append(cache[i-1] + cache[i-5])

    print(cache[N])
