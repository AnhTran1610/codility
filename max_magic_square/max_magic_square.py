def is_magic_square(A, row, col, length):
    # Calculate the sum of the first column
    sum_value = sum(A[i][col] for i in range(row, row + length))

    # Check the sums of columns
    for j in range(col, col + length):
        sum_col = sum(A[i][j] for i in range(row, row + length))
        if sum_col != sum_value:
            return False

    # Check the sums of rows
    for i in range(row, row + length):
        sum_row = sum(A[i][j] for j in range(col, col + length))
        if sum_row != sum_value:
            return False

    # Check the sum of the main diagonal
    sum_diagonal = sum(A[row + counter][col + counter] for counter in range(length))
    if sum_diagonal != sum_value:
        return False

    # Check the sum of the secondary diagonal
    sum_diagonal = sum(A[row + counter][col + length - 1 - counter] for counter in range(length))
    if sum_diagonal != sum_value:
        return False

    return True

def solution(A):
    max_square_length = min(len(A), len(A[0]))
    max_side_length = 1

    for i in range(len(A)):
        for j in range(len(A[i])):
            for k in range(2, max_square_length + 1):
                if i + k - 1 < len(A) and j + k - 1 < len(A[0]):
                    if is_magic_square(A, i, j, k):
                        max_side_length = max(max_side_length, k)

    return max_side_length
