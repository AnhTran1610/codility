function solution(A) {
    let counter = 0;
    const obj = {}
    const counterId = {};
    for (let i = 0; i < A.length; i++) {
        for (let j = 0; j < A[0].length; j++) {
            const id = A[i][j];
            if (obj[id] && counterId[id] === undefined) {
                counter++;
                counterId[id] = true;
            }
        }
        for (let j = 0; j < A[0].length; j++) {
            const id = A[i][j];
            if (obj[id] === undefined) {
                obj[id] = true;
            }
        }
    }
    return counter;
}