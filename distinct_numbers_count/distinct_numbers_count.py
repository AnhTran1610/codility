def solution(A):
    occurrence = []
    occurrences_dict = {}
    
    # Count occurrences of each element
    for elem in A:
        if elem not in occurrences_dict:
            occurrences_dict[elem] = 1
        else:
            occurrences_dict[elem] += 1
    
    # Store the counts in a list
    occurrence.extend(occurrences_dict.values())
    
    res_arr = list(range(1, occurrence[-1] + 1))
    
    num_of_occurrence = {}
    
    # Count the occurrences of occurrence counts
    for count in occurrence:
        if count not in num_of_occurrence:
            num_of_occurrence[count] = 1
        else:
            num_of_occurrence[count] += 1
    
    counter = 0
    
    for i in range(len(occurrence)):
        occur_down = occurrence[i]
        occur = occurrence[i]
        
        # Handle occurrences with count greater than 1
        if num_of_occurrence[occur] > 1:
            num_of_occurrence[occur_down] -= 1
            while occur_down > 0 and occur_down in num_of_occurrence and num_of_occurrence[occur_down] > 0:
                occur_down -= 1
                counter += 1
            if occur_down > 0:
                num_of_occurrence[occur_down] = 1
    
    return counter
