def solution(A):
    temp = []
    prev = 0
    
    for num in A:
        if num != prev:
            temp.append(num)
            prev = num
    
    if len(temp) == 1:
        return 1
    if len(temp) == 2:
        return 2

    counter = 2
    for i in range(1, len(temp) - 1):
        is_hill = temp[i - 1] < temp[i] > temp[i + 1]
        is_valley = temp[i - 1] > temp[i] < temp[i + 1]

        if is_hill or is_valley:
            counter += 1

    return counter