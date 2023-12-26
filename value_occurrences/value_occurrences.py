def solution(A):
    counter = 0
    stack = []

    # Iterate through the array A
    for i in range(len(A)):
        if not stack:
            # If the stack is empty, push the current element onto the stack
            stack.append(A[i])
        else:
            if A[i] == stack[-1]:
                # If the current element is equal to the top of the stack, push it onto the stack
                stack.append(A[i])
            else:
                # If the current element is different from the top of the stack
                curr_value = stack[-1]

                # Update the counter based on certain conditions
                if curr_value < len(stack):
                    counter += len(stack) - curr_value
                else:
                    if len(stack) < curr_value / 2:
                        counter += len(stack)
                    else:
                        counter += curr_value - len(stack)

                # Reset the stack with the current element
                stack = [A[i]]

    # Process the remaining elements in the stack after the loop
    curr_value = stack[-1]
    if curr_value < len(stack):
        counter += len(stack) - curr_value
    else:
        if len(stack) < curr_value / 2:
            counter += len(stack)
        else:
            counter += curr_value - len(stack)

    # Return the final counter value
    return counter
