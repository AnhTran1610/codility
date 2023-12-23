function solution(S) {
    const arr = S.split('');
    let counter = 0;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === '^' || arr[i] === 'v') {
            counter++;
            arr[i] = 'o';
        }
        if (arr[i] === '<') {
            if (arr[i - 1] === undefined) {
                counter++;
                arr[i] = 'o';
            } else {
                if (arr[i - 1] === 'o') {
                    counter++;
                    arr[i] = 'o'
                }
            }
        }
        if (arr[i] === '>') {
            if (arr[i + 1] === undefined) {
                counter++;
                arr[i] = 'o';
            }
        }
    }
    return counter;
}
