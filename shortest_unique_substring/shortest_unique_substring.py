def find_occurrence(s, substr):
    counter = 1
    first_index = s.find(substr)
    while first_index != -1:
        second_index = s.find(substr, first_index + 1)
        if second_index != -1:
            counter += 1
        first_index = second_index
    return counter

def solution(s):
    sub_length = 1
    for i in range(sub_length, len(s)):
        for j in range(0, len(s) - i + 1):
            substr = s[j : j + i]
            if find_occurrence(s, substr) <= 1:
                return i
    return len(s)
