function solution(A, K) {
    let longestLength = A[0].toString().length;
    for (let i = 0; i < A.length; i++) {
        if (A[i].toString().length > longestLength) {
            longestLength = A[i].toString().length;
        }
    }
    let currIdx = 0;
    for (let i = 1; i <= Math.floor(A.length / K); i++) {
        let edge = '';
        for (let j = 1; j <= K; j++) {
            edge += '+' + '-'.repeat(longestLength);
        }
        edge += '+';
        console.log(edge);

        let num = '|';
        for (let j = 1; j <= K; j++) {
            const spaceNeeded = longestLength - A[currIdx].toString().length;
            num += ' '.repeat(spaceNeeded) + A[currIdx].toString() + '|';
            currIdx++;
        }
        console.log(num)
    }

    let nearLastEdge = K;
    if (Math.floor(A.length / K) < 1) {
        nearLastEdge = A.length % K;
    }
    let edge = '';
    for (let j = 1; j <= nearLastEdge; j++) {
        edge += '+' + '-'.repeat(longestLength);
    }
    edge += '+';
    console.log(edge);

    if (A.length % K !== 0) {
        let num = '|';
        for (let j = 1; j <= A.length % K; j++) {
            const spaceNeeded = longestLength - A[currIdx].toString().length;
            num += ' '.repeat(spaceNeeded) + A[currIdx].toString() + '|';
            currIdx++;
        }
        console.log(num)
        edge = '';
        for (let j = 1; j <= A.length % K; j++) {
            edge += '+' + '-'.repeat(longestLength);
        }
        edge += '+';
        console.log(edge);
    }
}
