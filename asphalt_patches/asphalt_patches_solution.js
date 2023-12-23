function solution(S) {
    let count = 0;
    for (let i = 0; i < S.length; i++) {
        if (S[i] === 'X') {
            count++;
            if (i +2 >= S.length) break;
            i = i +2;
        }
    }
    return count;
};