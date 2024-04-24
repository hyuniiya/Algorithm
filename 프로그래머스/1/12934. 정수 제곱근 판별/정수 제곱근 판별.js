function solution(n) {
    const sqrt = Math.sqrt(n);

    return sqrt === parseInt(sqrt, 10) ? Math.pow(sqrt + 1, 2) : -1;
}