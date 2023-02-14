import sys
from collections import Counter


def check_condition(my_block, height, min_duration) -> (bool, int):
    global ground

    duration = 0
    for h in ground:
        if h == height:
            continue
        elif h > height:
            duration += (h - height) * 2
            my_block += (h - height)
        else:
            duration += (height - h)
            my_block -= (height - h)

    if my_block < 0:
        return False, min_duration
    elif duration < min_duration:
        return True, duration
    else:
        return False, min_duration


row, col, my_block = map(int, sys.stdin.readline().split())
ground = []
for _ in range(row):
    ground += list(map(int, sys.stdin.readline().split()))

min_duration = 500 * 500 * 257 * 2
max_height = -1
for h in range(max(ground), min(ground)-1, -1):
    result, min_duration = check_condition(my_block, h, min_duration)
    if result:
        max_height = h

print(min_duration, max_height)
