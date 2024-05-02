function solution(s){
    const pCount = (s.toUpperCase().match(/P/g) || []).length;
    const yCount = (s.toUpperCase().match(/Y/g) || []).length;

    return pCount === yCount;
}