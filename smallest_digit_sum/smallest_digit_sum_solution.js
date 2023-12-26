function solution(N) {
    let curr = N;
    let resStr = '';
    while (curr > 9) {
        curr -= 9;
        resStr = '9' + resStr;
    }
    resStr = curr + resStr;
    return Number(resStr);
}
