N = int(input())
cache = [0] * (N+1)

for x in range(1, N+1):
    if x <= 3:
        cache[x] = x
    else:
        cache[x] = ((cache[x-1] % 10007) + (cache[x-2] % 10007)) % 10007

print(cache[N])