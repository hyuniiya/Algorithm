function solution(num_list) {
    let result;
    
    if (num_list.length >= 11) {
        result = 0;
        for (const num of num_list) {
            result += num;
        }
    } else {
        result = 1;
        for (const num of num_list) {
            result *= num;
        }
    }

    return result;
}