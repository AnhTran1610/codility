function solution(S) {
    let A = 0;
    let B = 0;
    let N = 0;
    for (let i = 0; i < S.length; i++) {
        if (S[i] === 'B') {
            B++;
        }
        if (S[i] === 'A') {
            A++;
        }
        if (S[i] === 'N') {
            N++;
        }
    }

    let counter = 0;
    while (B >= 1 && A >=3 && N >=2) {
        B -= 1;
        A -= 3;
        N -= 2;
        counter++;
    }
    return counter;
}