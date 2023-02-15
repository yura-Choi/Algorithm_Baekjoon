N = int(input())
w_time = list(map(int, input().split()))
w_time.sort() # 소요시간이 짧은 순으로 줄을 설 때 전체 waiting 시간을 줄일 수 있다.

total_time = 0
save = [0]
for i in range(len(w_time)):
    save.append(save[i]+w_time[i])
    total_time += save[i+1]
print(total_time)
