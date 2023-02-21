N = int(input())
cache = [0] * (N+1)

for i in range(1, N+1):
    if i == 1:
        cache[i] = 1
    elif i == 2:
        cache[i] = 3
    else:
        cache[i] = cache[i-2] * 2 + cache[i-1]

print(cache[N] % 10007)