def solution(A):
    if len(A) == 1:
        return 0
    if len(A) == 2:
        if (A[0] + A[1]) % 2 == 0:
            return 1
        return 0

    arr = []
    for i in range(len(A) - 1):
        arr.append(A[i] + A[i + 1])
    arr.append(A[-1] + A[0])

    counter1 = 0
    isFirst = False
    isLast = False
    i = 0
    while i < len(arr):
        if arr[i] % 2 == 0:
            if i == 0:
                isFirst = True
            if i == len(arr) - 1:
                isLast = True
            counter1 += 1
            i += 1
        i += 1

    if isFirst and isLast:
        counter1 -= 1

    counter2 = 0
    i = 1
    while i < len(arr):
        if arr[i] % 2 == 0:
            counter2 += 1
            i += 1
        i += 1

    return max(counter1, counter2)
