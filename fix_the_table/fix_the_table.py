def solution(A):
    # Step 1: Check for edge cases
    if len(A) == 1 or len(A) == 2:
        return 1

    # Step 2: Sort the array in ascending order
    A.sort()

    # Step 3: Initialize the minimum difference as the maximum element of the sorted array
    min_diff = A[-1]

    # Step 4: Iterate through the sorted array and find the minimum difference
    for i in range(len(A) - 1):
        curr_max = max(A[i] - A[0], A[-1] - A[i + 1])
        if curr_max < min_diff:
            min_diff = curr_max

    # Step 5: Handle the case when the minimum difference is 0
    if min_diff == 0:
        min_diff = 1

    # Step 6: Return the final minimum difference
    return min_diff
