function solution(A) {
    if (A.length === 1) {
        return 0;
    }
    if (A.length === 2) {
        if ((A[0] + A[1]) % 2 === 0) {
            return 1;
        }
        return 0;
    }

    const arr = [];
    for (let i = 0; i < A.length - 1; i++) {
        arr.push(A[i] + A[i + 1]);
    }
    arr.push(A[A.length - 1] + A[0])

    let counter = 0;
    let isFirst = false;
    let isLast = false;

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] % 2 === 0) {
            if (i === 0) {
                isFirst = true;
            }
            if (i === arr.length - 1) {
                isLast = true;
            }
            counter++;
            i++;
        }
    }
    if (isFirst && isLast) {
        counter--;
    }
    return counter;
}