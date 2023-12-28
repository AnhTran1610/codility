def solution(S, F, M):
    total_length = (len(S) + F) * M
    total_missing = total_length - sum(S)

    if total_missing <= 0:
        return [0]

    avg = total_missing / F

    if avg > 6 or avg < 1:
        return [0]

    res = []

    for i in range(F - 1):
        res.append(int(avg))

    remaining = total_missing - int(avg) * (F - 1)
    curr_idx = 0

    while curr_idx < F - 1 and remaining > 6:
        res[curr_idx] += 1

        if remaining - 1 < 1:
            break

        remaining -= 1
        curr_idx += 1

    res.append(remaining)
    return res
