function solution(i, j, k) {
    let result = 0;
    for (let num = i; num <= j; num++) {
        const numStr = num.toString();
        for (let digit of numStr) {
            if (digit === k.toString()) {
                result++;
            }
        }
    }
    return result;
}