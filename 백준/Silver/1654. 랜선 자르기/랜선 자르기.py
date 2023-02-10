import sys

count_tohave, count_tomake = map(int, sys.stdin.readline().split())
cable = []
for _ in range(count_tohave):
    cable.append(int(sys.stdin.readline()))

# parametric search
start, end = 1, max(cable)
save_status = -1
while start <= end:
    mid = (start + end) // 2

    # condition check
    count = 0
    for e in cable:
        count += e // mid
    if count >= count_tomake: # go to longer length
        start = mid + 1
        save_status = mid
    else: # go to shorter length
        end = mid - 1

print(save_status)