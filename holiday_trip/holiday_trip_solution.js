function solution(P, S) {
    const sumOfPeople = P.reduce((total, curr) => total += curr);
    const cars = S.sort((a, b) => b - a);
    let counter = 1;
    let totalSeats = cars[0];
    let currIdx = 1;
    while(totalSeats < sumOfPeople) {
        counter++;
        totalSeats += cars[currIdx];
        currIdx++;
    }
    return counter;
}
