function solution(S) {
    for (let j = 0; j < S[0].length; j++) {
        const obj = {};
        for (let i = 0; i < S.length; i++) {
            if (obj[S[i][j] === undefined]) {
                obj[S[i][j]] = i;
            } else {
                return [obj[S[i][j]], i, j];
            }
        }
    }
    return [];
}