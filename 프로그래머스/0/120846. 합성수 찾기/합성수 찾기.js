function solution(n) {
    let count = 0;

    for (let i = 4; i <= n; i++) {
        let divisors = 0;
        for (let j = 1; j <= Math.sqrt(i); j++) {
            if (i % j === 0) {
                if (j * j === i) {
                    divisors++;
                } else {
                    divisors += 2;
                }
            }
        }
        if (divisors >= 3) {
            count++;
        }
    }

    return count;
}