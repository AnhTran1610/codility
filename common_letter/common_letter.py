def solution(S):
    for j in range(len(S[0])):
        obj = {}
        for i in range(len(S)):
            if S[i][j] not in obj:
                obj[S[i][j]] = i
            else:
                return [obj[S[i][j]], i, j]
    return []