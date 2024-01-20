function solution(rsp) {
    let arr = { 2:0 , 0:5 , 5:2};
    let result = rsp.split('').map(i => arr[i]).join('');
    return result;
}