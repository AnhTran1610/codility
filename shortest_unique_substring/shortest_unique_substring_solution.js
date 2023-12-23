function findOccurence(S, substr) {
    let counter = 1;
    let firstIndex = S.indexOf(substr);
    while (firstIndex !== -1) {
        const secondIndex = S.indexOf(substr, firstIndex + 1);
        if (secondIndex !== -1) {
            counter++;
        }
        firstIndex = secondIndex;
    }
    return counter;
}

function solution(S) {
    let subLength = 1;
    for (let i = subLength; i < S.length; i++) {
        for (let j = 0; j < S.length - i + 1; j++) {
            const substr = S.substring(j, j + i);
            if (findOccurence(S, substr) <= 1) {
                return i;
            }
        }
    }
    return S.length;
}
