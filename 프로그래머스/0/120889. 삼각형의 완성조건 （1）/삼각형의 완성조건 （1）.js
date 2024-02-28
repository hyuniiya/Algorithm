function solution(sides) {
    sides.sort((a, b) => a - b);
    const long = sides[2];
    const other = sides[0] + sides[1];

    return (long < other) ? 1 : 2;
}