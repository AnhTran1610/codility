def find_initial(initial_a, initial_b, R, V):
    a = initial_a
    b = initial_b
    for i in range(len(R)):
        if R[i] == "B":
            a -= V[i]
            b += V[i]
            if a < 0:
                return find_initial(initial_a +1, initial_b, R, V)
        else:
            a += V[i]
            b -= V[i]
            if b < 0:
                return find_initial(initial_a, initial_b + 1, R, V)
        print(f"iteration {i}: initial_a = {initial_a}, initial_b = {initial_b}")
    return [initial_a, initial_b]

def solution(R, V):
    initial_a = 0
    initial_b = 0
    return find_initial(initial_a, initial_b, R, V)
