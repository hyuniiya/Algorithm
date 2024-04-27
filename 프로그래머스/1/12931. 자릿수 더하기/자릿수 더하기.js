function solution(N) {
    if (N < 10) {
        return N;
    } else {
        return N % 10 + solution(Math.floor(N / 10));
    }
}