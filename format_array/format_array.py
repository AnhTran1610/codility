def solution(A, K):
    longest_length = len(str(A[0]))

    # Find the longest length in the array
    for num in A:
        longest_length = max(longest_length, len(str(num)))

    curr_idx = 0

    for i in range(1, (len(A) // K) + 1):
        # Print the top border of the row
        edge = ''
        for j in range(1, K + 1):
            edge += '+' + '-'.rjust(longest_length, '-')
        edge += '+'
        print(edge)

        # Print the numbers in the row
        num_row = '|'
        for j in range(1, K + 1):
            space_needed = longest_length - len(str(A[curr_idx]))
            num_row += ' ' * space_needed + str(A[curr_idx]) + '|'
            curr_idx += 1
        print(num_row)

    near_last_edge = K if (len(A) // K) >= 1 else len(A) % K
    edge = ''
    for j in range(1, near_last_edge + 1):
        edge += '+' + '-'.rjust(longest_length, '-')
    edge += '+'
    print(edge)

    if len(A) % K != 0:
        num_row = '|'
        for j in range(1, len(A) % K + 1):
            space_needed = longest_length - len(str(A[curr_idx]))
            num_row += ' ' * space_needed + str(A[curr_idx]) + '|'
            curr_idx += 1
        print(num_row)

        # Print the bottom border of the last row
        edge = ''
        for j in range(1, len(A) % K + 1):
            edge += '+' + '-'.rjust(longest_length, '-')
        edge += '+'
        print(edge)
