def solution(S):
    res = ""
    # iterate the string
    for i in range(len(S) - 1):
        # first point where s[i] > s[i+1]
        if S[i] > S[i + 1]:
            # append the string without char index i
            for j in range(len(S)):
                if i != j:
                    res += S[j]
            return res
    # leave the last character
    res = S[0 : len(S) - 1]
    return res
