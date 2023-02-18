import sys


# 0 ~ x번 계단까지의 최대 점수 return
def dp(x):
    if x == 0:
        return 0

    # memoization
    if cache[x] > 0:
        return cache[x]

    if x == 1:
        cache[x] = stair_score[1]
    elif x == 2:
        cache[x] = stair_score[1] + stair_score[2]
    else:
        cache[x] = max(dp(x-2), stair_score[x-1]+dp(x-3)) + stair_score[x]

    return cache[x]


N = int(sys.stdin.readline())
stair_score = [0] + [int(sys.stdin.readline()) for _ in range(N)]
cache = [0 for _ in range(N+1)]

print(dp(N))
