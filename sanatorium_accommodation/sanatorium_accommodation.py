def solution(A):
    arr = sorted(A)
    counter = 0
    i = 0
    while i < len(arr):
        counter += 1
        i += arr[i]

    return counter
