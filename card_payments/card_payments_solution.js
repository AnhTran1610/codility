function solution(A, D) {
    const obj = {};
    for (let i = 0; i < D.length; i++) {
        const month = D[i].split('-')[1];
        if (A[i] < 0) {
            if (obj[month] === undefined) {
                obj[month] = {
                    totalPayment: Math.abs(A[i]),
                    countPayment: 1,
                }
            } else {
                obj[month].totalPayment += Math.abs(A[i]);
                obj[month].countPayment += 1;
            }
        }
    }

    let total = 0;
    for (let i = 0; i < A.length; i++) {
        total += A[i];
    }

    for (i = 1; i <= 12; i++) {
        let key = i.toString();
        if (i < 10) {
            key = '0' + key;
        }
        if (obj[key] === undefined) {
            total = total - 5;
        } else {
            if (obj[key].totalPayment < 100 || obj[key].countPayment <3) {
                total = total - 5;
            }
        }
    }
    return total;
}