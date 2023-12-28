def solution(S):
    stack = []
    counter = 0

    for char in S:
        if not stack:
            stack.append(char)
        else:
            if char == stack[-1]:
                stack.append(char)
            else:
                if len(stack) >= 3:
                    counter += len(stack) // 3
                stack = [char]

    if len(stack) >= 3:
        counter += len(stack) // 3

    return counter