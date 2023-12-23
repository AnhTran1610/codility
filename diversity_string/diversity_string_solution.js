function solution(N) {
    const minOccurance = Math.ceil(N/26)
    let occurance = minOccurance;
    for (let i = minOccurance; i <= N; i++) {
        if (N % i === 0) {
            occurance = i;
            break;
        }
    }
    const alphabet = 'abcdefghijklmnopqrstuvwxyz'
    let str = ''
    for (const i of alphabet) {
        if (str.length < N) {
            str += i.repeat(occurance);
        } else {
            break;
        }
    }
    return str;
}