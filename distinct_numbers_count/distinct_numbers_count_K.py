def solution(A):
    print(A)
    print(f"uniques elements :{set(A)}")
    occurances = []
    delete_count = 0
    for e in set(A):
        occurances.append(A.count(e))
    occurances.sort(reverse=True)
    print(f"Before: {occurances}")
    i = 1
    while i < len(occurances):
        while occurances[i] >= occurances[i - 1] and occurances[i] > 0:
            occurances[i] -= 1
            delete_count += 1
        i += 1
    print(f"After: {occurances}")
    print(delete_count)
    return delete_count

assert solution(A=[1,1,1,2,2,2]) == 1