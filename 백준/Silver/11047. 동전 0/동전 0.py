import sys

N, K = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(N)]
coin.sort(reverse=True)

count = 0
for money in coin:
    if money > K:
        continue

    while K >= money:
        count += int(K / money)
        K %= money

    if K <= 0:
        break

print(count)