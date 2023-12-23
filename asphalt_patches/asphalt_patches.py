def solution(S):
    count = 0
    i = 0
    while i < len(S):
        if S[i] == 'X':
            count += 1
            if i + 2 >= len(S):
                break
            i = i + 2
        else:
            i += 1
    return count
