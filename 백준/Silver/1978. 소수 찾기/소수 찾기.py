N = int(input())
arr = list(map(int, input().split()))

def validate(num: int) -> bool:
    cnt = 0
    for i in range(2, num+1):
        if num % i == 0:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False

count = 0
for num in arr:
    if validate(num):
        count += 1
print(count)