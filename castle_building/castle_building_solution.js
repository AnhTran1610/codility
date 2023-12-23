function solution(A) {
    const temp = [];
    let prev = 0;
    for (let i = 0; i < A.length; i++) {
        if (A[i] !== prev) {
            temp.push(A[i]);
            prev = A[i];
        }
    }

    if (temp.length === 1) return 1;
    if (temp.length === 2) return 2;

    let counter = 2;
    for (let i = 1; i < temp.length - 1; i++) {
        const isHill = temp[i - 1] < temp[i] && temp[i] > temp[i + 1]
        const isValley = temp[i - 1] > temp[i] && temp[i] < temp[i + 1]
        if (isHill || isValley) {
            counter++;
        }
    }
    return counter;
}