import sys

N = int(sys.stdin.readline())
arr = list()
for _ in range(N):
    item = list(map(int, sys.stdin.readline().split()))
    arr.append(item)

arr = sorted(arr)
for item in arr:
    print(item[0], item[1])