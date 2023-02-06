import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    data = sys.stdin.readline().split()
    data[0] = int(data[0])
    arr.append(data)

arr.sort(key=lambda x : (x[0]))

for data in arr:
    print(data[0], data[1])