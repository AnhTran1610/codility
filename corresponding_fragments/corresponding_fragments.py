def solution(A, B):
    counter = 0

    for i in range(len(A)):
        subA = A[i]
        subB = B[i]

        if subA == subB:
            counter += 1

        for j in range(i + 1, len(A)):
            if A[j] is not None:
                subA += A[j]
                subB += B[j]

                objA = {}
                objB = {}

                for k in range(len(subA)):
                    objA[subA[k]] = objA.get(subA[k], 0) + 1
                    objB[subB[k]] = objB.get(subB[k], 0) + 1

                is_corresponding = all(objA.get(k, 0) == objB.get(k, 0) for k in set(objA.keys()) | set(objB.keys()))

                if is_corresponding:
                    counter += 1

    return counter