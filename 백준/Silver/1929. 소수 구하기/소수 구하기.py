import math

start, end = map(int, input().split())
net = [e for e in range(end+1)]
pointer = 2

net[1] = 0
while pointer <= math.sqrt(end):
    for i in range(pointer*2, end+1, pointer):
        net[i] = 0

    # 다음으로 가장 작은 소수 찾기
    while True:
        pointer += 1
        if net[pointer] != 0:
            break

for i in range(start, end+1):
    if net[i] != 0:
        print(net[i])