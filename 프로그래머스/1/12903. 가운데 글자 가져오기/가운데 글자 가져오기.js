function solution(s) {
    const middleIndex = Math.floor(s.length / 2);
    return s.length % 2 === 0 
    ? s.substr(middleIndex - 1, 2) 
    : s.charAt(middleIndex);
}