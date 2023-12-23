def solution(S):
    A = 0
    B = 0
    N = 0

    # Count the occurrences of 'A', 'B', and 'N'
    for char in S:
        if char == 'B':
            B += 1
        if char == 'A':
            A += 1
        if char == 'N':
            N += 1

    counter = 0

    # Repeat the pattern 'BAN' as long as there are enough 'B', 'A', and 'N'
    while B >= 1 and A >= 3 and N >= 2:
        B -= 1
        A -= 3
        N -= 2
        counter += 1

    return counter
