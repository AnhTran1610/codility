function solution(A) {
    const arr = A.sort((a, b) => a - b)
    let counter = 0;
    for (let i = 0; i < arr.length; i++) {
        counter += 1;
        i += arr[i] - 1;
    }
    console.log(arr)
    return counter;
}
