def solution(B):
    row = len(B)
    col = len(B[0])
    n = row * col
    patrolCounter = 0
    submarineCounter = 0
    destroyerCounter = 0
    obj = {}

    # Destroyer
    for i in range(n):
        x = i // col
        y = i % col
        if i not in obj:
            if B[x][y] == "#":
                up = B[x-1][y] if x - 1 >= 0 else None
                left = B[x][y-1] if y - 1 >= 0 else None
                down = B[x+1][y] if x + 1 < row else None
                right = B[x][y+1] if y + 1 < col else None

                if up == "#" and down == "#":
                    if (x-1)*col+y not in obj and (x+1)*col+y not in obj:
                        destroyerCounter += 1
                        obj[(x-1)*col+y] = True
                        obj[(x+1)*col+y] = True
                        obj[i] = True
                    continue
                if left == '#' and down == '#':
                    if x*col+y-1 not in obj and (x+1)*col+y not in obj:
                        destroyerCounter += 1
                        obj[x*col+y-1] = True
                        obj[(x+1)*col+y] = True
                        obj[i] = True
                    continue
                if right == '#' and down == '#':
                    if x*col+y+1 not in obj and (x+1)*col+y not in obj:
                        destroyerCounter += 1
                        obj[x*col+y+1] = True
                        obj[(x+1)*col+y] = True
                        obj[i] = True
                    continue
                if right == '#' and up == '#':
                    if x*col+y+1 not in obj and (x-1)*col+y not in obj:
                        destroyerCounter += 1
                        obj[x*col+y+1] = True
                        obj[(x-1)*col+y] = True
                        obj[i] = True
                    continue
                if left == '#' and up == '#':
                    if x*col+y-1 not in obj and (x-1)*col+y not in obj:
                        destroyerCounter += 1
                        obj[x*col+y-1] = True
                        obj[(x-1)*col+y] = True
                        obj[i] = True
                    continue
                if left == '#' and right == '#':
                    if x*col+y-1 not in obj and x*col+y+1 not in obj:
                        destroyerCounter += 1
                        obj[x*col+y-1] = True
                        obj[x*col+y+1] = True
                        obj[i] = True
                    continue

    # Submarine
    for i in range(n):
        x = i // col
        y = i % col
        if i not in obj:
            if B[x][y] == "#":
                up = B[x-1][y] if x - 1 >= 0 else None
                left = B[x][y-1] if y - 1 >= 0 else None
                down = B[x+1][y] if x + 1 < row else None
                right = B[x][y+1] if y + 1 < col else None

                if up == "#":
                    if (x-1)*col+y not in obj:
                        submarineCounter += 1
                        obj[(x-1)*col+y] = True
                        obj[i] = True
                    continue
                if left == '#':
                    if x*col+y-1 not in obj:
                        submarineCounter += 1
                        obj[x*col+y-1] = True
                        obj[i] = True
                    continue
                if down == '#':
                    if (x+1)*col+y not in obj:
                        submarineCounter += 1
                        obj[(x+1)*col+y] = True
                        obj[i] = True
                    continue
                if right == '#':
                    if x*col+y+1 not in obj:
                        submarineCounter += 1
                        obj[x*col+y+1] = True
                        obj[i] = True
                    continue

    # Patrol
    for i in range(n):
        x = i // col
        y = i % col
        if i not in obj:
            if B[x][y] == "#":
                patrolCounter += 1

    return [patrolCounter, submarineCounter, destroyerCounter]
