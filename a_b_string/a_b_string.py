def solution(S):
    flag = False
    for char in S:
        if char == 'b':
            flag = True
        if char == 'a':
            if flag:
                return False
    return True
