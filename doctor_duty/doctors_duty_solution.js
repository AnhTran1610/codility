function solution(A) {
    let counter = 0;
    const resArr = [];
    const idObj = {}
    for (let i = 0; i < A.length; i++) {
        const obj = {};
        for (let j = 0; j < A[0].length; j++) {
            const id = A[i][j];
            if (obj[id] === undefined) {
                obj[id] = true;
            }
            if (idObj[id] === undefined) {
                idObj[id] = true;
            }
        }
        resArr.push(obj);
    }

    const idArr = Object.keys(idObj);

    for (let i = 0; i < idArr.length; i++) {
        let count = 0;
        for (let j = 0; j < resArr.length; j++) {
            if (resArr[j][idArr[i]] === true) {
                count++;
            }
        }
        if (count >= 2) counter++;
    }
    return counter;
}