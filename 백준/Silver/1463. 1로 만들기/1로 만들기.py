x = int(input())
cache = [-1] * x


def solve(n):
    global cache

    if n == 1:
        return 0

    if cache[n-1] != -1:
        return cache[n-1]

    if n % 3 == 0 and n % 2 == 0:
        cache[n-1] = 1 + min(solve(n//3), solve(n//2))
    elif n % 3 == 0:
        cache[n-1] = 1 + min(solve(n//3), solve(n-1))
    elif n % 2 == 0:
        cache[n-1] = 1 + min(solve(n//2), solve(n-1))
    else:
        cache[n-1] = 1 + solve(n-1)

    return cache[n-1]


print(solve(x))