N = int(input())

count, temp = 0, N
flag = False

while temp != 0:
    if not flag and temp >= 5: # 5의 배수
        count += 1
        temp -= 5
    elif temp % 3 == 0: # 5보다 작으면서 나머지가 3의 배수일 경우 or 5로는 나누어떨어지지 않으면서 나머지가 3의 배수인 경우
        if temp == N:
            count = temp // 3
        else:
            count += temp // 3
        temp = 0 # 종료 조건
    else: # 5보다 작지만 나머지가 3의 배수로 나오지 않는 경우
        temp += 5
        count -= 1
        flag = True

    if flag and temp > N: # 3, 5로 표현되지 않는 수일 경우
        count = -1
        break

print(count)
