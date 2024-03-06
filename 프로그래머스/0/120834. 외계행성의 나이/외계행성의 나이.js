function solution(age) {
    let result = '';
    const alphabet = ['a','b','c','d','e','f','g','h','i','j']
    const ageStr = age.toString();
    
    for(let i = 0; i < ageStr.length; i++){
        result = result + alphabet[ageStr[i]];
    }
    return result;
}