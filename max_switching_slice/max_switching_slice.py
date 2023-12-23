def solution(A):
    if len(A) == 1:
        return 1
    elif len(A) == 2:
        return 2
    elif len(A) == 3:
        return 3 if A[0] == A[2] else 2
    
    max_length = 2
    curr_length = 2
    first = A[0]
    second = A[1]

    for i in range(2, len(A)):
        if i == len(A) - 1:
            if A[i] == first:
                curr_length += 1
            if curr_length > max_length:
                max_length = curr_length
        else:
            if A[i] == first:
                curr_length += 1
                if A[i + 1] == second:
                    curr_length += 1
                    i += 1
                else:
                    if curr_length > max_length:
                        max_length = curr_length
                    curr_length = 2
                    first = A[i]
                    second = A[i + 1]
                    i += 1
            else:
                if curr_length > max_length:
                    max_length = curr_length
                curr_length = 2
                first = A[i - 1]
                second = A[i]

    if curr_length > max_length:
        max_length = curr_length

    return max_length
