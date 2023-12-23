def solution(S):
    arr = list(S)
    counter = 0

    for i in range(len(arr)):
        if arr[i] == '^' or arr[i] == 'v':
            counter += 1
            arr[i] = 'o'

        if arr[i] == '<':
            if i - 1 < 0 or arr[i - 1] == 'o':
                counter += 1
                arr[i] = 'o'

        if arr[i] == '>':
            if i + 1 >= len(arr):
                counter += 1
                arr[i] = 'o'

    return counter
