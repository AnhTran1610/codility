function solution(A) {
    let occurance = [];
    let obj = {};
    for (let i = 0; i < A.length; i++) {
        if (obj[A[i]] === undefined) {
            obj [A[i]] = 1;
        } else {
            obj[A[i]] ++;
        }
    }
    for (const i in obj) {
        occurance.push(obj[i]);
    }
    occurance = occurance.sort((a, b) => b - a)
    const numOfOccurance = {}
    for (const i of occurance) {
        if (numOfOccurance[i] === undefined) {
            numOfOccurance[i] = 1;
        } else {
            numOfOccurance[i] ++;
        }
    }
    const distinctOccurance = Object.keys(numOfOccurance).sort((a, b) => b - a);
    console.log(distinctOccurance)
    let counter = 0;
    let currMin = occurance[0] + 1;
    for (let i = 0; i < distinctOccurance.length; i++) {
        const num = Number(distinctOccurance[i]);
        const c = distinctOccurance[i];
        if (num < currMin) {
            if (numOfOccurance[num] > 1)
        }
    }
}