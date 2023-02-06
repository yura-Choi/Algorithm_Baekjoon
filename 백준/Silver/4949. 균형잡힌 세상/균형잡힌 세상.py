import sys

while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == ".":
        break

    stack = []
    result = "yes"
    for alpha in sentence:
        if alpha == "(" or alpha == "[":
            stack.append(alpha)
        elif alpha == ")":
            if len(stack) == 0 or stack.pop() != "(":
                result = "no"
                break
        elif alpha == "]":
            if len(stack) == 0 or stack.pop() != "[":
                result = "no"
                break

    if len(stack) != 0:
        result = "no"
    print(result)
