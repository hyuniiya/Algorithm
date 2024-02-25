function solution(money) {
    const ice = 5500;
    const count = Math.floor(money / ice);
    const rest = money % ice;
    
    return [count , rest];
}