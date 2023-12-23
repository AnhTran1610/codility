def solution(A):
    # Step 1: Check for edge cases
    if len(A) == 1:
        return 0
    elif len(A) == 2:
        # Check if the sum of the two elements is even
        if (A[0] + A[1]) % 2 == 0:
            return 1
        return 0

    # Step 2: Create an array by summing consecutive elements and adding the last with the first
    arr = [A[i] + A[i + 1] for i in range(len(A) - 1)]
    arr.append(A[-1] + A[0])

    # Step 3: Count pairs where the sum is even, considering the first and last pairs
    counter = 0
    is_first = False
    is_last = False

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            if i == 0:
                is_first = True
            if i == len(arr) - 1:
                is_last = True
            counter += 1
            i += 1

    # Step 4: Adjust the counter based on whether the first and last pairs are both even
    if is_first and is_last:
        counter -= 1

    # Step 5: Return the final counter
    return counter
