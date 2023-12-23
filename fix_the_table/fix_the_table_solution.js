function solution(A) {
    if (A.length === 1 || A.length === 2) return 1;
    A = A.sort((a, b) => a - b);
    let min = A[A.length - 1];
    for (let i = 0; i < A.length - 1; i++) {
        const currMax = Math.max(A[i] - A[0], A[A.length - 1] - A[i + 1]);
        if (currMax < min) min = currMax;
    }
    if (min === 0) min = 1;
    return min;
}
