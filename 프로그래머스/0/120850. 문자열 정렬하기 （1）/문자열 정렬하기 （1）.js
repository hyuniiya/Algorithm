function solution(my_string) {
    let result = [];
    
    for (let char of my_string) {
        const digit = parseInt(char, 10);
        if (!isNaN(digit)) {
            result.push(digit);
        }
    }

    return result.sort((a, b) => a - b);
}