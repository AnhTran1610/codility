def solution(D, C, P):
    # Create a list of objects
    monitors = [{'distance': D[i], 'monitor': C[i]} for i in range(len(D))]

    # Sort the list based on distance and monitor cost
    sorted_monitors = sorted(monitors, key=lambda x: (x['distance'], x['monitor']))

    # Iterate through the sorted list
    counter = 0
    for i in range(len(sorted_monitors)):
        if P >= sorted_monitors[i]['monitor']:
            P -= sorted_monitors[i]['monitor']
            counter += 1
        else:
            return counter

    return counter
