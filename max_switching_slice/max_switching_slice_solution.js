function solution(A) {
    if (A.length === 1) {
        return 1;
    }
    if (A.length === 2) {
        return 2;
    }
    if (A.length === 3) {
        if (A[0] === A[2]) {
            return 3;
        } else {
            return 2;
        }
    }
    let max = 2;
    let currLength = 2;
    let first = A[0];
    let second = A[1];
    for (let i = 2; i < A.length; i++) {
        if (i === A.length - 1) {
            if (A[i] === first) {
                currLength++;
            }
            if (currLength > max) max = currLength;
        } else {
            if (A[i] === first) {
                currLength++;
                if (A[i + 1] === second) {
                    currLength++;
                    i++;
                } else {
                    if (currLength > max) max = currLength;
                    currLength = 2;
                    first = A[i];
                    second = A[i + 1];
                    i++;
                }
            } else {
                if (currLength > max) max = currLength;
                currLength = 2;
                first = A[i - 1];
                second = A[i];
            }
        }
    }
    if (currLength > max) max = currLength;
    return max;
}
