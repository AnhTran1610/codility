function solution(S) {
    const A = S.split(""); // Convert the string to an array of characters
    let low = 0;
    let high = A.length - 1;

    while (low < high) {
        if (A[low] !== A[high]) {
            // If the characters at the current positions are not equal
            if (A[low] === '?' && A[high] !== '?') {
                A[low] = A[high]; // Fill in '?' with the character at the opposite end
            } else if (A[low] !== '?' && A[high] === '?') {
                A[high] = A[low]; // Fill in '?' with the character at the opposite end
            } else {
                return 'NO'; // If both characters are not '?' and not equal, it's not possible to form a palindrome
            }
        } else {
            // If the characters at the current positions are equal
            if (A[low] === '?') {
                A[low] = 'a'; // If the character is '?', fill in 'a'
                A[high] = 'a';
            }
        }
        low++;
        high--;
    }

    // Check if there is a single character left in the middle of the string and fill it with 'a'
    if (low === high && A[low] === '?') {
        A[low] = 'a';
    }

    return A.join(""); // Convert the array back to a string and return the result
}
