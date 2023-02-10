import sys

n = int(sys.stdin.readline())
input_arr = []
for _ in range(n):
    input_arr.append(int(sys.stdin.readline()))
result_str = ""

stack = []
num = 1
for e in input_arr:
    while len(stack) == 0 or e != stack[-1]:
        if num > n:
            break
        stack.append(num)
        result_str += "+\n"
        num += 1

    if len(stack) == 0 and num > n:
        result_str = "NO"
        break
    else:
        item = stack.pop()
        if item != e:
            result_str = "NO"
            break
        result_str += "-\n"

sys.stdout.write(result_str)
