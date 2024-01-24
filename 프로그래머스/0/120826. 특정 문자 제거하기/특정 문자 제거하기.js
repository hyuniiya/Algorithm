function solution(my_string, letter) {
    let result = my_string.split('').filter(i => i !== letter).join('');
    return result;
}