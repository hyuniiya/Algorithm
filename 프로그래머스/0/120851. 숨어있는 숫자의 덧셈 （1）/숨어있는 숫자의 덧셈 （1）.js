function solution(my_string) {
    let sum = 0;
    let str = my_string.split('');
    for(let i of str)
    if(!isNaN(i)) {
        sum += parseInt(i);
    }
    return sum;
}