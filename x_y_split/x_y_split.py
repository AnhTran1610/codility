def solution(S):
    counter = 0
    x = 0
    y = 0
    indexes = {}

    # Forward iteration through the string
    for i in range(len(S) - 1):
        if S[i] == 'x':
            x += 1
        if S[i] == 'y':
            y += 1
        if x == y:
            # If the count of 'x' equals the count of 'y', mark the index and increment the counter
            indexes[i + 1] = True
            counter += 1

    # Reset counts for backward iteration
    x = 0
    y = 0
    counter1 = 0

    # Backward iteration through the string
    for i in range(len(S) - 1, 0, -1):
        if S[i] == 'x':
            x += 1
        if S[i] == 'y':
            y += 1
        if x == y and i not in indexes:
            # If the count of 'x' equals the count of 'y' and the index is not marked, increment the counter1
            counter1 += 1

    # Return the sum of the two counters
    return counter + counter1

