def solution(A):
    occurrence = []
    obj = {}

    # Count occurrences of each element in A
    for element in A:
        if obj.get(element) is None:
            obj[element] = 1
        else:
            obj[element] += 1

    # Collect the occurrences in a list
    for key in obj:
        occurrence.append(obj[key])

    res_arr = []

    # Generate a list of numbers from 1 to the maximum occurrence
    for i in range(1, occurrence[-1] + 1):
        res_arr.append(i)

    num_of_occurrence = {}

    # Count the occurrence of occurrences
    for i in occurrence:
        if num_of_occurrence.get(i) is None:
            num_of_occurrence[i] = 1
        else:
            num_of_occurrence[i] += 1

    counter = 0

    for i in range(len(occurrence)):
        occur_down = occurrence[i]
        occur = occurrence[i]

        if num_of_occurrence[occur] > 1:
            num_of_occurrence[occur_down] -= 1

            while num_of_occurrence[occur_down] > 0 and occur_down > 0:
                occur_down -= 1
                counter += 1

            if occur_down > 0:
                num_of_occurrence[occur_down] = 1

    return counter
