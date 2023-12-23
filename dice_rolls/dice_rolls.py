def solution(A, F, M):
    denominator = len(A) + F
    total_missing_value = M * denominator - sum(A)

    # Check if the calculated missing values are within a valid range
    if total_missing_value / F < 1 or total_missing_value / F > 6:
        print([0])
        return [0]

    # Calculate the missing values and distribute them among the elements
    res = [total_missing_value // F for i in range(F)]
    res[0] += total_missing_value % F

    print(res)
    return res
