function solution(A) {
    let counter = 0;
    let first = [];
    let last = {};
    let duplicate = 0;
    for (let i = 0; i < A.length; i++) {
        const firstDigit = Number(A[i].toString()[0])
        first.push(firstDigit);
        const lastDigit = A[i] % 10;
        if (firstDigit === lastDigit) {
            duplicate += 1;
        }
        if (last[lastDigit] === undefined) {
            last[lastDigit] = 1;
        } else {
            last[lastDigit] ++;
        }
    }
    for (let i = 0; i < first.length; i++) {
        const numofLasts = last[first[i]];
        if (numofLasts !== undefined) {
            counter += numofLasts;
        }
    }
    return counter - duplicate;
}
