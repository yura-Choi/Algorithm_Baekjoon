import sys

N, T = map(int, sys.stdin.readline().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))
sum_cache = [0] * (N+1)

# 각 x에 대한 0 ~ x 부분합 저장
for x in range(1, N+1):
    sum_cache[x] = sum_cache[x-1] + arr[x]

for _ in range(T):
    start, end = map(int, sys.stdin.readline().split())
    print(sum_cache[end] - sum_cache[start-1])
