function solution(B) {
    const row = B.length;
    const col = B[0].length;
    const n = row * col;
    let patrolCounter = 0;
    let submarineCounter = 0;
    let destroyerCounter = 0;
    let obj = {};


    //destroyer
    for (let i = 0; i < n; i++) {
        let x = Math.floor(i / col);
        let y = i % col;
        if (!obj[i]) {
            if (B[x][y] === "#") {
                let up = undefined;
                let left = undefined;
                let down = undefined;
                let right = undefined;

                if (x - 1 >= 0) up = B[x-1][y];
                if (y - 1 >= 0) left = B[x][y - 1];
                if (x + 1 < row) down = B[x + 1][y];
                if (y - 1 < col) right = B[x][y +1];

                if (up === "#" && down === "#") {
                    if (!obj[(x-1)*col +y] && !obj[(x+1)*col + y]) {
                        destroyerCounter++;
                        obj[(x-1)*col + y] = true;
                        obj[(x+1)*col + y] = true;
                        obj[i] = true;
                    }
                    continue; 
                }
                if (left === '#' && down === '#') {
                    if (!obj[x*col + y - 1] && !obj[(x+1)*col + y]) {
                        destroyerCounter++;
                        obj[x*col + y - 1] = true;
                        obj[(x+1)*col + y] = true;
                        obj[i] = true;
                    }
                    continue;
                }
                if (right === '#' && down === '#') {
                    if (!obj[x*col + y +1] && !obj[(x+1)*col + y]) {
                        destroyerCounter++;
                        obj[x*col + y + 1] = true;
                        obj[(x+1)*col + y] = true;
                        obj[i] = true;
                    }
                    continue;
                }
                if (right === '#' && up === '#') {
                    if (!obj[x*col + y + 1] && !obj[(x-1)*col + y]) {
                        destroyerCounter++;
                        obj[x*col + y + 1] = true;
                        obj[(x-1)*col + y] = true;
                        obj[i] = true;
                    }
                    continue;
                }
                if (left === '#' && up === '#') {
                    if (!obj[x*col + y - 1] && !obj[(x-1)*col + y]) {
                        destroyerCounter++;
                        obj[x*col + y - 1] = true;
                        obj[(x-1)*col + y] = true;
                        obj[i] = true;
                    }
                    continue;
                }
                if (left === '#' && right === '#') {
                    if (!obj[x*col + y - 1] && !obj[x*col + y + 1]){
                        destroyerCounter++;
                        obj[x*col + y - 1] = true;
                        obj[x*col + y + 1] = true;
                        obj[i] = true
                    }
                    continue;
                }
            }
        }
    }
    //submarine
    for (let i = 0; i < n; i++) {
        let x = Math.floor(i / col);
        let y = i % col
        if (!obj[i]) {
            if (B[x][y] === "#") {
                let up = undefined;
                let left = undefined;
                let down = undefined;
                let right = undefined;

                if (x - 1 >= 0) up = B[x - 1][y];
                if (y - 1 >= 0) left = B[x][y - 1];
                if (x + 1 < row) down = B[x + 1][y];
                if (y - 1 < col) right = B[x][y + 1];

                if (up === "#") {
                    if (!obj[(x-1)*col + y]){
                        submarineCounter++;
                        obj[(x-1)*col + y] = true;
                        obj[i] = true;
                    }
                    continue;
                }
                if (left === '#') {
                    if (!obj[x*col + y - 1]){
                        submarineCounter++;
                        obj[x*col + y - 1] = true;
                        obj[i] = true;
                    }
                    continue;
                }
                if (down === '#') {
                    if (!obj[(x+1)*col + y]){
                        submarineCounter++;
                        obj[(x+1)*col + y] = true;
                        obj[i] = true;
                    }
                    continue;
                }
                if (right === '#') {
                    if (!obj[x*col + y + 1]){
                        submarineCounter++;
                        obj[x*col + y + 1] = true;
                        obj[i] = true;
                    }
                    continue;
                }
            }
        }
    }
    //Patrol
    for (let i = 0; i < n; i++) {
        let x = Math.floor(i / col);
        let y = i % col;
        if (!obj[i]) {
            if (B[x][y] === "#") {
                patrolCounter++;
            }
        }
    }

    return [patrolCounter, submarineCounter, destroyerCounter]
}

const A = [".##.#", "#.#..", "#...#", "#.##."]
const A1 = [".#..#", "##..#", "...#."]
const A2 = ["##.", "#.#", ".##"]