def solution(A):
    counter = 0
    obj = {}
    counter_id = {}

    for i in range(len(A)):
        for j in range(len(A[0])):
            id_value = A[i][j]

            if obj.get(id_value) and counter_id.get(id_value) is None:
                counter += 1
                counter_id[id_value] = True

        for j in range(len(A[0])):
            id_value = A[i][j]

            if obj.get(id_value) is None:
                obj[id_value] = True

    return counter
