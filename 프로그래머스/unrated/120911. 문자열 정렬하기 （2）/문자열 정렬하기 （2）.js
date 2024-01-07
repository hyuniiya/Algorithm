function solution(my_string) {
    var answer = '';
    var str = my_string.toLowerCase(); 
    var arr = Array.from(str);
    arr = arr.sort(); 
    answer = arr.join('').replaceAll(',', '');
    return answer;
}