def solution(A):
    counter = 0
    res_arr = []
    id_obj = {}
    # Iterate over rows of the 2D array
    for i in range(len(A)):
        obj = {}
        # Iterate over columns of each row
        for j in range(len(A[0])):
            id_val = A[i][j]
            # Track unique values in the current row
            if id_val not in obj:
                obj[id_val] = True
            # Track unique values across all rows
            if id_val not in id_obj:
                id_obj[id_val] = True
        # Store the unique values in the current row
        res_arr.append(obj)
    # Get an array of unique values across all rows
    id_arr = list(id_obj.keys())
    # Count the columns where there are at least two rows with the same value
    for i in range(len(id_arr)):
        count = 0
        # Iterate over rows and check if the value exists in the current column
        for j in range(len(res_arr)):
            if id_arr[i] in res_arr[j]:
                count += 1
        # If there are at least two rows with the same value, increment the counter
        if count >= 2:
            counter += 1
    return counter
