N = int(input())

max_count = (N // 3) + 1
result = -1

for b5 in range(max_count, -1, -1):
    for b3 in range(max_count, -1, -1):
        total_sugar = (b5 * 5) + (b3 * 3)
        if total_sugar == N:
            result = b5 + b3
            break
    if result != -1:
        break

print(result)