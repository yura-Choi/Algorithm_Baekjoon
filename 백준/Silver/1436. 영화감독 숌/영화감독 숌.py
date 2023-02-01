N = int(input())
num = 0

def check_num(num: str) -> bool:
    if "666" in num:
        return True
    else:
        return False

while N > 0:
    num += 1
    if check_num(str(num)):
        N -= 1

print(num)