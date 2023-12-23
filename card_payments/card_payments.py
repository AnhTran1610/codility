def solution(A, D):
    obj = {}
    
    for i in range(len(D)):
        month = D[i].split('-')[1]
        
        if A[i] < 0:
            if month not in obj:
                obj[month] = {
                    'totalPayment': abs(A[i]),
                    'countPayment': 1,
                }
            else:
                obj[month]['totalPayment'] += abs(A[i])
                obj[month]['countPayment'] += 1

    total = sum(A)

    for i in range(1, 13):
        key = str(i).zfill(2)
        
        if key not in obj:
            total -= 5
        elif obj[key]['totalPayment'] < 100 or obj[key]['countPayment'] < 3:
            total -= 5

    return total