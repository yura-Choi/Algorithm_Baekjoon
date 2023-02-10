import sys
from collections import Counter

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

# average
average = round(sum(arr) / N)
print(average)

sorted_arr = sorted(arr)
# mid
mid = sorted_arr[N//2]
print(mid)

# most appearing
counter = Counter(arr)
most_comm = counter.most_common(N)
most_comm.sort(key=lambda x : (x[1], -x[0]), reverse=True)
count = most_comm[0][0]
if len(most_comm) > 1 and most_comm[1][1] == most_comm[0][1]:
    count = most_comm[1][0]
print(count)

# range
range_len = max(arr) - min(arr)
print(range_len)

