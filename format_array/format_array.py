def solution(A, K):
    longest_length = len(str(A[0]))
    
    # Find the longest length in the array
    for num in A:
        longest_length = max(longest_length, len(str(num)))
    
    curr_idx = 0
    
    # Print the table
    for i in range(1, (len(A) // K) + 1):
        # Print the top border of the row
        edge = '+' + '-'.rjust(longest_length, '-') + '+'
        print(edge * K)
        
        # Print the numbers in the row
        num_row = '|'
        for j in range(K):
            space_needed = longest_length - len(str(A[curr_idx]))
            num_row += ' ' * space_needed + str(A[curr_idx]) + '|'
            curr_idx += 1
        print(num_row)
    
    # Print the top border of the last row
    near_last_edge = K if (len(A) // K) >= 1 else len(A) % K
    edge = '+' + '-'.rjust(longest_length, '-') + '+'
    print(edge * near_last_edge)
    
    # Print the numbers in the last row
    if len(A) % K != 0:
        num_row = '|'
        for j in range(len(A) % K):
            space_needed = longest_length - len(str(A[curr_idx]))
            num_row += ' ' * space_needed + str(A[curr_idx]) + '|'
            curr_idx += 1
        print(num_row)
        
        # Print the bottom border of the last row
        edge = '+' + '-'.rjust(longest_length, '-') + '+'
        print(edge * (len(A) % K))
