def solution(numbers):
    counter = 0
    first = []
    last = {}
    duplicate = 0

    for num in numbers:
        first_digit = int(str(num)[0])
        first.append(first_digit)

        last_digit = num % 10

        if first_digit == last_digit:
            duplicate += 1

        last[last_digit] = last.get(last_digit, 0) + 1

    for i in range(len(first)):
        num_of_lasts = last.get(first[i], 0)
        counter += num_of_lasts

    return counter - duplicate
