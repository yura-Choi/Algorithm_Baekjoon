# x 를 1 또는 2로 표현할 때의 경우의 수 return
def dp(x):
    if x < 1:
        return 0
    if x == 1 or x == 2:
        return x

    if cache[x] != 0:
        return cache[x]

    cache[x] = dp(x-2) + dp(x-1)
    return cache[x]


N = int(input())
cache = [0] * (N+1)

print(dp(N) % 10007)