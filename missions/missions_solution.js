function solution(D, X) {
    let stack = [D[0]];
    let counter = 0;
    let min = D[0], max = D[0];
    for (let i = 0; i < D.length; i++) {
        if (Math.abs(D[i] - min) <= X && Math.abs(D[i] - max) <= X) {
            stack.push(A[i]);
            if (D[i] < min) {
                min = D[i];
            }
            if (D[i] > max) {
                max = D[i];
            }
        } else {
            counter++;
            stack = [D[i]];
            min = D[i];
            max = D[i];
        }
    }
    if (stack.length !== 0) counter++;
    return counter;
}
