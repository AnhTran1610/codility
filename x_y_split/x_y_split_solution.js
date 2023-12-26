function solution(S) {
    let counter = 0;
    let x = 0;
    let y = 0;
    const indexes = {};
    for (let i = 0; i < S.length - 1; i++) {
        if (S[i] === 'x') {
            x++;
        }
        if (S[i] === 'y') {
            y++;
        }
        if (x === y) {
            indexes[i + 1] = true;
            counter++;
        }
    }
    
    x = 0;
    y = 0;
    let counter1 = 0;
    for (let i = S.length - 1; i > 0; i--) {
        if (S[i] === 'x') {
            x++;
        }
        if (S[i] === 'y') {
            y++;
        }
        if (x === y && indexes[i] === undefined) {
            counter1++;
        }
    }
    return counter + counter1;
}