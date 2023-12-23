def solution(P, S):
    sum_of_people = sum(P)
    cars = sorted(S, reverse=True)
    
    counter = 1
    total_seats = cars[0]
    curr_idx = 1
    
    while total_seats < sum_of_people:
        counter += 1
        total_seats += cars[curr_idx]
        curr_idx += 1
    
    return counter
