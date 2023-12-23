def solution(D, X):
    stack = [D[0]]
    counter = 0
    min_val = D[0]
    max_val = D[0]

    for i in range(len(D)):
        if abs(D[i] - min_val) <= X and abs(D[i] - max_val) <= X:
            stack.append(D[i])
            min_val = min(D[i], min_val)
            max_val = max(D[i], max_val)
        else:
            counter += 1
            stack = [D[i]]
            min_val = D[i]
            max_val = D[i]

    if stack:
        counter += 1

    return counter
