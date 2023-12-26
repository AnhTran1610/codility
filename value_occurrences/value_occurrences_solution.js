function solution(A) {
    let counter = 0;
    let stack = [];
    for (let i = 0; i < A.length; i++) {
        if (stack.length === 0) {
            stack.push(A[i]);
        } else {
            if (A[i] === stack[stack.length - 1]) {
                stack.push(A[i]);
            } else {
                const currValue = stack[stack.length - 1];
                if (currValue < stack.length) {
                    counter += stack.length - currValue;
                } else {
                    if (stack.length < currValue / 2) {
                        counter += stack.length;
                    } else {
                        counter += currValue - stack.length;
                    }
                }
                stack = [A[i]];
            }
        }
    }
    const currValue = stack[stack.length - 1];
    if (currValue < stack.length) {
        counter += stack.length - currValue;
    } else {
        if (stack.length < currValue / 2) {
            counter += stack.length;
        } else {
            counter += currValue - stack.length;
        }
    }
    return counter;
}
