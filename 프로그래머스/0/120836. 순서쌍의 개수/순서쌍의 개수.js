function solution(n) {
    let result = [];
    for(let i =0; i<=n; i++){
        n%i === 0 ? result.push(i):'';
    }
    return result.length;
}