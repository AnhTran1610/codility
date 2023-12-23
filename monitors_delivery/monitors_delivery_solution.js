function solution (D, C, P) {
    const list = [];
    for (let i = 0; i < D.length; i++) {
        const element = {
            distance: D[i],
            monitor: C[i],
        }
        list.push(element);
    }
    const sortedList = list.sort((a, b) => {
        if (a.distance !== b.distance) {
            return a.distance - b.distance;
        } else {
            return a.monitor - b.monitor;
        }
    });

    let counter = 0;
    for (let i = 0; i < sortedList.length; i++) {
        if (P >= sortedList[i].monitor) {
            P -= sortedList[i].monitor;
            counter++;
        } else {
            return counter;
        }
    }
    return counter;
}