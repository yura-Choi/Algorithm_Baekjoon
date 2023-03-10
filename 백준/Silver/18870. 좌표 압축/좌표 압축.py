import sys

N = int(sys.stdin.readline())
origin_list = list(map(int, sys.stdin.readline().split()))

num_list = sorted(list(set(origin_list)))
num_dict = {}
index = 0
for num in num_list:
    num_dict[num] = index
    index += 1

for num in origin_list:
    print(num_dict[num], end=" ")