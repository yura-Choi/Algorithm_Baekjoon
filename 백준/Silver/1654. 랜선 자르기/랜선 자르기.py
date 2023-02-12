import sys


def check_condition(cable, length, goal) -> bool:
    count = 0
    for e in cable:
        count += e // length
    if count >= goal:
        return True
    else:
        return False


count_tohave, count_tomake = map(int, sys.stdin.readline().split())
cable = []
for _ in range(count_tohave):
    cable.append(int(sys.stdin.readline()))

# parametric search
low, high = 1, max(cable) + 1
while (high - low) > 1:
    mid = (high + low) // 2
    if check_condition(cable, mid, count_tomake):
        low = mid
    else:
        high = mid

print(low)
