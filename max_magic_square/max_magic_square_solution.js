function isMagicSquare(A, row, col, length) {
    let sum = 0;
    for (let i = row; i < row + length; i++) {
        sum += A[i][col];
    }
    for (let j = col; j < col + length; j++) {
        let sumCol = 0;
        for (let i = row; i < row + length; i++) {
            sumCol += A[i][j];
        }
        if (sumCol !== sum) {
            return false;
        }
    }

    for (let i = row; i < row + length; i++) {
        let sumRow = 0;
        for (let j = col; j < col + length; j++) {
            sumRow += A[i][j];
        }
        if (sumRow !== sum) {
            return false;
        }
    }

    let counter = 0;
    let sumDiagonal = 0;

    while(counter < length) {
        sumDiagonal += A[row + counter][col + counter];
        counter++;
    }
    if (sumDiagonal !== sum) {
        return false;
    }

    sumDiagonal = 0;
    counter = 0;
    let j = col + length -1;
    while (counter < length) {
        sumDiagonal += A[row + counter][j - counter];
        counter++;
    }
    if (sumDiagonal !== sum) {
        return false;
    }

    return true;

}

function solution(A) {
    const maxSquareLength = Math.min(A.length, A[0].length)
    let max = 1;
    for (let i = 0; i < A.length; i++) {
        for (let j = 0; j < A[i].length; j++) {
            for (let k = 2; k <= maxSquareLength; k++) {
                if (i + k - 1 < A.length && j + k - 1 < A[0].length) {
                    console.log(i, j, k);
                    if (isMagicSquare(A, i, j, k)) {
                        if (k > max) max = k;
                    }
                }
            }
        }
    }
    return max;
}
