function solution(S) {
    let flag = false;
    for (let i = 0; i < S.length; i++) {
        if (S[i] === 'b') {
            flag = true;
        }
        if (S[i] === 'a') {
            if (flag === true) return false;
        }
    }
    return true;
}