function solution(S, F, M) {
    const sum = (S.length + F) * M;
    const totalMissing = num - S.reduce((res, value) => res += value);
    if (totalMissing <= 0) return [0];
    console.log(totalMissing, F)
    const avg = totalMissing / F;
    if (avg > 6 || avg < 1) return [0];
    const res = [];
    for (let i = 0; i < F - 1; i++) {
        res.push(Math.floor(avg));
    }
    let remaining = totalMissing - Math.floor(avg) * (F - 1);
    let currIdx = 0;
    while(currIdx < F - 1 && remaining > 6) {
        res[currIdx]++;
        if (remaining - 1 < 1) {
            break;
        }
        remaining -= 1;
        currIdx++;
    }
    res.push(remaining);
    return res;
}
