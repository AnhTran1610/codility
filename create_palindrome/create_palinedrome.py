def solution(S):
    A = list(S)  # Convert the string to a list of characters
    low = 0
    high = len(A) - 1

    while low < high:
        if A[low] != A[high]:
            # If the characters at the current positions are not equal
            if A[low] == '?' and A[high] != '?':
                A[low] = A[high]  # Fill in '?' with the character at the opposite end
            elif A[low] != '?' and A[high] == '?':
                A[high] = A[low]  # Fill in '?' with the character at the opposite end
            else:
                return 'NO'  # If both characters are not '?' and not equal, it's not possible to form a palindrome
        else:
            # If the characters at the current positions are equal
            if A[low] == '?':
                A[low] = 'a'  # If the character is '?', fill in 'a'
                A[high] = 'a'
        low += 1
        high -= 1

    # Check if there is a single character left in the middle of the string and fill it with 'a'
    if low == high and A[low] == '?':
        A[low] = 'a'

    return ''.join(A)  # Convert the list back to a string and return the result
