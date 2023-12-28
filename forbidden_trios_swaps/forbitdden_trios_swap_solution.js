function solution(S) {
    let stack = [];
    let counter = 0;
    for (let i = 0; i < S.length; i++) {
        if (stack.length === 0) {
            stack.push(S[i]);
        } else {
            if (S[i] === stack[stack.length - 1]) {
                stack.push(S[i]);
            } else {
                if (stack.length >= 3) {
                    counter += Math.floor(stack.length / 3);
                }
                stack = [S[i]];
            }
        }
    }
    if (stack.length >= 3) {
        counter += Math.floor(stack.length / 3);
    }
    return counter;
}
