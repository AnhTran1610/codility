function solution(S) {
    let a = 0;
    let b = 0;
    for (let i = 0; i < S.length; i++) {
        if (S[i] === 'A') {
            a++;
        }
    }
    const ans = a;
    for (let i = 0; i < S.length; i++) {
        if (S[i] === 'A') {
            a--;
        } else {
            b++;
        }
        ans = Math.min(ans, a + b)
    }
    return ans;
}