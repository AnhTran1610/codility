def solution(N):
    curr = N
    res_str = ''
    while curr > 9:
        curr -= 9
        res_str = '9' + res_str
    res_str = str(curr) + res_str
    return int(res_str)
