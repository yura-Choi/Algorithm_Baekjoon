N = int(input())
cache = [0] * (N+1)
cache[1] = 1

for i in range(2, N+1):
    if i == 2:
        cache[i] = 3
    else:
        cache[i] = (cache[i-2] * 2 + cache[i-1]) % 10007

print(cache[N])