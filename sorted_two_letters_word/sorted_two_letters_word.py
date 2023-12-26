def solution(S):
    a = 0
    b = 0
    
    # First Loop
    for i in range(len(S)):
        if S[i] == 'A':
            a += 1

    # Intermediate Assignment
    ans = a

    # Second Loop
    for i in range(len(S)):
        if S[i] == 'A':
            a -= 1
        else:
            b += 1
        
        # Update Minimum Count
        ans = min(ans, a + b)

    # Return Result
    return ans
