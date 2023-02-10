import sys
from collections import Counter

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr = sorted(arr)

# average
print(round(sum(arr) / N))

# mid
print(arr[N//2])

# most appearing
counter = Counter(arr)
most_comm = counter.most_common()
most_comm.sort(key=lambda x : (x[1], -x[0]), reverse=True)
if len(most_comm) > 1 and most_comm[1][1] == most_comm[0][1]:
    print(most_comm[1][0])
else:
    print(most_comm[0][0])

# range
print(arr[N-1] - arr[0])

