def solution(N):
    # Calculate the minimum occurrence needed
    min_occurrence = -(-N // 26)
    occurrence = min_occurrence

    # Find the smallest occurrence that divides N evenly
    for i in range(min_occurrence, N + 1):
        if N % i == 0:
            occurrence = i
            break

    # Define the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Generate the string by repeating alphabet characters
    result_str = ''
    for char in alphabet:
        if len(result_str) < N:
            result_str += char * occurrence

    return result_str
