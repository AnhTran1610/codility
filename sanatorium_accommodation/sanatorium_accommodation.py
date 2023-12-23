def solution(A):
    # Sort the array in ascending order
    arr = sorted(A)

    # Initialize a counter for unique values
    counter = 0

    # Iterate through the sorted array
    i = 0
    while i < len(arr):
        # Increment the counter for each unique value
        counter += 1

        # Skip elements in the array based on their values (in this case if value = 1 will skip)
        i += arr[i] - 1

    # Return the count of unique values
    return counter
