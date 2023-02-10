N, M = map(int, input().split())
trees = list(map(int, input().split()))

# parametric search
start, end = 0, max(trees)
last_answer = -1
while start <= end:
    mid = (start + end) // 2

    # condition check
    count = 0
    for e in trees:
        if e > mid:
            count += e - mid
    if count >= M:
        start = mid + 1
        last_answer = mid
    else:
        end = mid - 1

print(last_answer)