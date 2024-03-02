function solution(n, numlist) {
    const result = [];
    
    for (let num of numlist) {
        if (num % n === 0) {
            result.push(num);
        }
    }
    
    return result;
}