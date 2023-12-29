function solution(A) {
    let occurance = [];
    let obj = {};
    for (let i = 0; i < A.length; i++) {
        if (obj[A[i]] === undefined) {
            obj[A[i]] = 1;
        } else {
            obj[A[i]] ++;
        }
    }
    for (const i in obj) {
        occurance.push(obj[i]);
    }
    const resArr = [];
    for (let i = 1; i <= occurance[occurance.length - 1]; i++) {
        resArr.push(i);
    }
    const numOfOccurance = {}
    for (const i of occurance) {
        if (numOfOccurance[i] === undefined) {
            numOfOccurance[i] = 1;
        } else {
            numOfOccurance[i] ++;
        }
    }
    let counter = 0;

    for (let i = 0; i < occurance.length; i++) {
        let occurDown = occurance[i];
        let occur = occurance[i]
        if (numOfOccurance[occur] > 1) {
            numOfOccurance[occurDown]--;
            while(numOfOccurance[occurDown] > 0 && occurDown > 0) {
                occurDown--;
                counter++;
            }
            if (occurDown > 0) numOfOccurance[occurDown] = 1;
        }
    }
    return counter;
}
